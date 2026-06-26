# Interview Walkthrough

## 30-Second Project Summary

I built a K-12 student data reporting and data integrity lab using synthetic student information system data. The project uses CSV source files, a SQLite database, SQL validation queries, Python scripts, generated reports, SOPs, and sample troubleshooting tickets to simulate how education data can be reviewed before reporting.

The goal was to demonstrate my ability to support student data systems, validate records, investigate discrepancies, document procedures, and troubleshoot reporting issues.

## Why I Built It

The Systems Information Specialist role requires strong data accuracy, reporting, documentation, and troubleshooting skills. Since my professional background is strongest in IT support and systems support, I built this project to demonstrate hands-on competence with student-data-style workflows, reporting extracts, SQL queries, and data quality review.

## How the Workflow Works

1. Synthetic CSV files represent SIS-style records.
2. `scripts/build_database.py` loads the CSV files into SQLite.
3. `scripts/run_validation.py` runs validation queries.
4. Generated reports are saved to `reports/generated/`.
5. SOPs and tickets document how issues would be reviewed and resolved.

## Main Data Issues Detected

| Issue | Example |
|---|---|
| Duplicate record | Student ID 1007 appears twice |
| Missing exit code | Student ID 1006 is inactive but missing an exit code |
| Invalid grade level | Student ID 1016 has grade level 13 |
| Missing program status | Student ID 1012 has no program status |
| Senior status issue | Student IDs 1005 and 1015 are missing graduation status |
| Transcript conflict | Student ID 1014 is graduation eligible despite insufficient credits |

## SQL and Reporting Examples

The project includes SQL queries for:

- Enrollment by grade
- Duplicate student records
- Missing exit codes
- Transcript discrepancies
- Program participation counts
- Senior exit review
- Attendance summary
- Discipline summary
- Data quality exception reporting
- Data quality scorecard

## Documentation Examples

The project includes:

- Data dictionary
- Job alignment matrix
- Data validation workflow
- Enrollment and withdrawal SOP
- Reporting deadline checklist
- Vendor import/export SOP
- FERPA-aware data handling guide
- Staff training guide

## How This Connects to My Experience

My work experience includes IT systems support, user troubleshooting, Microsoft 365 support, Active Directory support, ServiceNow ticketing, documentation, SQL, Excel, and escalation workflows.

This project adds a focused education-data layer: student records, reporting extracts, data validation, senior exit review, and education data documentation.

## Honest Scope

This is a simulated project using synthetic data. It does not claim direct access to real CALPADS, CBEDS, CRDC, SEIS, or live student information systems. It demonstrates that I understand the workflow concepts and can build tools to validate, document, and troubleshoot education data processes.
