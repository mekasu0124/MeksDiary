import sqlite3 as sql

def add_to_db(title,date,details):
    with sql.connect("./server/main.db") as mdb:
        cur = mdb.cursor()

        srch = 'INSERT INTO entries(title, date, details) VALUES (?,?,?)'
        val = (title, date, details)

        try:
            cur.execute(srch, val)
            return True
        except Exception as e:
            raise e

def get_combo_list():
    with sql.connect("./server/main.db") as mdb:
        cur = mdb.cursor()

        results = cur.execute('SELECT id, title, date, details FROM entries').fetchall()

        return_list = []

        for result in results:
            id = result[0]
            title = result[1]
            date = result[2]
            details = result[3]

            text = f"{id} - {title} - {date} - {details}"
            return_list.append(text)

        return return_list
    
def update_db(id,title,date,details):
    with sql.connect("./server/main.db") as mdb:
        cur = mdb.cursor()

        srch = 'UPDATE entries SET title=?, date=?, details=? WHERE id=?'
        val = (title, date, details, id)

        try:
            cur.execute(srch, val)
            return True
        except Exception as e:
            raise e