-- Script to list all the records and show only the score at or above 10.

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;