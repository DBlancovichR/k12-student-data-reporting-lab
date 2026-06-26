# Job Alignment Matrix

## Purpose

This document maps the project deliverables to education data systems responsibilities such as student information system support, data validation, reporting extracts, documentation, and troubleshooting.

## Alignment Summary

| Job Responsibility | Project Evidence |
|---|---|
| Manage and maintain data used for reporting | Synthetic SIS-style files in `data/` covering students, enrollments, transcripts, programs, attendance, and discipline |
| Analyze data discrepancies | `reports/data_quality_exception_report.csv` identifies duplicate records, missing exit codes, invalid grade levels, missing program status, and transcript issues |
| Create user-defined reports | SQL query files in `sql/` generate enrollment, program, attendance, discipline, senior status, and exception reports |
| Design query statements | Ten SQL files demonstrate targeted reporting and validation queries |
| Maintain student records | Student, enrollment, transcript, and program files simulate core student record workflows |
| Support enrollment and withdrawal reporting | `docs/enrollment_withdrawal_review_sop.md` and `sql/03_missing_exit_codes.sql` |
| Support senior exit review | `reports/senior_exit_status_report.csv` and `tickets/005-senior-exit-status-review.md` |
| Export/import data for third-party systems | `docs/vendor_import_export_sop.md` |
| Document procedures and data standards | SOPs and workflow guides in `docs/` |
| Train/support staff | `docs/staff_training_guide.md` |
| Troubleshoot reporting issues | Sample issue tickets in `tickets/` |
| Protect student information | `docs/ferpa_aware_data_handling.md` |
| Prepare CALPADS/CBEDS/CRDC-style reporting simulations | Enrollment, program, senior status, and discipline reports in `reports/` |

## Positioning Statement

This project demonstrates the ability to support student data systems through data validation, reporting review, issue documentation, procedure writing, and stakeholder support. It is designed as a practical bridge between IT systems support experience and education data reporting responsibilities.
