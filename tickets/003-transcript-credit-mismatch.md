# Ticket 003 - Transcript Credit Mismatch

## Issue

Student ID `1013` shows credits earned greater than credits attempted.

## Impact

Transcript credit discrepancies can affect graduation eligibility and senior exit reporting.

## Investigation

Reviewed senior transcript records for credit inconsistencies.

## SQL Used

`sql/04_transcript_credit_discrepancies.sql`

## Root Cause

Credit total appears inconsistent and requires transcript review.

## Resolution

Counseling or registrar staff should review the transcript, verify course credits, and correct the total if needed.

## Prevention

Run senior transcript validation before graduation reporting.

## Status

Open
