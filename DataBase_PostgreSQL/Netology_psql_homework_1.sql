CREATE TABLE IF NOT EXISTS genres (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL
	);
	
CREATE TABLE IF NOT EXISTS artists (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL 
	);

CREATE TABLE IF NOT EXISTS artists_genres (
	genre_id INTEGER REFERENCES genres(id) NOT NULL,
	artist_id INTEGER REFERENCES artists(id) NOT NULL,
	UNIQUE (genre_id, artist_id)
	);
	
CREATE TABLE IF NOT EXISTS albums (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	year DATE DEFAULT NULL
	);
	
CREATE TABLE IF NOT EXISTS artists_albums (
	artist_id INTEGER REFERENCES artists(id) NOT NULL,
	album_id INTEGER REFERENCES albums(id) NOT NULL,
	UNIQUE (artist_id, album_id)
);

CREATE TABLE IF NOT EXISTS songs (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	album_id INTEGER REFERENCES albums(id) NOT NULL,
	duration TEXT DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS collections (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	year DATE DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS collections_songs (
	collection_id INTEGER REFERENCES collections(id) NOT NULL,
	song_id INTEGER REFERENCES songs(id) NOT NULL,
	UNIQUE (collection_id, song_id)
);