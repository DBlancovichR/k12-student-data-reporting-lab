#!/usr/bin/env python3
"""
Applies sample corrections to the SQLite database.

This simulates how a data specialist would resolve reporting exceptions after
reviewing the correction action plan. The original CSV source data is preserved.
Corrections are applied only to the generated SQLite database.
"""

import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "database" / "k12_student_reporting.db"


def main():
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not found: {DB_PATH}. Run scripts/build_database.py first."
        )

    conn = sqlite3.connect(DB_PATH)

    # 1. Remove duplicate student master record for student_id 1007.
    conn.execute("""
        DELETE FROM students
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM students
            GROUP BY student_id, state_student_id
        );
    """)

    # 2. Add missing exit code for inactive student 1006.
    conn.execute("""
        UPDATE enrollments
        SET exit_code = 'T160'
        WHERE student_id = 1006
          AND enrollment_status = 'Inactive'
          AND exit_date IS NOT NULL
          AND (exit_code IS NULL OR exit_code = '');
    """)

    # 3. Correct invalid grade level for student 1016.
    conn.execute("""
        UPDATE enrollments
        SET grade_level = 12
        WHERE student_id = 1016
          AND grade_level = 13;
    """)

    # 4. Add missing program status for student 1012.
    conn.execute("""
        UPDATE programs
        SET program_status = 'Active'
        WHERE student_id = 1012
          AND (program_status IS NULL OR program_status = '');
    """)

    # 5. Add missing senior graduation statuses.
    conn.execute("""
        UPDATE students
        SET graduation_status = 'Pending Review'
        WHERE student_id IN (1005, 1015)
          AND grade_level = 12
          AND (graduation_status IS NULL OR graduation_status = '');
    """)

    # 6. Add missing student master record for enrollment-only student 1016.
    conn.execute("""
        INSERT INTO students (
            student_id,
            state_student_id,
            first_name,
            last_name,
            grade_level,
            enrollment_status,
            english_learner_status,
            special_education_status,
            section_504_status,
            graduation_status
        )
        SELECT
            1016,
            'CA0001016',
            'Review',
            'Pending',
            12,
            'Active',
            'No',
            'No',
            'No',
            'Pending Review'
        WHERE NOT EXISTS (
            SELECT 1 FROM students WHERE student_id = 1016
        );
    """)

    conn.commit()
    conn.close()

    print("Sample corrections applied to SQLite database.")
    print("Original CSV files were not modified.")


if __name__ == "__main__":
    main()
