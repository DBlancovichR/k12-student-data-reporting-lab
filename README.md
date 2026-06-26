# K-12 Student Data Reporting & Data Integrity Lab

## Overview

This project simulates a K-12 student information system reporting workflow using synthetic student data. It demonstrates how student records can be validated, queried, documented, and reviewed before reporting extracts are prepared.

The lab focuses on data integrity issues commonly found in education data systems, including duplicate student records, missing exit codes, invalid grade levels, incomplete program participation records, transcript discrepancies, senior exit status gaps, and discipline reporting summaries.

All data is synthetic. No real student data is used.

## Purpose

This project was built to demonstrate practical skills relevant to education data systems and systems information roles, including:

- Student information system data review
- SQL-based reporting and validation
- Enrollment and withdrawal discrepancy analysis
- Transcript and senior exit review
- Program participation reporting
- Attendance and discipline summary reporting
- CALPADS-style, CBEDS-style, and CRDC-style reporting simulations
- Data quality exception reporting
- Vendor import/export documentation
- FERPA-aware data handling
- Staff-facing SOPs and troubleshooting tickets

## Technical Stack

- Python 3
- SQLite
- SQL
- CSV
- Markdown documentation
- Git/GitHub

## Project Structure

```text
k12-student-data-reporting-lab/
├── data/                 # Synthetic source data
├── database/             # SQLite schema and generated database
├── scripts/              # Python build and validation scripts
├── sql/                  # Standalone SQL reporting queries
├── reports/              # Static and generated report outputs
├── docs/                 # SOPs, data dictionary, alignment matrix
├── tickets/              # Sample support tickets
└── screenshots/          # Future screenshots and dashboard images
```

## Synthetic Data Files

| File | Purpose |
|---|---|
| `data/students.csv` | Student demographic, grade, program flag, and graduation status data |
| `data/enrollments.csv` | Entry dates, exit dates, exit codes, grade level, and enrollment status |
| `data/transcripts.csv` | Senior credit totals, GPA, graduation eligibility, and transcript notes |
| `data/programs.csv` | English Learner, Special Education, and Section 504 program participation |
| `data/attendance.csv` | Attendance totals and attendance rates |
| `data/discipline.csv` | Discipline incidents, actions taken, and days removed |

## Executable Workflow

### 1. Build the SQLite database

```bash
python3 scripts/build_database.py
```

This creates:

```text
database/k12_student_reporting.db
```

### 2. Run validation reports

```bash
python3 scripts/run_validation.py
```

This generates CSV outputs in:

```text
reports/generated/
```

## Generated Reports

| Report | Purpose |
|---|---|
| `duplicate_student_records.csv` | Identifies duplicate student IDs |
| `missing_exit_codes.csv` | Finds inactive enrollments missing exit codes |
| `invalid_grade_levels.csv` | Finds grade levels outside the expected high school range |
| `program_records_missing_status.csv` | Finds incomplete program participation records |
| `senior_exit_status_review.csv` | Reviews grade 12 graduation status and transcript issues |
| `referential_integrity_exceptions.csv` | Finds records that do not match a student master record |
| `data_quality_scorecard.csv` | Summarizes exception counts |
| `enrollment_by_grade.csv` | Summarizes active enrollment by grade |
| `crdc_style_discipline_summary.csv` | Summarizes discipline actions and removal days |
| `validation_summary.md` | Provides a reviewer-friendly Markdown summary of validation results |

## Reporting Extracts

| Extract | Purpose |
|---|---|
| `calpads_style_enrollment_extract.csv` | Simulates an enrollment reporting extract |
| `calpads_style_program_participation_extract.csv` | Simulates a program participation reporting extract |
| `cbeds_style_school_summary.csv` | Simulates a school-level enrollment summary |
| `crdc_style_discipline_extract.csv` | Simulates a discipline reporting extract |
| `senior_exit_extract.csv` | Simulates a senior exit and graduation-status extract |

## Sample Data Quality Findings

| Finding | Example |
|---|---|
| Duplicate student record | Student ID `1007` appears twice |
| Missing exit code | Student ID `1006` has an exit date but no exit code |
| Invalid grade level | Student ID `1016` has grade level `13` |
| Missing program status | Student ID `1012` has a blank program status |
| Transcript credit discrepancy | Student ID `1013` has credits earned greater than attempted |
| Graduation eligibility conflict | Student ID `1014` is marked eligible despite insufficient credits |
| Missing senior graduation status | Student IDs `1005` and `1015` |

## Example Scorecard Output

```text
check_name,exception_count
Duplicate student records,1
Inactive enrollments missing exit codes,1
Invalid grade levels,1
Program records missing status,1
Seniors missing graduation status,2
```

## Documentation Included

| Document | Purpose |
|---|---|
| `data/data_dictionary.md` | Defines all synthetic data fields |
| `docs/job_alignment_matrix.md` | Maps project deliverables to education data systems responsibilities |
| `docs/data_validation_workflow.md` | Documents the validation process |
| `docs/enrollment_withdrawal_review_sop.md` | Reviews enrollment and withdrawal data handling |
| `docs/reporting_deadline_checklist.md` | Provides a reporting preparation checklist |
| `docs/vendor_import_export_sop.md` | Documents import/export workflow controls |
| `docs/ferpa_aware_data_handling.md` | Describes privacy-aware student data handling |
| `docs/staff_training_guide.md` | Provides staff-facing correction workflow guidance |

## Sample Support Tickets

The `tickets/` folder includes realistic issue documentation for:

- Duplicate student record
- Missing exit code
- Transcript credit mismatch
- Vendor import error
- Senior exit status review

Each ticket includes issue, impact, investigation, SQL used, root cause, resolution, prevention, and status.

## Key Skills Demonstrated

- SQL reporting
- SQLite database creation
- Python scripting
- CSV import/export workflow
- Data validation
- Reporting exception analysis
- Student record review
- Procedure documentation
- Support ticket documentation
- Education data privacy awareness
- Stakeholder and vendor support workflow

## Future Enhancements

Planned improvements include:

- PostgreSQL version
- Larger synthetic dataset
- Python-generated dashboards
- Expanded automated data quality scoring
- More detailed CALPADS-style extract simulations
- Import/export error logging
- Screenshots of report outputs and workflow execution

## Optional Makefile Commands

The project can also be run with Make:

| Command | Purpose |
|---|---|
| `make build` | Builds the SQLite database |
| `make validate` | Runs validation reports |
| `make extracts` | Generates CALPADS-style, CBEDS-style, CRDC-style, and senior exit extracts |
| `make summary` | Generates the Markdown validation summary |
| `make corrections` | Generates the correction action plan |
| `make apply-corrections` | Applies sample corrections and regenerates reports |
| `make reset` | Rebuilds the database and regenerates all reports/extracts |
| `make clean` | Removes generated database and report files |

## Correction Action Plan

The project also generates correction planning outputs:

| Output | Purpose |
|---|---|
| `reports/generated/correction_action_plan.csv` | Maps each validation issue to an owner, correction step, prevention control, and priority |
| `reports/generated/correction_action_plan.md` | Provides a reviewer-friendly correction action plan in Markdown |

This simulates the workflow of detecting reporting issues, assigning ownership, documenting corrective action, and preventing recurrence.
