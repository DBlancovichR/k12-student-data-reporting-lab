#!/usr/bin/env python3
"""
Generates CALPADS-style, CBEDS-style, CRDC-style, and senior exit reporting extracts
from the SQLite database.

These are simplified reporting simulations using synthetic data only.
"""

import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "database" / "k12_student_reporting.db"
OUTPUT_DIR = ROOT / "reports" / "generated"


EXTRACTS = {
    "calpads_style_enrollment_extract.csv": """
        SELECT
            s.state_student_id,
            s.student_id,
            s.first_name,
            s.last_name,
            e.school_year,
            e.grade_level,
            e.entry_date,
            e.exit_date,
            e.exit_code,
            e.enrollment_status
        FROM enrollments e
        LEFT JOIN students s
            ON e.student_id = s.student_id
        ORDER BY e.grade_level, s.last_name, s.first_name;
    """,

    "calpads_style_program_participation_extract.csv": """
        SELECT
            s.state_student_id,
            s.student_id,
            s.first_name,
            s.last_name,
            p.program_name,
            p.program_status,
            p.start_date,
            p.end_date
        FROM programs p
        LEFT JOIN students s
            ON p.student_id = s.student_id
        ORDER BY p.program_name, s.last_name, s.first_name;
    """,

    "cbeds_style_school_summary.csv": """
        SELECT
            e.school_year,
            e.grade_level,
            COUNT(DISTINCT e.student_id) AS student_count
        FROM enrollments e
        WHERE e.enrollment_status = 'Active'
        GROUP BY e.school_year, e.grade_level
        ORDER BY e.school_year, e.grade_level;
    """,

    "crdc_style_discipline_extract.csv": """
        SELECT
            d.school_year,
            d.incident_type,
            d.action_taken,
            COUNT(*) AS incident_count,
            SUM(d.days_removed) AS total_days_removed
        FROM discipline d
        GROUP BY d.school_year, d.incident_type, d.action_taken
        ORDER BY d.school_year, d.action_taken, d.incident_type;
    """,

    "senior_exit_extract.csv": """
        SELECT
            s.state_student_id,
            s.student_id,
            s.first_name,
            s.last_name,
            s.enrollment_status,
            s.graduation_status,
            t.credits_attempted,
            t.credits_earned,
            t.gpa,
            t.graduation_eligible,
            t.notes
        FROM students s
        LEFT JOIN transcripts t
            ON s.student_id = t.student_id
        WHERE s.grade_level = 12
        ORDER BY s.last_name, s.first_name;
    """
}


def write_extract(conn, file_name, query):
    output_path = OUTPUT_DIR / file_name
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    headers = [description[0] for description in cursor.description]

    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"Generated {output_path.relative_to(ROOT)} ({len(rows)} rows)")


def main():
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not found: {DB_PATH}. Run scripts/build_database.py first."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    for file_name, query in EXTRACTS.items():
        write_extract(conn, file_name, query)

    conn.close()
    print(f"Reporting extracts generated: {len(EXTRACTS)}")


if __name__ == "__main__":
    main()
