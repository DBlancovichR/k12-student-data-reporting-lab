#!/usr/bin/env python3
"""
Generates a reviewer-friendly Markdown validation summary from generated CSV reports.
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports" / "generated"
OUTPUT_FILE = REPORT_DIR / "validation_summary.md"


def read_csv_rows(file_name):
    path = REPORT_DIR / file_name
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def markdown_table(rows):
    if not rows:
        return "_No records found._\n"

    headers = list(rows[0].keys())
    lines = []

    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for row in rows:
        lines.append("| " + " | ".join(str(row.get(header, "")) for header in headers) + " |")

    return "\n".join(lines) + "\n"


def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    scorecard = read_csv_rows("data_quality_scorecard.csv")
    duplicates = read_csv_rows("duplicate_student_records.csv")
    missing_exit_codes = read_csv_rows("missing_exit_codes.csv")
    invalid_grades = read_csv_rows("invalid_grade_levels.csv")
    missing_program_status = read_csv_rows("program_records_missing_status.csv")
    senior_review = read_csv_rows("senior_exit_status_review.csv")
    discipline_summary = read_csv_rows("crdc_style_discipline_summary.csv")

    total_exceptions = 0
    for row in scorecard:
        try:
            total_exceptions += int(row.get("exception_count", 0))
        except ValueError:
            pass

    content = f"""# Validation Summary

## Overview

This report summarizes the generated data validation results for the K-12 Student Data Reporting & Data Integrity Lab.

The validation workflow reviews synthetic student information system data for common reporting issues before reports or extracts are finalized.

## Summary

| Metric | Result |
|---|---|
| Total validation categories | {len(scorecard)} |
| Total detected exceptions | {total_exceptions} |
| Duplicate student records | {len(duplicates)} |
| Missing exit code records | {len(missing_exit_codes)} |
| Invalid grade level records | {len(invalid_grades)} |
| Program records missing status | {len(missing_program_status)} |
| Senior records requiring review | {len(senior_review)} |

## Data Quality Scorecard

{markdown_table(scorecard)}

## Duplicate Student Records

{markdown_table(duplicates)}

## Missing Exit Codes

{markdown_table(missing_exit_codes)}

## Invalid Grade Levels

{markdown_table(invalid_grades)}

## Program Records Missing Status

{markdown_table(missing_program_status)}

## Senior Exit Status Review

{markdown_table(senior_review)}

## CRDC-Style Discipline Summary

{markdown_table(discipline_summary)}

## Review Notes

These results are based on synthetic data and are intended to demonstrate data validation, reporting review, issue documentation, and education data workflow understanding.
"""

    OUTPUT_FILE.write_text(content, encoding="utf-8")
    print(f"Generated {OUTPUT_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
