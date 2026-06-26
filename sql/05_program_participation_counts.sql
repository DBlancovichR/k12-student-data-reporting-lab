-- Program participation count report
-- Purpose: Summarize active program participation for reporting review.

SELECT
    program_name,
    program_status,
    COUNT(DISTINCT student_id) AS student_count
FROM programs
GROUP BY program_name, program_status
ORDER BY program_name, program_status;
