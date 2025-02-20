import os
import pandas
from tkinter import *

window=Tk("Test")

window.title("Points Manager Version 2.0")

def Profile(df1,I,N,P,D):
    df1Temp=df1.T
    df1Temp[I]=[I,N,P,D]
    df1=df1Temp.T
    print(df1)
    df1.to_csv("Data.csv", index=False)

def List():
    t1.delete('1.0', END)
    df1=pandas.read_csv("Data.csv")
    print("Listing")
    print(df1)
    t1.insert(END,df1)

def Add():
    def aclose():
        add.destroy()
        
    df1=pandas.read_csv("Data.csv")
    def confirm():
        num=ID.get()
        intn=int(num)
        df1.at[intn-1:intn,2:3] = df1.iloc[intn-1:intn,2:3] + 5
        print(df1)
        df1.to_csv("Data.csv", index=False)
        aclose()
        
    add=Tk()
    add.title("Add Points")
    ID=Entry(add)
    ID.grid(row=0,column=1)
    addb=Button(add,text="Confirm",command=confirm)
    addb.grid(row=1,column=1)
    addl=Label(add,height=1,width=15,text="Enter Profile ID")
    addl.grid(row=0,column=0)
    
def Remove():
    def rclose():
        remove.destroy()
        
    df1=pandas.read_csv("Data.csv")
    def confirmr():
        num=ID.get()
        intn=int(num)
        df1.at[intn-1:intn,2:3] = df1.iloc[intn-1:intn,2:3] - 5
        print(df1)
        df1.to_csv("Data.csv", index=False)
        rclose()
        
    remove=Tk()
    remove.title("Remove Points")
    ID=Entry(remove)
    ID.grid(row=0,column=1)
    addb=Button(remove,text="Confirm",command=confirmr)
    addb.grid(row=1,column=1)
    addl=Label(remove,height=1,width=15,text="Enter Profile ID")
    addl.grid(row=0,column=0) 
    
def Create():
    df1=pandas.read_csv("Data.csv")
    Identity=e1.get()
    Name=e2.get()
    Points=0
    Description=e3.get()
    Profile(df1,Identity,Name,Points,Description)
    
def Help():
    def close():
        helpw.destroy()
    print("Help")
    helpw=Tk()
    helpw.title("Help")
    helpt=Text(helpw,height=10,width=50)
    helpt.grid(row=0,column=0)
    helpt.insert(END,"Welcome to Points Manager 2.0! This is the help window. To create a profile type the information above the button 'Create' and when you are finished, click create. To add points select a profile and click add. To remove points select a profile and click remove! If you need extra help please ask the programmer, siembra!")
    ok=Button(helpw,text="Ok",command=close)
    ok.grid(row=1,column=0)
    helpw.mainloop()
    
b1=Button(window,text="List",command=List)
b1.grid(row=5,column=4)

b2=Button(window,text="Add",command=Add)
b2.grid(row=5,column=1)

b3=Button(window,text="Remove",command=Remove)
b3.grid(row=5,column=3)

b4=Button(window,text="Create",command=Create)
b4.grid(row=3,column=2)

b5=Button(window,text="Help",command=Help)
b5.grid(row=7,column=0)

e1=Entry(window)
e1.grid(row=2,column=1)
e2=Entry(window)
e2.grid(row=2,column=2)
e3=Entry(window)
e3.grid(row=2,column=3)

t1=Text(window,height=10,width=50)
t1.grid(row=6,column=4)
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

window.mainloop()
