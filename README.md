# K-12 Student Data Reporting & Data Integrity Lab

## Project Overview

This project simulates a K-12 student information system reporting workflow using synthetic student data. It demonstrates data validation, SQL reporting, reporting-extract review, documentation, and troubleshooting workflows commonly used in education data systems support roles.

The project focuses on student records, enrollment and withdrawal data, transcript review, program participation, attendance, discipline summaries, and reporting exceptions.

This project does not use real student data and is not connected to any real school system.

## Purpose

The purpose of this lab is to demonstrate practical competence in:

- Student information system data review
- Data integrity validation
- SQL-based reporting
- Enrollment and withdrawal discrepancy analysis
- Transcript and credit review
- Program participation reporting
- CALPADS-style, CBEDS-style, and CRDC-style reporting simulations
- Vendor import/export workflow documentation
- FERPA-aware data handling
- Staff-facing procedure documentation
- Data-system troubleshooting tickets

## Phase 1 Scope

This first phase is a lightweight, reviewable project built around CSV data, SQL query examples, reporting outputs, SOP documentation, and sample support tickets.

Later phases may expand this project into a database-backed lab using PostgreSQL or SQLite, Python validation scripts, dashboard reporting, and deeper student information system workflows.

## Project Structure

- `data/` - Synthetic student information system data
- `sql/` - SQL queries for reporting and data validation
- `reports/` - Sample reporting outputs
- `docs/` - SOPs, checklists, and workflow documentation
- `tickets/` - Sample support tickets for education data issues
- `screenshots/` - Placeholder for screenshots and future dashboard images

## Data Files

| File | Purpose |
|---|---|
| `students.csv` | Student demographic and enrollment status data |
| `enrollments.csv` | Entry dates, exit dates, grade level, school year, and exit codes |
| `transcripts.csv` | Course credits, GPA, and graduation-status review |
| `programs.csv` | Program participation such as English Learner, Special Education, and 504 |
| `attendance.csv` | Attendance summary data by student |
| `discipline.csv` | Discipline incidents for CRDC-style summary reporting |

## Reporting Simulations

This project includes simplified reporting simulations for:

- Enrollment by grade
- Missing exit codes
- Duplicate student records
- Transcript credit discrepancies
- Senior exit status review
- Program participation counts
- Attendance summaries
- CRDC-style discipline summary
- Data quality exception reporting

These reports are simulations only and are not official state or federal reporting submissions.

## Key Skills Demonstrated

- SQL querying
- Data validation
- Data discrepancy review
- CSV import/export awareness
- Student record review
- Reporting-extract preparation
- Documentation and SOP creation
- Education data privacy awareness
- Troubleshooting and ticket documentation
- Cross-functional support for staff and vendors

## Sample Findings

The synthetic dataset intentionally includes common data-quality issues:

- Duplicate student record
- Inactive student missing exit code
- Invalid grade level
- Missing senior graduation status
- Program participation record missing status
- Transcript credit mismatch
- Student marked graduation eligible despite insufficient credits

## Notes

All data in this repository is synthetic and created for demonstration purposes only.

## Additional Documentation

- `data/data_dictionary.md` explains each synthetic data file and field.
- `docs/job_alignment_matrix.md` maps project deliverables to education data systems responsibilities.
