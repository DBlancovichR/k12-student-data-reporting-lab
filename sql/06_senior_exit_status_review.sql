-- Senior exit status review
-- Purpose: Identify grade 12 students missing graduation status or requiring senior exit review.

SELECT
    s.student_id,
    s.first_name,
    s.last_name,
    s.grade_level,
    s.enrollment_status,
    s.graduation_status,
    t.credits_attempted,
    t.credits_earned,
    t.graduation_eligible,
    t.notes
FROM students s
LEFT JOIN transcripts t
    ON s.student_id = t.student_id
WHERE s.grade_level = 12
  AND (
        s.graduation_status IS NULL
        OR s.graduation_status = ''
        OR s.graduation_status = 'Behind Credits'
        OR t.credits_earned < 220
        OR t.credits_earned > t.credits_attempted
      )
ORDER BY s.student_id;
