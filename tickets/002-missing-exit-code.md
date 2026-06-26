# Ticket 002 - Missing Exit Code

## Issue

Student ID `1006` has an inactive enrollment with an exit date but no exit code.

## Impact

Missing exit codes can affect withdrawal, dropout, and enrollment reporting accuracy.

## Investigation

Filtered inactive enrollments and reviewed records where `exit_date` is populated but `exit_code` is blank.

## SQL Used

`sql/03_missing_exit_codes.sql`

## Root Cause

Exit date was entered, but the withdrawal code was not completed.

## Resolution

Registrar should confirm the withdrawal reason and enter the appropriate exit code.

## Prevention

Require exit code completion during withdrawal processing.

## Status

Open
