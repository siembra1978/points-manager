import sqlite3

def setup():
    print("Setting Up Store Database")
    conn=sqlite3.connect("storedata.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (Name TEXT, Description TEXT, Points INTEGER)")
    conn.commit()
    conn.close()
    print("Store Database Setup Complete")

def createitem(Name, Description, Points):
    print("Creating Item")
    conn=sqlite3.connect("storedata.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(Name, Description, Points))
    conn.commit()
    conn.close()
    print("Item Created")

def removeitem(Name):
    print("Removing Item")
    conn=sqlite3.connect("storedata.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE Name = ?",(Name,))
    conn.commit()
    conn.close()
    print("Item Removed")

def display():
    print("Displaying")
    conn=sqlite3.connect("storedata.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    print("Displaying")
    return rows

def delete_all():
    conn=sqlite3.connect("storedata.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store")
    conn.commit()
    conn.close()
