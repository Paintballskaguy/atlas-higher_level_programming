-- Script to create a second_table and insert rows
-- Creates the table with columns id, name, score
--puts 4 records into the table.

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8)

ON DUPLICATE KEY UPDATE score = VALUES(score);