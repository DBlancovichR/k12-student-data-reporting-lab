# Ticket 001 - Duplicate Student Record

## Issue

Student ID `1007` appears twice in `students.csv`.

## Impact

Duplicate student records can inflate enrollment counts, create conflicting program records, and cause reporting extract errors.

## Investigation

Reviewed the student file and ran duplicate student record validation.

## SQL Used

`sql/02_duplicate_student_records.sql`

## Root Cause

Duplicate row exists with the same `student_id` and `state_student_id`.

## Resolution

Registrar or data owner should verify whether the duplicate is a true duplicate or a legitimate separate record. If duplicate, merge or remove the extra record.

## Prevention

Run duplicate record validation before generating reporting extracts.

## Status

Open
