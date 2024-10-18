import sqlite3

def connect():
    conn=sqlite3.connect("important.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS pass (Pass TEXT)")
    conn.commit()
    conn.close()

def setuppass(Pass):
    print(Pass)
    conn=sqlite3.connect("important.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM pass")
    cur.execute("INSERT INTO pass VALUES (?)",(Pass,))
    conn.commit()
    conn.close()

def check():
    conn=sqlite3.connect("important.db")
    cur=conn.cursor()
    cur.execute("SELECT Pass FROM pass")
    row=cur.fetchall()
    conn.close()
    return row
