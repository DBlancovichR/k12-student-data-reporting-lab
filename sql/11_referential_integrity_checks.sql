-- Referential integrity checks
-- Purpose: Identify records in child data files that do not have matching student master records.

SELECT
    'Enrollment Missing Student Master Record' AS exception_type,
    e.student_id,
    e.enrollment_id AS source_record_id,
    'enrollments.csv' AS source_file
FROM enrollments e
LEFT JOIN students s
    ON e.student_id = s.student_id
WHERE s.student_id IS NULL

UNION ALL

SELECT
    'Transcript Missing Student Master Record' AS exception_type,
    t.student_id,
    t.transcript_id AS source_record_id,
    'transcripts.csv' AS source_file
FROM transcripts t
LEFT JOIN students s
    ON t.student_id = s.student_id
WHERE s.student_id IS NULL

UNION ALL

SELECT
    'Program Missing Student Master Record' AS exception_type,
    p.student_id,
    p.program_record_id AS source_record_id,
    'programs.csv' AS source_file
FROM programs p
LEFT JOIN students s
    ON p.student_id = s.student_id
WHERE s.student_id IS NULL

UNION ALL

SELECT
    'Attendance Missing Student Master Record' AS exception_type,
    a.student_id,
    a.attendance_id AS source_record_id,
    'attendance.csv' AS source_file
FROM attendance a
LEFT JOIN students s
    ON a.student_id = s.student_id
WHERE s.student_id IS NULL

UNION ALL

SELECT
    'Discipline Missing Student Master Record' AS exception_type,
    d.student_id,
    d.incident_id AS source_record_id,
    'discipline.csv' AS source_file
FROM discipline d
LEFT JOIN students s
    ON d.student_id = s.student_id
WHERE s.student_id IS NULL;
