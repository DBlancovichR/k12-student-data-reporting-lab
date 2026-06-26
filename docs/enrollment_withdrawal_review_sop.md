# Enrollment and Withdrawal Review SOP

## Purpose

This SOP defines the process for reviewing enrollment and withdrawal records before reporting.

## Review Criteria

Enrollment records should include:

- Student ID
- School year
- Entry date
- Grade level
- Enrollment status

Inactive enrollment records should also include:

- Exit date
- Exit code
- Correct withdrawal reason

## Procedure

1. Open the enrollment source file.
2. Filter for inactive records.
3. Identify records with exit dates but missing exit codes.
4. Identify students with active status but invalid grade levels.
5. Cross-check student IDs against the student file.
6. Document exceptions in the data quality exception report.
7. Assign corrections to the appropriate records owner.
8. Re-run the validation query after corrections.

## SQL Reference

Use:

- `sql/01_current_enrollment_by_grade.sql`
- `sql/03_missing_exit_codes.sql`
- `sql/09_reporting_exception_report.sql`

## Expected Outcome

All inactive students with exit dates should have valid exit codes before reporting extracts are finalized.
