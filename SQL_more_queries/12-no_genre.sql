-- Script to show all the shows in the database

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id
ORDER BY tv_shows.title ASC;