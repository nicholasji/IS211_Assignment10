DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Albums;
DROP TABLE IF EXISTS Songs;

CREATE TABLE artist (
  id    INTEGER PRIMARY KEY, 
  name  TEXT
);

CREATE TABLE albums (
  id INTEGER PRIMARY KEY,
  name TEXT,
  artist INTEGER,
  FOREIGN KEY(artist) REFERENCES artist(id)
);

CREATE TABLE songs (
  id INTEGER PRIMARY KEY,
  name TEXT,
  track INTEGER,
  duration REAL,
  album INTEGER,
  FOREIGN KEY(album) REFERENCES albums(id)
);