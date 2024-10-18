import os
import pandas
import csv

commands=["List","Add","Remove","Create","Help","Exit"]
errors=["That is not a command!"]

#df1=pandas.read_csv("Data.csv")

def Profile(df1,I,N,P,D):
    df1Temp=df1.T
    df1Temp[I]=[I,N,P,D]
    df1=df1Temp.T
    print(df1)
    df1.to_csv("Data.csv", index=False)

def Command():
    c=input("Please enter a command: ")
    if c in commands:
        if c == commands[0]:
            df1=pandas.read_csv("Data.csv")
            print("Listing")
            print(df1)
            Command()
        elif c == commands[1]:
            df1=pandas.read_csv("Data.csv")
        elif c == commands[2]:
            df1=pandas.read_csv("Data.csv")
        elif c == commands[3]:
            df1=pandas.read_csv("Data.csv")
            Identity=input("Enter ID Number: ")
            Name=input("Enter Profile Name: ")
            Points=0
            Description=input("Enter Profile Description: ")
            Profile(df1,Identity,Name,Points,Description)
        elif c == commands[4]:
            print(commands)
            Command()
        elif c == commands[5]:
            print("Exiting Program")
    else:
        print(errors[0])
        Command()




print("Starting Points Manager ALPHA Version 1.0")
print("Enter 'Help' to View All Commands")
Command()
