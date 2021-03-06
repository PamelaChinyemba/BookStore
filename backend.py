import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer isbn integer)")
    conn.commit()
    conn.close


def insert(title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall
    
    conn.close
    return rows

connect()

insert ("The sea", "James Blunt", 2022, 9001487526)
print (view())
