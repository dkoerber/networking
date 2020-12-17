import sqlite3

conn = sqlite3.connect('satnight.db')
c = conn.cursor()

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS beers (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        description TEXT,
        drinkable INTEGER
    )
    '''
)

starter_beers = [
    (1, 'guinness', 'thick and delicious', True),
    (2, 'modelo', 'its modelo time', True),
    (3, 'coors', 'dads favorite', False),
]

c.executemany('''INSERT INTO beers VALUES (?, ?, ?, ?)''', starter_beers)

conn.commit()
conn.close()
