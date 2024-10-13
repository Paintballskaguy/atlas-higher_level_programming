-- Script to list all cities from the database.

SELECT cities.id, cities.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;