-- Transcript credit discrepancy review
-- Purpose: Identify senior transcript records requiring manual review.

SELECT
    transcript_id,
    student_id,
    grade_level,
    credits_attempted,
    credits_earned,
    graduation_eligible,
    notes
FROM transcripts
WHERE credits_earned > credits_attempted
   OR (graduation_eligible = 'Yes' AND credits_earned < 220)
   OR notes LIKE '%review%'
   OR notes LIKE '%missing%';
