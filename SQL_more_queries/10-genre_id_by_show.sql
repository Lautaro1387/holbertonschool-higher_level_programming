-- Lists all shows contained in hbtn_0d_tvshows
SELECT tv_show.title, tv_show_genrs.genre_id
FROM tv_show JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id
ORDER BY tv_show.title, tv_show_genres.genr_id ASC;