#!/usr/bin/env python3
"""
Generates a correction action plan from generated validation reports.

The output maps each detected data issue to a recommended owner, correction step,
and prevention control.
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports" / "generated"
CSV_OUTPUT = REPORT_DIR / "correction_action_plan.csv"
MD_OUTPUT = REPORT_DIR / "correction_action_plan.md"


def read_csv(file_name):
    path = REPORT_DIR / file_name
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def add_action(actions, issue_type, student_id, source, issue, owner, correction, prevention, priority):
    actions.append({
        "issue_type": issue_type,
        "student_id": student_id,
        "source": source,
        "issue": issue,
        "recommended_owner": owner,
        "correction_step": correction,
        "prevention_control": prevention,
        "priority": priority
    })


def markdown_table(rows):
    if not rows:
        return "_No correction actions required._\n"

    headers = rows[0].keys()
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for row in rows:
        lines.append("| " + " | ".join(str(row[h]) for h in headers) + " |")

    return "\n".join(lines) + "\n"


def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    actions = []

    for row in read_csv("duplicate_student_records.csv"):
        add_action(
            actions,
            "Duplicate Student Record",
            row.get("student_id", ""),
            "students.csv",
            "Duplicate student_id/state_student_id found",
            "Registrar / Data Specialist",
            "Review duplicate record, confirm correct student master record, and merge or remove duplicate.",
            "Run duplicate student validation before reporting extracts.",
            "High"
        )

    for row in read_csv("missing_exit_codes.csv"):
        add_action(
            actions,
            "Missing Exit Code",
            row.get("student_id", ""),
            "enrollments.csv",
            "Inactive enrollment has exit date but missing exit code",
            "Registrar",
            "Confirm withdrawal reason and enter valid exit code.",
            "Require exit code completion during withdrawal processing.",
            "High"
        )

    for row in read_csv("invalid_grade_levels.csv"):
        add_action(
            actions,
            "Invalid Grade Level",
            row.get("student_id", ""),
            "enrollments.csv",
            "Grade level is outside expected high school range",
            "Registrar / Data Specialist",
            "Verify grade placement and correct enrollment record.",
            "Validate grade level values before extract generation.",
            "High"
        )

    for row in read_csv("program_records_missing_status.csv"):
        add_action(
            actions,
            "Missing Program Status",
            row.get("student_id", ""),
            "programs.csv",
            "Program participation record is missing status",
            "Program Coordinator",
            "Confirm program participation status and update record.",
            "Reject program records with blank status before vendor export.",
            "Medium"
        )

    for row in read_csv("senior_exit_status_review.csv"):
        add_action(
            actions,
            "Senior Exit Status Review",
            row.get("student_id", ""),
            "students.csv / transcripts.csv",
            "Senior record has missing or inconsistent graduation/credit status",
            "Counseling / Registrar",
            "Review transcript, confirm graduation status, and update senior exit record.",
            "Run senior exit validation before graduation reporting deadlines.",
            "High"
        )

    for row in read_csv("referential_integrity_exceptions.csv"):
        add_action(
            actions,
            "Referential Integrity Exception",
            row.get("student_id", ""),
            row.get("source_file", ""),
            "Child record does not match a student master record",
            "Data Specialist / SIS Administrator",
            "Create or correct the student master record, or remove invalid child record.",
            "Validate student IDs across source files before imports and extracts.",
            "High"
        )

    with CSV_OUTPUT.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "issue_type",
            "student_id",
            "source",
            "issue",
            "recommended_owner",
            "correction_step",
            "prevention_control",
            "priority"
        ])
        writer.writeheader()
        writer.writerows(actions)

    md_content = f"""# Correction Action Plan

## Overview

This report translates detected validation issues into practical correction actions.

It is designed to simulate how a data specialist or systems information specialist would document ownership, correction steps, and prevention controls before final reporting.

## Correction Actions

{markdown_table(actions)}

## Notes

All records are synthetic. This report demonstrates issue documentation, ownership assignment, correction planning, and prevention controls for education data workflows.
"""

    MD_OUTPUT.write_text(md_content, encoding="utf-8")

    print(f"Generated {CSV_OUTPUT.relative_to(ROOT)} ({len(actions)} rows)")
    print(f"Generated {MD_OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
