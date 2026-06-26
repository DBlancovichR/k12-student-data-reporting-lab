-- Data quality exception report
-- Purpose: Combine common reporting exceptions into one review list.

SELECT
    'Duplicate Student Record' AS exception_type,
    CAST(student_id AS TEXT) AS student_id,
    'Duplicate student_id/state_student_id found in student file' AS issue
FROM students
GROUP BY student_id, state_student_id
HAVING COUNT(*) > 1

UNION ALL

SELECT
    'Missing Exit Code' AS exception_type,
    CAST(student_id AS TEXT) AS student_id,
    'Inactive enrollment has exit date but missing exit code' AS issue
FROM enrollments
WHERE enrollment_status = 'Inactive'
  AND exit_date IS NOT NULL
  AND (exit_code IS NULL OR exit_code = '')

UNION ALL

SELECT
    'Invalid Grade Level' AS exception_type,
    CAST(student_id AS TEXT) AS student_id,
    'Enrollment grade level is outside expected 9-12 range' AS issue
FROM enrollments
WHERE grade_level NOT BETWEEN 9 AND 12

UNION ALL

SELECT
    'Missing Program Status' AS exception_type,
    CAST(student_id AS TEXT) AS student_id,
    'Program participation record is missing program_status' AS issue
FROM programs
WHERE program_status IS NULL OR program_status = ''

UNION ALL

SELECT
    'Senior Graduation Status Review' AS exception_type,
    CAST(student_id AS TEXT) AS student_id,
    'Grade 12 student has missing or inconsistent graduation status' AS issue
FROM students
WHERE grade_level = 12
  AND (graduation_status IS NULL OR graduation_status = '');
