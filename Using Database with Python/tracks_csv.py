import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Drop old tables to start clean
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'tracks.csv'

# CSV format:
# Track title, Artist, Album, Count, Rating, Length, Genre
# [0]          [1]     [2]    [3]    [4]     [5]     [6]

try:
    fh = open(fname)
except FileNotFoundError:
    print(f"File not found: {fname}")
    quit()

for line in fh:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 7:
        continue

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    # Insert or ignore Artist
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    # Insert or ignore Genre
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    # Insert or ignore Album
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    # Insert or replace Track
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        (name, album_id, genre_id, length, rating, count))

conn.commit()

# Run the validation query
test_sql = '''
SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track JOIN Genre JOIN Album JOIN Artist 
ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
    AND Album.artist_id = Artist.id
ORDER BY Artist.name LIMIT 3
'''

print("\n--- Test Query Output ---")
for row in cur.execute(test_sql):
    print(row[0], '|', row[1], '|', row[2], '|', row[3])

cur.close()
conn.close()
