#!/usr/bin/env python3
"""
Builds a SQLite database from the synthetic CSV files.

This script creates database/k12_student_reporting.db using the schema in
database/schema.sql and loads data from the data/ directory.
"""

import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "database" / "k12_student_reporting.db"
SCHEMA_PATH = ROOT / "database" / "schema.sql"
DATA_DIR = ROOT / "data"

TABLE_FILES = {
    "students": "students.csv",
    "enrollments": "enrollments.csv",
    "transcripts": "transcripts.csv",
    "programs": "programs.csv",
    "attendance": "attendance.csv",
    "discipline": "discipline.csv",
}


def clean_value(value: str):
    """Convert blank CSV fields to None for SQLite."""
    if value is None:
        return None
    value = value.strip()
    return value if value != "" else None


def load_csv(conn: sqlite3.Connection, table_name: str, csv_path: Path) -> int:
    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames

        if not columns:
            raise ValueError(f"No columns found in {csv_path}")

        placeholders = ", ".join(["?"] * len(columns))
        column_list = ", ".join(columns)

        insert_sql = f"INSERT INTO {table_name} ({column_list}) VALUES ({placeholders})"

        row_count = 0
        for row in reader:
            values = [clean_value(row[column]) for column in columns]
            conn.execute(insert_sql, values)
            row_count += 1

    return row_count


def main():
    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(f"Missing schema file: {SCHEMA_PATH}")

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    with SCHEMA_PATH.open("r", encoding="utf-8") as schema_file:
        conn.executescript(schema_file.read())

    total_rows = 0

    for table_name, file_name in TABLE_FILES.items():
        csv_path = DATA_DIR / file_name

        if not csv_path.exists():
            raise FileNotFoundError(f"Missing data file: {csv_path}")

        rows_loaded = load_csv(conn, table_name, csv_path)
        total_rows += rows_loaded
        print(f"Loaded {rows_loaded} rows into {table_name}")

    conn.commit()
    conn.close()

    print(f"Database created: {DB_PATH}")
    print(f"Total rows loaded: {total_rows}")


if __name__ == "__main__":
    main()
