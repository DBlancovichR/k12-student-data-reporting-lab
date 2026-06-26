# Data Validation Workflow

## Purpose

This workflow documents how student data should be reviewed before reporting extracts are generated or submitted.

## Scope

The workflow applies to student, enrollment, withdrawal, transcript, program participation, attendance, and discipline data.

## Validation Steps

1. Confirm required source files are present.
2. Review student identifiers for duplicates.
3. Verify active and inactive enrollment status.
4. Confirm inactive students with exit dates have valid exit codes.
5. Check grade levels for expected values.
6. Review senior students for graduation status.
7. Validate transcript credits and graduation eligibility.
8. Review program participation records for missing statuses.
9. Review attendance and discipline summaries for reporting exceptions.
10. Generate a data quality exception report.
11. Assign each exception to an owner.
12. Document correction steps before final reporting.

## Common Exceptions

| Exception | Risk | Resolution |
|---|---|---|
| Duplicate student record | Inflated counts or incorrect reporting | Merge or correct duplicate SIS record |
| Missing exit code | Inaccurate withdrawal/dropout reporting | Confirm exit reason and update code |
| Missing graduation status | Senior exit reporting error | Review transcript and update status |
| Program status missing | Program participation reporting error | Confirm active/inactive status |
| Credit mismatch | Graduation eligibility error | Review transcript and credit totals |

## Output

The main output is `reports/data_quality_exception_report.csv`.
