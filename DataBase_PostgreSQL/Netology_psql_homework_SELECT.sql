/* 1. Название и год выхода альбомов, вышедших в 2018 году.*/
SELECT *
  FROM albums
 WHERE year = 2018;

/* 2. Название и продолжительность самого длительного трека.*/
SELECT name, duration 
  FROM songs
 ORDER BY duration DESC
 LIMIT 1;

/* 3. Название треков, продолжительность которых не менее 3,5 минут.*/
SELECT name, duration 
  FROM songs
 WHERE duration >= 210
 ORDER BY duration ASC;

/* 4. Названия сборников, вышедших в период с 2018 по 2020 год включительно.*/
SELECT name
  FROM collections
 WHERE year BETWEEN 2018 AND 2020;

/* 5. Исполнители, чьё имя состоит из одного слова.*/
SELECT name
  FROM artists
 WHERE name NOT ILIKE '% %';

/* 6. Название треков, которые содержат слово «мой» или «my».*/
SELECT name
  FROM songs
 WHERE name ILIKE 'my %'   -- все названия треков на английском, фильтрацию по слову "мое" решил не делать.
    OR name ILIKE '% my %' 
    OR name ILIKE '% my';