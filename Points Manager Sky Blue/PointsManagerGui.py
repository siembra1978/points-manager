import database, time
from tkinter import *

window=Tk()

window.title("Points Manager Sky Blue")

def delete_window():
    deletew=Tk()
    def get_selected_row(event):
        global selected_tuple
        index=deletel.curselection()[0]
        selected_tuple=deletel.get(index)

    deletew.title("Delete Profiles")
    deletel=Listbox(deletew,height=10,width=50)
    deletel.grid(row=0,column=0)

    deletel.bind('<<ListboxSelect>>',get_selected_row)
    for row in database.list():
        deletel.insert(END,row)

    def deletew_command():
        database.delete(selected_tuple[0])
        deletel.delete(0,END)
        for thing in database.list():
            deletel.insert(END,thing)
    deletebutton=Button(deletew,text="Delete",command=deletew_command)
    deletebutton.grid(row=1,column=0)
    sb1=Scrollbar(deletew)
    sb1.grid(row=0,column=1)

    deletel.configure(yscrollcommand=sb1.set)
    sb1.configure(command=deletel.yview)
    deletew.mainloop()

def list_window():
    listw=Tk()
    listw.title("List Profiles")
    listb=Listbox(listw,height=10,width=50)
    listb.grid(row=0,column=0)
    def list_command():
        listb.delete(0,END)
        for row in database.list():
            listb.insert(END,row)
    list_command()
    listbutton=Button(listw,text="List",command=list_command)
    listbutton.grid(row=1,column=0)
    sb1=Scrollbar(listw)
    sb1.grid(row=0,column=1)

    listb.configure(yscrollcommand=sb1.set)
    sb1.configure(command=listb.yview)
    listw.mainloop()

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

def profile_creator():
    def close():
        create_command()
        pc.destroy()
    pc=Tk()
    pc.title("Profile Manager")
    e1=Entry(pc)
    e1.grid(row=1,column=0)
    e2=Entry(pc)
    e2.grid(row=1,column=1)
    e3=Entry(pc)
    e3.grid(row=1,column=2)
    t2=Label(pc,height=1,width=15,text="ID Number")
    t2.grid(row=0,column=0)
    t3=Label(pc,height=1,width=15,text="Name")
    t3.grid(row=0,column=1)
    t4=Label(pc,height=1,width=15,text="Description")
    t4.grid(row=0,column=2)
    t6=Label(pc,height=1,width=15,text="Profile Manager")
    b=Button(pc,text="Create",command=close)
    b.grid(row=2,column=1)
    def create_command():
        database.create(e1.get(),e2.get(),0,e3.get())
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
    pc.mainloop()

b1=Button(window,text="List",command=list_window)
b1.grid(row=0,column=0)

b2=Button(window,text="Add",command=add_command)
b2.grid(row=0,column=1)

b3=Button(window,text="Remove",command=subtract_command)
b3.grid(row=0,column=2)

b4=Button(window,text="Profiles",command=profile_creator)
b4.grid(row=0,column=3)

b5=Button(window,text="Help")
b5.grid(row=0,column=4)

b6=Button(window,text="Delete Profiles",command=delete_window)
b6.grid(row=0,column=5)

canvas = Canvas(width=88, height=88, bg='white')
canvas.grid(row=0,column=6,rowspan=5)
img = PhotoImage(file='perry.ppm')
canvas.create_image(0, 0, image=img, anchor=NW)

database.connect()

window.mainloop()
