# Ticket 005 - Senior Exit Status Review

## Issue

Senior students `1005` and `1015` are missing graduation status. Student `1014` is marked graduation eligible despite insufficient credits.

## Impact

Senior exit status errors can affect graduation, certificate, and completion reporting.

## Investigation

Reviewed grade 12 students, transcript credits, and graduation eligibility.

## SQL Used

`sql/06_senior_exit_status_review.sql`

## Root Cause

Graduation status was not updated for some seniors. One senior record has conflicting eligibility and credit data.

## Resolution

Counseling and registrar staff should review senior transcripts and update graduation status.

## Prevention

Run senior exit status report before graduation certification and state reporting deadlines.

## Status

Open
