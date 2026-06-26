-- Current enrollment by grade level
-- Purpose: Support enrollment count review for school reporting.

SELECT
    grade_level,
    COUNT(DISTINCT student_id) AS active_student_count
FROM enrollments
WHERE enrollment_status = 'Active'
  AND grade_level BETWEEN 9 AND 12
GROUP BY grade_level
ORDER BY grade_level;
