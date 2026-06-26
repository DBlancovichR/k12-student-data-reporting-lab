# Validation Summary

## Overview

This report summarizes the generated data validation results for the K-12 Student Data Reporting & Data Integrity Lab.

The validation workflow reviews synthetic student information system data for common reporting issues before reports or extracts are finalized.

## Summary

| Metric | Result |
|---|---|
| Total validation categories | 5 |
| Total detected exceptions | 6 |
| Duplicate student records | 1 |
| Missing exit code records | 1 |
| Invalid grade level records | 1 |
| Program records missing status | 1 |
| Senior records requiring review | 4 |

## Data Quality Scorecard

| check_name | exception_count |
| --- | --- |
| Duplicate student records | 1 |
| Inactive enrollments missing exit codes | 1 |
| Invalid grade levels | 1 |
| Program records missing status | 1 |
| Seniors missing graduation status | 2 |


## Duplicate Student Records

| student_id | state_student_id | record_count |
| --- | --- | --- |
| 1007 | CA0001007 | 2 |


## Missing Exit Codes

| enrollment_id | student_id | school_year | entry_date | exit_date | exit_code | grade_level | enrollment_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E006 | 1006 | 2025-2026 | 2025-08-12 | 2025-11-03 |  | 9 | Inactive |


## Invalid Grade Levels

| enrollment_id | student_id | school_year | grade_level | enrollment_status |
| --- | --- | --- | --- | --- |
| E016 | 1016 | 2025-2026 | 13 | Active |


## Program Records Missing Status

| program_record_id | student_id | program_name | program_status | start_date | end_date |
| --- | --- | --- | --- | --- | --- |
| P007 | 1012 | English Learner |  | 2025-08-12 |  |


## Senior Exit Status Review

| student_id | first_name | last_name | grade_level | enrollment_status | graduation_status | credits_attempted | credits_earned | graduation_eligible | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1005 | Isabella | Nguyen | 12 | Active |  | 230 | 218 | No | Missing graduation status in student record |
| 1013 | Ava | Thomas | 12 | Active | On Track | 230 | 232 | Yes | Credit total requires review |
| 1014 | William | Moore | 12 | Active | Behind Credits | 230 | 190 | Yes | Marked eligible despite insufficient credits |
| 1015 | Mia | Taylor | 12 | Active |  | 230 | 226 | Yes | Graduation status missing |


## CRDC-Style Discipline Summary

| action_taken | incident_count | total_days_removed |
| --- | --- | --- |
| In-School Suspension | 2 | 2 |
| Conference | 1 | 0 |
| Detention | 1 | 0 |
| Out-of-School Suspension | 1 | 3 |


## Review Notes

These results are based on synthetic data and are intended to demonstrate data validation, reporting review, issue documentation, and education data workflow understanding.
