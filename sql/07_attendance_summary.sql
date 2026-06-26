-- Attendance summary
-- Purpose: Identify attendance patterns that may require intervention or reporting review.

SELECT
    student_id,
    school_year,
    days_enrolled,
    days_present,
    days_absent,
    attendance_rate
FROM attendance
WHERE attendance_rate < 90.00
ORDER BY attendance_rate ASC;
