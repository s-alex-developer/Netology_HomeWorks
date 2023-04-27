CREATE TABLE IF NOT EXISTS genres (
	PRIMARY KEY(id),
	  id SERIAL,
	name VARCHAR(50) NOT NULL,
	     UNIQUE(name)
);
	
CREATE TABLE IF NOT EXISTS artists (
	PRIMARY KEY(id),
	  id SERIAL,
	name VARCHAR(50) NOT NULL,
	     UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS artists_genres (
	 genre_id INTEGER NOT NULL,
			  FOREIGN KEY (genre_id) REFERENCES genres(id),
	artist_id INTEGER NOT NULL,
			  FOREIGN KEY (artist_id) REFERENCES artists(id),
			   UNIQUE (genre_id, artist_id)			  
);
	
CREATE TABLE IF NOT EXISTS albums (
	PRIMARY KEY(id),
	  id SERIAL,
	name VARCHAR(50) NOT NULL,
	year SMALLINT DEFAULT NULL 
		    CHECK (year BETWEEN 1850 AND 2050) 
);
	
CREATE TABLE IF NOT EXISTS artists_albums (
	artist_id INTEGER NOT NULL,
			  FOREIGN KEY (artist_id) REFERENCES artists(id),
	 album_id INTEGER NOT NULL,
	          FOREIGN KEY (album_id)  REFERENCES albums(id),
			   UNIQUE (artist_id, album_id)
);

CREATE TABLE IF NOT EXISTS songs (
	PRIMARY KEY(id),
	      id SERIAL,
	    name VARCHAR(50) NOT NULL,
	album_id INTEGER NOT NULL,
		     FOREIGN KEY (album_id) REFERENCES albums(id), 
	duration INTEGER DEFAULT NULL
			   CHECK (duration BETWEEN 1 AND 48212)
);

CREATE TABLE IF NOT EXISTS collections (
	PRIMARY KEY(id),
	  id SERIAL,
	name VARCHAR(50) NOT NULL,
	year smallint DEFAULT NULL
		 CHECK(year BETWEEN 1850 AND 2050)
);

CREATE TABLE IF NOT EXISTS collections_songs (
	collection_id INTEGER NOT NULL,
				  FOREIGN KEY (collection_id) REFERENCES collections(id),
	      song_id INTEGER NOT NULL,
			      FOREIGN KEY (song_id) REFERENCES songs(id),
	               UNIQUE (collection_id, song_id)
);