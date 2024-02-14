-- Script to list all genres not linked to the show Dexter in hbtn_0d_tvshows
SELECT DISTINCT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
WHERE tv_shows.title != 'Dexter' OR tv_shows.title IS NULL
ORDER BY tv_genres.name ASC;
