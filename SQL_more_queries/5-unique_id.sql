-- script to create table unique_id

CREATE TABLE IF NOT EXISTS unique_id(
    id INT default 1 unique,
    name VARCHAR(256)
);