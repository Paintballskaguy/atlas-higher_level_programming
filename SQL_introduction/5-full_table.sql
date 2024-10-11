-- Script to print the description of the table first_table from the current database

SELECT column_name, column_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'first_table'
AND table_schema = DATABASE();
