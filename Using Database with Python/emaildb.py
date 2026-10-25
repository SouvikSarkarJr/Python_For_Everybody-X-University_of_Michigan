import sqlite3

# Connect to (or create) the SQLite database file
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Clear out any previous table
cur.execute('DROP TABLE IF EXISTS Counts')

# Create the required schema
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'

try:
    fh = open(fname)
except FileNotFoundError:
    print(f"File not found: {fname}")
    quit()

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    
    # Extract domain/organization after '@'
    org = email.split('@')[1]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

# Commit once outside the loop for speed
conn.commit()

# Print top 10 results
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print("Counts:")
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
conn.close()
