# Correction Action Plan

## Overview

This report translates detected validation issues into practical correction actions.

It is designed to simulate how a data specialist or systems information specialist would document ownership, correction steps, and prevention controls before final reporting.

## Correction Actions

| issue_type | student_id | source | issue | recommended_owner | correction_step | prevention_control | priority |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Duplicate Student Record | 1007 | students.csv | Duplicate student_id/state_student_id found | Registrar / Data Specialist | Review duplicate record, confirm correct student master record, and merge or remove duplicate. | Run duplicate student validation before reporting extracts. | High |
| Missing Exit Code | 1006 | enrollments.csv | Inactive enrollment has exit date but missing exit code | Registrar | Confirm withdrawal reason and enter valid exit code. | Require exit code completion during withdrawal processing. | High |
| Invalid Grade Level | 1016 | enrollments.csv | Grade level is outside expected high school range | Registrar / Data Specialist | Verify grade placement and correct enrollment record. | Validate grade level values before extract generation. | High |
| Missing Program Status | 1012 | programs.csv | Program participation record is missing status | Program Coordinator | Confirm program participation status and update record. | Reject program records with blank status before vendor export. | Medium |
| Senior Exit Status Review | 1005 | students.csv / transcripts.csv | Senior record has missing or inconsistent graduation/credit status | Counseling / Registrar | Review transcript, confirm graduation status, and update senior exit record. | Run senior exit validation before graduation reporting deadlines. | High |
| Senior Exit Status Review | 1013 | students.csv / transcripts.csv | Senior record has missing or inconsistent graduation/credit status | Counseling / Registrar | Review transcript, confirm graduation status, and update senior exit record. | Run senior exit validation before graduation reporting deadlines. | High |
| Senior Exit Status Review | 1014 | students.csv / transcripts.csv | Senior record has missing or inconsistent graduation/credit status | Counseling / Registrar | Review transcript, confirm graduation status, and update senior exit record. | Run senior exit validation before graduation reporting deadlines. | High |
| Senior Exit Status Review | 1015 | students.csv / transcripts.csv | Senior record has missing or inconsistent graduation/credit status | Counseling / Registrar | Review transcript, confirm graduation status, and update senior exit record. | Run senior exit validation before graduation reporting deadlines. | High |
| Referential Integrity Exception | 1016 | enrollments.csv | Child record does not match a student master record | Data Specialist / SIS Administrator | Create or correct the student master record, or remove invalid child record. | Validate student IDs across source files before imports and extracts. | High |


## Notes

All records are synthetic. This report demonstrates issue documentation, ownership assignment, correction planning, and prevention controls for education data workflows.
