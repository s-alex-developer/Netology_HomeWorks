/*не менее 5 жанров*/
INSERT INTO genres
VALUES (1, 'Trash Metal'),
       (2, 'Melodic Death Metal'),
	   (3, 'Heavy Metal'),
	   (4, 'Symphonic Metal'),
	   (5, 'Hard Rock'),
	   (6, 'Folk Metal'),
	   (7, 'Power Metal'),
	   (8, 'Nu Metal'),
	   (9, 'Alternative Metal');
	

/*не менее 8 исполнителей*/
INSERT INTO artists
VALUES
	(1, 'Metallica'),
	(2, 'Arch Enemy'),
	(3, 'Iron Maiden'),
	(4, 'Nightwish'),
	(5, 'Judas Priest'),
	(6, 'Korpiklaani'),
	(7, 'Megadeth'),
	(8, 'Manowar'),
	(9, 'Motorhead'),
	(10, 'Slipknot'),
	(11, 'Korn');

INSERT INTO artists_genres
VALUES 
	(1, 1),
	(2, 2),
	(4, 4),
	(5, 5),
	(3, 3),
	(6, 6),
	(1, 7),
	(7, 8),
	(5, 9),
	(8, 10),
	(9, 11);

/*не менее 8 альбомов*/
INSERT INTO albums
VALUES
	(1, 'Master of Puppets', 1986),
	(2, 'War Eternal', 2014),
	(3, 'Powerslave', 1984),
	(4, 'Century Child', 2002),
	(5, 'Endless Forms Most Beautiful', 2015),
	(6, 'Firepower', 2018),
	(7, 'Kulkija', 2018),
	(8, 'Youthanasia', 1994),
	(9, 'Countdown to Extinction', 1992),
	(10, 'Battle Hymns', 1982),
	(11, 'Load', 1996),
	(12, 'Orgasmatron ', 1986),
	(13, 'Slipknot', 1999),
	(14, 'Take a Look in the Mirror', 2003);

INSERT INTO artists_albums
VALUES
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(4, 5),
	(5, 6),
	(6, 7),
	(7, 8),
	(7, 9),
	(8, 10),
	(1, 11),
	(9, 12),
	(10, 13),
	(11, 14);

/*не менее 15 треков*/
INSERT INTO songs
VALUES
	(1, 'Master Of Puppets', 1, 516),
	(2,	'War Eternal', 2, 262),
	(3,	'Aces High', 3, 271),
	(4, 'End of All Hope', 4, 263),
	(5, 'Elan', 5, 287),
	(6, 'Firepower', 6, 207),
	(7, 'Tuttu on tie', 7, 442),
	(8, 'A Tout le Monde', 8, 265),
	(9, 'Symphony of Destruction', 9, 246),
	(10, 'Battle Hymn', 10, 530),
	(11, 'Manowar', 10, 219),
	(12, 'Metal Daze', 10, 260),
	(13, 'Ain`t My Bitch', 11, 304),
	(14, 'Ain`t My Crime', 12, 224),
	(15, 'Eyeless', 13, 236),
	(16, 'Did My Time',14, 247);

/*не менее 8 сборников*/
INSERT INTO collections
VALUES
	(1, 'Best Metal Of All Time', 2020),
	(2, 'Best of the Beast', 1996),
	(3, 'Decades', 2018),
	(4, 'Greatest Hits: Back to the Start', 2005),
	(5, 'Anthology', 1996),
	(6, 'The Best Of Motorhead', 2000),
	(7, 'Antennas to Hell', 2012),
	(8, 'Greatest Hits Vol. 1', 2014);

INSERT INTO collections_songs
VALUES
	(1, 1),
	(1, 2),
	(2, 3),
	(3, 4),
	(3, 5),
	(4, 8),
	(4, 9),
	(5, 10),
	(5, 11),
	(5, 12),
	(6, 14),
	(7, 15),
	(8, 16);