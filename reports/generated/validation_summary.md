# Validation Summary

## Overview

This report summarizes the generated data validation results for the K-12 Student Data Reporting & Data Integrity Lab.

The validation workflow reviews synthetic student information system data for common reporting issues before reports or extracts are finalized.

## Summary

| Metric | Result |
|---|---|
| Total validation categories | 5 |
| Total detected exceptions | 0 |
| Duplicate student records | 0 |
| Missing exit code records | 0 |
| Invalid grade level records | 0 |
| Program records missing status | 0 |
| Senior records requiring review | 3 |
| Referential integrity exceptions | 0 |

## Data Quality Scorecard

| check_name | exception_count |
| --- | --- |
| Duplicate student records | 0 |
| Inactive enrollments missing exit codes | 0 |
| Invalid grade levels | 0 |
| Program records missing status | 0 |
| Seniors missing graduation status | 0 |


## Duplicate Student Records

_No records found._


## Missing Exit Codes

_No records found._


## Invalid Grade Levels

_No records found._


## Program Records Missing Status

_No records found._


## Senior Exit Status Review

| student_id | first_name | last_name | grade_level | enrollment_status | graduation_status | credits_attempted | credits_earned | graduation_eligible | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1005 | Isabella | Nguyen | 12 | Active | Pending Review | 230 | 218 | No | Missing graduation status in student record |
| 1013 | Ava | Thomas | 12 | Active | On Track | 230 | 232 | Yes | Credit total requires review |
| 1014 | William | Moore | 12 | Active | Behind Credits | 230 | 190 | Yes | Marked eligible despite insufficient credits |


## Referential Integrity Exceptions

_No records found._


## CRDC-Style Discipline Summary

| action_taken | incident_count | total_days_removed |
| --- | --- | --- |
| In-School Suspension | 2 | 2 |
| Conference | 1 | 0 |
| Detention | 1 | 0 |
| Out-of-School Suspension | 1 | 3 |


## Review Notes

These results are based on synthetic data and are intended to demonstrate data validation, reporting review, issue documentation, and education data workflow understanding.
