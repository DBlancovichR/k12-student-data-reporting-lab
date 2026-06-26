-- CRDC-style discipline summary
-- Purpose: Summarize discipline incidents by action type and removal days.

SELECT
    action_taken,
    COUNT(*) AS incident_count,
    SUM(days_removed) AS total_days_removed
FROM discipline
GROUP BY action_taken
ORDER BY incident_count DESC, action_taken;
