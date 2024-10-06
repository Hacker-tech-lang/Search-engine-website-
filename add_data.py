import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('search.db')
cursor = conn.cursor()

# Insert sample documents
documents = [
    ('First Document', 'This is the content of the first document.'),
    ('Second Document', 'This is the content of the second document.'),
    ('Third Document', 'This is more text in the third document.')
]

# Insert data into the documents table
cursor.executemany("INSERT INTO documents (title, content) VALUES (?, ?)", documents)

conn.commit()
conn.close()
