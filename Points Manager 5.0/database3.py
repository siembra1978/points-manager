import sqlite3, datetime

def setup3():
    print("Setting Up Log")
    conn=sqlite3.connect("logdata.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS log (ID TEXT, Points INTEGER, Description TEXT, Date TEXT, Type TEXT)")
    conn.commit()
    conn.close()
    print("Log Complete")

def log(ID, Points, Description, Type):
    Date=datetime.datetime.now()
    print("Logging")
    conn=sqlite3.connect("logdata.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO log VALUES (?,?,?,?,?)",(ID, Points, Description, Date, Type))
    conn.commit()
    conn.close()
    print("Logged")

def show():
    print("Showing")
    conn=sqlite3.connect("logdata.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM log")
    rows=cur.fetchall()
    conn.close()
    print("Showing")
    return rows

def delete_all():
    conn=sqlite3.connect("logdata.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM log")
    conn.commit()
    conn.close()
