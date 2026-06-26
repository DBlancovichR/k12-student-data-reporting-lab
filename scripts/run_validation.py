#!/usr/bin/env python3
"""
Runs education data validation checks against the SQLite database.

Outputs generated CSV reports to reports/generated/.
"""

import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "database" / "k12_student_reporting.db"
OUTPUT_DIR = ROOT / "reports" / "generated"

QUERIES = {
    "duplicate_student_records.csv": """
        SELECT
            student_id,
            state_student_id,
            COUNT(*) AS record_count
        FROM students
        GROUP BY student_id, state_student_id
        HAVING COUNT(*) > 1
        ORDER BY record_count DESC;
    """,

    "missing_exit_codes.csv": """
        SELECT
            enrollment_id,
            student_id,
            school_year,
            entry_date,
            exit_date,
            exit_code,
            grade_level,
            enrollment_status
        FROM enrollments
        WHERE enrollment_status = 'Inactive'
          AND exit_date IS NOT NULL
          AND (exit_code IS NULL OR exit_code = '');
    """,

    "invalid_grade_levels.csv": """
        SELECT
            enrollment_id,
            student_id,
            school_year,
            grade_level,
            enrollment_status
        FROM enrollments
        WHERE grade_level NOT BETWEEN 9 AND 12;
    """,

    "program_records_missing_status.csv": """
        SELECT
            program_record_id,
            student_id,
            program_name,
            program_status,
            start_date,
            end_date
        FROM programs
        WHERE program_status IS NULL OR program_status = '';
    """,

    "senior_exit_status_review.csv": """
        SELECT
            s.student_id,
            s.first_name,
            s.last_name,
            s.grade_level,
            s.enrollment_status,
            s.graduation_status,
            t.credits_attempted,
            t.credits_earned,
            t.graduation_eligible,
            t.notes
        FROM students s
        LEFT JOIN transcripts t
            ON s.student_id = t.student_id
        WHERE s.grade_level = 12
          AND (
                s.graduation_status IS NULL
                OR s.graduation_status = ''
                OR s.graduation_status = 'Behind Credits'
                OR t.credits_earned < 220
                OR t.credits_earned > t.credits_attempted
              )
        ORDER BY s.student_id;
    """,

    "data_quality_scorecard.csv": """
        SELECT 'Duplicate student records' AS check_name, COUNT(*) AS exception_count
        FROM (
            SELECT student_id
            FROM students
            GROUP BY student_id, state_student_id
            HAVING COUNT(*) > 1
        )

        UNION ALL

        SELECT 'Inactive enrollments missing exit codes' AS check_name, COUNT(*) AS exception_count
        FROM enrollments
        WHERE enrollment_status = 'Inactive'
          AND exit_date IS NOT NULL
          AND (exit_code IS NULL OR exit_code = '')

        UNION ALL

        SELECT 'Invalid grade levels' AS check_name, COUNT(*) AS exception_count
        FROM enrollments
        WHERE grade_level NOT BETWEEN 9 AND 12

        UNION ALL

        SELECT 'Program records missing status' AS check_name, COUNT(*) AS exception_count
        FROM programs
        WHERE program_status IS NULL OR program_status = ''

        UNION ALL

        SELECT 'Seniors missing graduation status' AS check_name, COUNT(*) AS exception_count
        FROM students
        WHERE grade_level = 12
          AND (graduation_status IS NULL OR graduation_status = '');
    """,

    "enrollment_by_grade.csv": """
        SELECT
            grade_level,
            COUNT(DISTINCT student_id) AS active_student_count
        FROM enrollments
        WHERE enrollment_status = 'Active'
        GROUP BY grade_level
        ORDER BY grade_level;
    """,

    "crdc_style_discipline_summary.csv": """
        SELECT
            action_taken,
            COUNT(*) AS incident_count,
            SUM(days_removed) AS total_days_removed
        FROM discipline
        GROUP BY action_taken
        ORDER BY incident_count DESC, action_taken;
    """
}


def write_query_to_csv(conn: sqlite3.Connection, output_file: Path, query: str) -> int:
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    headers = [description[0] for description in cursor.description]

    with output_file.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

    return len(rows)


def main():
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not found: {DB_PATH}. Run scripts/build_database.py first."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    total_outputs = 0

    for file_name, query in QUERIES.items():
        output_path = OUTPUT_DIR / file_name
        row_count = write_query_to_csv(conn, output_path, query)
        total_outputs += 1
        print(f"Generated {output_path.relative_to(ROOT)} ({row_count} rows)")

    conn.close()

    print(f"Validation complete. Reports generated: {total_outputs}")


if __name__ == "__main__":
    main()
