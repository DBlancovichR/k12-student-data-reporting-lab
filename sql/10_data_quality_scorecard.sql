-- Data quality scorecard
-- Purpose: Summarize exception counts for reporting readiness review.

SELECT 'Duplicate student records' AS check_name, COUNT(*) AS exception_count
FROM (
    SELECT student_id
    FROM students
    GROUP BY student_id, state_student_id
    HAVING COUNT(*) > 1
) x

UNION ALL

SELECT 'Inactive enrollments missing exit codes' AS check_name, COUNT(*) AS exception_count
FROM enrollments
WHERE enrollment_status = 'Inactive'
  AND exit_date IS NOT NULL
  AND (exit_code IS NULL OR exit_code = '')

UNION ALL

SELECT 'Invalid grade levels' AS check_name, COUNT(*) AS exception_count
FROM enrollments
WHERE grade_level NOT BETWEEN 9 AND 12

UNION ALL

SELECT 'Program records missing status' AS check_name, COUNT(*) AS exception_count
FROM programs
WHERE program_status IS NULL OR program_status = ''

UNION ALL

SELECT 'Seniors missing graduation status' AS check_name, COUNT(*) AS exception_count
FROM students
WHERE grade_level = 12
  AND (graduation_status IS NULL OR graduation_status = '');
