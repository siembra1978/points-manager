import database
from tkinter import *

window=Tk("Test")

window.title("Points Manager Version 3.0")

e1=Entry(window)
e1.grid(row=2,column=1)
e2=Entry(window)
e2.grid(row=2,column=2)
e3=Entry(window)
e3.grid(row=2,column=3)

l1=Listbox(window,height=10,width=50)
l1.grid(row=6,column=4)
t2=Label(window,height=1,width=15,text="ID Number")
t2.grid(row=1,column=1)
t3=Label(window,height=1,width=15,text="Name")
t3.grid(row=1,column=2)
t4=Label(window,height=1,width=15,text="Description")
t4.grid(row=1,column=3)
t5=Label(window,height=1,width=15,text="Point Managing")
t5.grid(row=4,column=2)
t6=Label(window,height=1,width=15,text="Profile Manager")
t6.grid(row=0,column=2)

sb1=Scrollbar(window)
sb1.grid(row=6,column=5)

l1.configure(yscrollcommand=sb1.set)
sb1.configure(command=l1.yview)

def list_command():
    l1.delete(0,END)
    for row in database.list():
        l1.insert(0,row)

def create_command():
    database.create(e1.get(),e2.get(),0,e3.get())
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

def add_command():
    def close():
        ide=ID.get()
        Points=e.get()
        database.add(ide,Points)
        add.destroy()
    add=Tk()
    add.title("Add Points")
    ID=Entry(add)
    ID.grid(row=0,column=1)
    e=Entry(add)
    e.grid(row=0,column=3)
    addb=Button(add,text="Confirm",command=close)
    addb.grid(row=1,column=1)
    addl=Label(add,height=1,width=15,text="Enter Profile ID")
    addl.grid(row=0,column=0)
    add2=Label(add,height=1,width=15,text="Amount of Points")
    add2.grid(row=0,column=2)
    add.mainloop()
    print("add")

def subtract_command():
    def close():
        ide=ID.get()
        Points=e.get()
        database.subtract(ide,Points)
        add.destroy()
    add=Tk()
    add.title("Remove Points")
    ID=Entry(add)
    ID.grid(row=0,column=1)
    e=Entry(add)
    e.grid(row=0,column=3)
    addb=Button(add,text="Confirm",command=close)
    addb.grid(row=1,column=1)
    addl=Label(add,height=1,width=15,text="Enter Profile ID")
    addl.grid(row=0,column=0)
    add2=Label(add,height=1,width=15,text="Amount of Points")
    add2.grid(row=0,column=2)
    add.mainloop()
    print("subtract")

b1=Button(window,text="List",command=list_command)
b1.grid(row=5,column=4)

b2=Button(window,text="Add",command=add_command)
b2.grid(row=5,column=1)

b3=Button(window,text="Remove",command=subtract_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Create",command=create_command)
b4.grid(row=3,column=2)

b5=Button(window,text="Help")
b5.grid(row=7,column=0)

database.connect()

window.mainloop()
