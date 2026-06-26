-- Missing exit code review
-- Purpose: Identify inactive enrollments with exit dates but missing exit codes.

SELECT
    enrollment_id,
    student_id,
    school_year,
    entry_date,
    exit_date,
    exit_code,
    grade_level,
    enrollment_status
FROM enrollments
WHERE enrollment_status = 'Inactive'
  AND exit_date IS NOT NULL
  AND (exit_code IS NULL OR exit_code = '');
