-- Duplicate student record review
-- Purpose: Identify duplicate student IDs that may cause reporting or SIS integrity issues.

SELECT
    student_id,
    state_student_id,
    COUNT(*) AS record_count
FROM students
GROUP BY student_id, state_student_id
HAVING COUNT(*) > 1
ORDER BY record_count DESC;
