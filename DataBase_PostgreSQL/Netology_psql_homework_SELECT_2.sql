/* 1. Количество исполнителей в каждом жанре.*/

SELECT ge.name AS music_genres, 
       COUNT(ar.*) AS number_of_artists
  FROM genres AS ge
       JOIN artists_genres AS ag 
         ON ge.id = ag.genre_id
       JOIN artists AS ar 
         ON ar.id = ag.artist_id
 GROUP BY music_genres
 ORDER BY number_of_artists DESC;


/* 2. Количество треков, вошедших в альбомы 2019–2020 годов.*/

SELECT COUNT(so.name) AS number_of_songs
  FROM songs AS so, 
       albums AS al
 WHERE so.album_id = al.id 
   AND al.year IN (2019, 2020);
  

/* 3. Средняя продолжительность треков по каждому альбому.*/
  
SELECT al.name AS albums, 
       COUNT(so.*) AS songs_amount,    -- добавил кол-во треков для удобства проверки.
       TRUNC(AVG(so.duration), 3) AS average_song_duration    -- точность до миллисекунд.
  FROM albums AS al
       JOIN songs AS so 
         ON so.album_id = al.id
 GROUP BY albums
 ORDER BY average_song_duration DESC;


/* 4. Все исполнители, которые не выпустили альбомы в 2020 году.*/

SELECT ar.name AS artists, 
       al.name AS albums,
       al.year AS year_of_release
  FROM artists AS ar
       JOIN artists_albums AS aa 
         ON aa.artist_id = ar.id
       JOIN albums AS al 
         ON aa.album_id = al.id
 WHERE al.year <> 2020
 ORDER BY year_of_release DESC;


/* 5. Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).*/

SELECT co.name AS collection_names
  FROM collections AS co
       JOIN collections_songs AS cs 
         ON cs.collection_id = co.id 
       JOIN songs AS so 
         ON cs.song_id = so.id
       JOIN albums AS al
         ON al.id = so.album_id
       JOIN artists_albums AS aa
         ON aa.album_id = al.id
       JOIN artists AS ar 
         ON aa.artist_id = ar.id
 WHERE ar.name IN ('Metallica', 'Manowar', 'Sepultura') -- Кол-во песен в сборниках: Metallica 1 песня, Manowar 3 песни, Sepultura 0 песен.
 GROUP BY collection_names
 ORDER BY collection_names;

/* 6. Названия альбомов, в которых присутствуют исполнители более чем одного жанра.*/

SELECT al.name AS album_names
  FROM albums AS al
       JOIN artists_albums AS aa
         ON aa.album_id = al.id
       JOIN artists AS ar
         ON aa.artist_id = ar.id 
       JOIN artists_genres AS ag
         ON ag.artist_id = ar.id
       JOIN genres AS ge 
         ON ag.genre_id = ge.id
 GROUP BY album_names
HAVING Count(ge.name) > 1
 ORDER BY album_names ASC;


/* 7. Наименования треков, которые не входят в сборники.*/

SELECT name as songs
  FROM songs
 WHERE name NOT IN
       (SELECT so.name
          FROM songs AS so
          JOIN collections_songs AS cs
            ON cs.song_id = so.id 
          JOIN collections AS co 
            ON cs.collection_id = co.id)
 ORDER BY name ASC;

/* 8. Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько.*/

SELECT ar.name AS artist, 
       so.name AS song_name,
       so.duration AS duration
  FROM artists AS ar
       JOIN artists_albums AS aa
         ON aa.artist_id = ar.id
       JOIN albums AS al
         ON aa.album_id = al.id 
       JOIN songs AS so
         ON so.album_id = al.id 
 WHERE so.duration = 
       (SELECT MIN(duration) 
          FROM songs);

/* 9. Названия альбомов, содержащих наименьшее количество треков.*/
         
SELECT al.name AS albums 
  FROM albums AS al, 
       songs AS so
 WHERE al.id = so.album_id 
 GROUP BY al.name
HAVING COUNT(so.*) = 
       (SELECT COUNT(so.*)
          FROM albums AS al, 
               songs AS so
         WHERE al.id = so.album_id
         GROUP BY al.name
         ORDER BY count(so.*) ASC
         LIMIT 1)
ORDER BY albums;

