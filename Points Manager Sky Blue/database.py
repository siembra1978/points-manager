import sqlite3

def connect():
    print("Connecting")
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profiles (ID INTEGER,Name TEXT,Points INTEGER ,Description TEXT)")
    conn.commit()
    conn.close()
    print("Connected")

def create(ID,Name,Points,Description):
    print("Creating Profile")
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO profiles VALUES (?,?,?,?)",(ID,Name,Points,Description))
    conn.commit()
    conn.close()
    print("Created Profile")

def list():
    print("Listing")
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM profiles")
    rows=cur.fetchall()
    conn.close()
    print("Listed")
    return rows

def add(ide,p):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("UPDATE profiles SET Points = Points + ? WHERE ID=?",(p,ide))
    conn.commit()
    conn.close()

def subtract(ide,p):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("UPDATE profiles SET Points = Points - ? WHERE ID=?",(p,ide))
    conn.commit()
    conn.close()

def delete(ID):
    print("Deleting Profile")
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM profiles WHERE ID = ?",(ID,))
    conn.commit()
    conn.close()
    print("Deleted Profile")
