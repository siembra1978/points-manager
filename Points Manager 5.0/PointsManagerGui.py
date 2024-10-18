import database, database2, database3, database4, webbrowser
from tkinter import *

window=Tk()
window.title("Points Manager")
window.iconbitmap("pmlogo1icon.ico")

def SetupPass():
    def Finish():
        passw=pe.get()
        database4.setuppass(passw)
        p.destroy()
    p=Tk()
    p.title("Setup Password")
    p.iconbitmap("pmlogo1icon.ico")
    pl=Label(p,text="Enter New Password Below")
    pl.grid(row=0,column=0)
    pe=Entry(p,show="*")
    pe.grid(row=1,column=0)
    pb=Button(p,text="Ok",command=Finish)
    pb.grid(row=2,column=0)
    p.mainloop()

def HelpHtml():
    webbrowser.open_new_tab("Help.html")

def delete_data():
    def deleteitall():
        Pass=pe.get()
        str(Pass)
        NPass=database4.check()
        str(NPass)
        print(NPass)
        if Pass == NPass:
            print("Deleting All Data")
            database.delete_all()
            database2.delete_all()
            database3.delete_all()
            p.destroy()
        else:
            print("Wrong Password")
    p=Tk()
    p.title("Delete All Data")
    p.iconbitmap("pmlogo1icon.ico")
    pl=Label(p,text="Enter Your Password to Delete All Data")
    pl.grid(row=0,column=0)
    pe=Entry(p,show="*")
    pe.grid(row=1,column=0)
    pb=Button(p,text="Ok",command=deleteitall)
    pb.grid(row=2,column=0)
    p.mainloop()

def delete_window():
    deletew=Tk()
    deletew.iconbitmap("pmlogo1icon.ico")
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

def store():
    storew=Tk()
    storew.iconbitmap("pmlogo1icon.ico")
    def get_selected_row(event):
        global selected_storetuple
        index=storel.curselection()[0]
        selected_storetuple=storel.get(index)
    def listitems():
        storel.delete(0,END)
        for row in database2.display():
            storel.insert(END,row)
    storew.title("Store")
    storel=Listbox(storew,height=10,width=50)
    storel.grid(row=0,column=0,columnspan=5)

    storel.bind('<<ListboxSelect>>',get_selected_row)
    listitems()
    def createitem_command():
        ciw=Tk()
        def createitemd():
            N=cie1.get()
            P=cie2.get()
            D=cie3.get()
            database2.createitem(N,P,D)
            listitems()
            ciw.destroy()
        ciw.title("Create Item")
        cie1=Entry(ciw)
        cie1.grid(row=1,column=0)
        cie1l=Label(ciw,height=1,width=15,text="Name")
        cie1l.grid(row=0,column=0)
        cie2=Entry(ciw)
        cie2.grid(row=1,column=1)
        cie2l=Label(ciw,height=1,width=15,text="Price")
        cie2l.grid(row=0,column=1)
        cie3=Entry(ciw)
        cie3.grid(row=1,column=2)
        cie3l=Label(ciw,height=1,width=15,text="Description")
        cie3l.grid(row=0,column=2)
        cib=Button(ciw,text="Confirm",command=createitemd)
        cib.grid(row=2,column=1)
        ciw.mainloop()
    def purchase():
        def confirm(listtuple):
            biw=Tk()
            biw.iconbitmap("pmlogo1icon.ico")
            biw.title("Are you sure?")
            def finalp():
                print(listtuple[0])
                database.subtract(listtuple[0],selected_storetuple[1])
                print("Item Purchased")
                biw.destroy()
            bil=Label(biw,height=1,width=45,text="Are you sure you want to buy this item?")
            bil.grid(row=0,column=0)
            bib=Button(biw,text="Yes, I am sure.",command=finalp)
            bib.grid(row=1,column=0)
            biw.mainloop()
        profilesel=Tk()
        profilesel.iconbitmap("pmlogo1icon.ico")
        def get_selected_rows(event):
            global selected_storetuple2
            index=listb.curselection()[0]
            selected_storetuple2=listb.get(index)
            print(selected_storetuple2)
        def fullsel():
            profilesel.destroy()
            confirm(selected_storetuple2)
        profilesel.title("Select A Profile")
        listb=Listbox(profilesel,height=10,width=50)
        listb.grid(row=0,column=0)
        def list_command():
            listb.delete(0,END)
            for row in database.list():
                listb.insert(END,row)
        list_command()
        listbutton=Button(profilesel,text="Select",command=fullsel)
        listbutton.grid(row=1,column=0)
        sb1=Scrollbar(profilesel)
        sb1.grid(row=0,column=1)

        listb.configure(yscrollcommand=sb1.set)
        sb1.configure(command=listb.yview)

        listb.bind('<<ListboxSelect>>',get_selected_rows)
        profilesel.mainloop()

    def deleteitem_command():
        database2.removeitem(selected_storetuple[0])
        listitems()
    createitemb=Button(storew,text="Create Item",command=createitem_command)
    createitemb.grid(row=1,column=0)
    buyitemb=Button(storew,text="Purchase Item",command=purchase)
    buyitemb.grid(row=1,column=1)
    deleteitemb=Button(storew,text="Delete Item",command=deleteitem_command)
    deleteitemb.grid(row=1,column=2)
    sb1=Scrollbar(storew)
    sb1.grid(row=0,column=6)

    storel.configure(yscrollcommand=sb1.set)
    sb1.configure(command=storel.yview)
    storew.mainloop()

def list_window():
    listw=Tk()
    listw.iconbitmap("pmlogo1icon.ico")
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

def add_command(event):
    def close():
        ide=ID.get()
        Points=e.get()
        Desc=e2.get()
        database.add(ide,Points)
        Type=("Add")
        print(Type)
        database3.log(ide,Points,Desc,Type)
        add.destroy()
    add=Tk()
    add.iconbitmap("pmlogo1icon.ico")
    add.title("Add Points")
    ID=Entry(add)
    ID.grid(row=1,column=0)
    e=Entry(add)
    e.grid(row=1,column=1)
    e2=Entry(add)
    e2.grid(row=1,column=2)
    addb=Button(add,text="Confirm",command=close)
    addb.grid(row=2,column=1)
    addl=Label(add,height=1,width=15,text="Enter Profile ID")
    addl.grid(row=0,column=0)
    add2=Label(add,height=1,width=15,text="Amount of Points")
    add2.grid(row=0,column=1)
    add3=Label(add,height=1,width=15,text="Description")
    add3.grid(row=0,column=2)
    add.mainloop()
    print("add")

def subtract_command():
    def close():
        ide=ID.get()
        Points=e.get()
        Desc=e2.get()
        database.subtract(ide,Points)
        Type=("Remove")
        print(Type)
        database3.log(ide,Points,Desc,Type)
        add.destroy()
    add=Tk()
    add.iconbitmap("pmlogo1icon.ico")
    add.title("Remove Points")
    ID=Entry(add)
    ID.grid(row=1,column=0)
    e=Entry(add)
    e.grid(row=1,column=1)
    e2=Entry(add)
    e2.grid(row=1,column=2)
    addb=Button(add,text="Confirm",command=close)
    addb.grid(row=2,column=1)
    addl=Label(add,height=1,width=15,text="Enter Profile ID")
    addl.grid(row=0,column=0)
    add2=Label(add,height=1,width=15,text="Amount of Points")
    add2.grid(row=0,column=1)
    add3=Label(add,height=1,width=15,text="Description")
    add3.grid(row=0,column=2)
    add.mainloop()
    print("subtract")

def profile_creator():
    def close():
        create_command()
        pc.destroy()
    pc=Tk()
    pc.iconbitmap("pmlogo1icon.ico")
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

def log():
    def lgclose():
        lg.destroy()
    lg=Tk()
    lg.iconbitmap("pmlogo1icon.ico")
    lg.title("Points Log")
    lgb=Listbox(lg,height=20,width=100)
    lgb.grid(row=0,column=0)
    lgc=Button(lg,text="Go Back",command=lgclose)
    lgc.grid(row=1,column=0)
    def lglist():
        lgb.delete(0,END)
        for row in database3.show():
            lgb.insert(END,row)
    lglist()
    sblg=Scrollbar(lg)
    sblg.grid(row=0,column=1)

    lgb.configure(yscrollcommand=sblg.set)
    sblg.configure(command=lgb.yview)
    lg.mainloop()

b1=Button(window,text="List Profiles",command=list_window,height=5,width=12)
b1.grid(row=0,column=0)

b2=Button(window,text="Add Points",command=lambda:add_command(1),height=5,width=12)
b2.grid(row=0,column=1)

window.bind('<Control-a>', add_command)

b3=Button(window,text="Remove Points",command=subtract_command,height=5,width=12)
b3.grid(row=1,column=1)

b4=Button(window,text="Create Profile",command=profile_creator,height=5,width=12)
b4.grid(row=0,column=2)

b5=Button(window,text="Help",command=HelpHtml,height=5,width=12)
b5.grid(row=1,column=0)

b6=Button(window,text="Delete Profiles",command=delete_window,height=5,width=12)
b6.grid(row=1,column=2)

b7=Button(window,text="Store",command=store,height=5,width=12)
b7.grid(row=0,column=3)

b7=Button(window,text="Points Log",command=log,height=5,width=12)
b7.grid(row=1,column=3)

b8=Button(window,text="Delete All Data",command=delete_data,height=5,width=12)
b8.grid(row=0,column=4)

b9=Button(window,text="Setup Password",command=SetupPass,height=5,width=12)
b9.grid(row=1,column=4)

canvas = Canvas(width=88, height=88, bg='white')
canvas.grid(row=0,column=6,rowspan=5)
img = PhotoImage(file='pmlogo1ppm.ppm')
canvas.create_image(0, 0, image=img, anchor=NW)

database.connect()
database2.setup()
database3.setup3()
database4.connect()

window.mainloop()
