import sqlite3 as sql

def create_db():
    with sql.connect("./server/main.db") as mdb:
        cur = mdb.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS entries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        date TEXT,
        details TEXT
        )''')