-- Script to get all the comedy shows

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
GROUP BY tv_shows.title;