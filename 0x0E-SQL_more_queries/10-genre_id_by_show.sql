-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT shows.title AS title, genres.genre_id AS genre_id
FROM tv_shows shows
LEFT JOIN tv_show_genres genres
ON shows.id = genres.show_id
WHERE genres.genre_id IS NOT NULL
ORDER BY title ASC, genre_id ASC;
