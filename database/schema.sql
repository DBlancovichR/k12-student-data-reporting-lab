-- SQLite schema for K-12 Student Data Reporting & Data Integrity Lab

DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS transcripts;
DROP TABLE IF EXISTS programs;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS discipline;

CREATE TABLE students (
    student_id INTEGER,
    state_student_id TEXT,
    first_name TEXT,
    last_name TEXT,
    grade_level INTEGER,
    enrollment_status TEXT,
    english_learner_status TEXT,
    special_education_status TEXT,
    section_504_status TEXT,
    graduation_status TEXT
);

CREATE TABLE enrollments (
    enrollment_id TEXT,
    student_id INTEGER,
    school_year TEXT,
    entry_date TEXT,
    exit_date TEXT,
    exit_code TEXT,
    grade_level INTEGER,
    enrollment_status TEXT
);

CREATE TABLE transcripts (
    transcript_id TEXT,
    student_id INTEGER,
    school_year TEXT,
    grade_level INTEGER,
    credits_attempted INTEGER,
    credits_earned INTEGER,
    gpa REAL,
    graduation_eligible TEXT,
    notes TEXT
);

CREATE TABLE programs (
    program_record_id TEXT,
    student_id INTEGER,
    program_name TEXT,
    program_status TEXT,
    start_date TEXT,
    end_date TEXT
);

CREATE TABLE attendance (
    attendance_id TEXT,
    student_id INTEGER,
    school_year TEXT,
    days_enrolled INTEGER,
    days_present INTEGER,
    days_absent INTEGER,
    attendance_rate REAL
);

CREATE TABLE discipline (
    incident_id TEXT,
    student_id INTEGER,
    school_year TEXT,
    incident_date TEXT,
    incident_type TEXT,
    action_taken TEXT,
    days_removed INTEGER
);
