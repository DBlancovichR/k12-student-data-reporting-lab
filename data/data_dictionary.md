# Synthetic Data Dictionary

## Purpose

This document defines the synthetic data files used in the K-12 Student Data Reporting & Data Integrity Lab.

All records are fictional and created for demonstration purposes only.

## students.csv

| Field | Description |
|---|---|
| student_id | Local synthetic student identifier |
| state_student_id | Synthetic state-level student identifier |
| first_name | Fictional student first name |
| last_name | Fictional student last name |
| grade_level | Student grade level |
| enrollment_status | Active or inactive status |
| english_learner_status | English Learner status |
| special_education_status | Special Education status |
| section_504_status | Section 504 status |
| graduation_status | Senior graduation status when applicable |

## enrollments.csv

| Field | Description |
|---|---|
| enrollment_id | Synthetic enrollment record identifier |
| student_id | Student identifier |
| school_year | Academic year |
| entry_date | Enrollment entry date |
| exit_date | Withdrawal/exit date if inactive |
| exit_code | Exit or withdrawal code |
| grade_level | Grade level for enrollment record |
| enrollment_status | Active or inactive enrollment status |

## transcripts.csv

| Field | Description |
|---|---|
| transcript_id | Synthetic transcript identifier |
| student_id | Student identifier |
| school_year | Academic year |
| grade_level | Transcript grade level |
| credits_attempted | Credits attempted |
| credits_earned | Credits earned |
| gpa | Grade point average |
| graduation_eligible | Indicates if student is marked graduation eligible |
| notes | Review notes or exception comments |

## programs.csv

| Field | Description |
|---|---|
| program_record_id | Synthetic program record identifier |
| student_id | Student identifier |
| program_name | Program participation category |
| program_status | Active/inactive status |
| start_date | Program start date |
| end_date | Program end date when applicable |

## attendance.csv

| Field | Description |
|---|---|
| attendance_id | Synthetic attendance record identifier |
| student_id | Student identifier |
| school_year | Academic year |
| days_enrolled | Total enrolled days |
| days_present | Total present days |
| days_absent | Total absent days |
| attendance_rate | Attendance percentage |

## discipline.csv

| Field | Description |
|---|---|
| incident_id | Synthetic discipline incident identifier |
| student_id | Student identifier |
| school_year | Academic year |
| incident_date | Date of incident |
| incident_type | Discipline incident category |
| action_taken | Administrative action |
| days_removed | Number of school days removed |

## Intentional Data Quality Issues

| Issue | Example |
|---|---|
| Duplicate student record | Student ID 1007 appears twice |
| Missing exit code | Student ID 1006 has exit date but no exit code |
| Invalid grade level | Student ID 1016 has grade level 13 |
| Missing program status | Student ID 1012 has blank program status |
| Credit discrepancy | Student ID 1013 has credits earned greater than attempted |
| Graduation eligibility conflict | Student ID 1014 is marked eligible with insufficient credits |
| Missing senior graduation status | Student IDs 1005 and 1015 |
