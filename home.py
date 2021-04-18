from tkinter import *
import os
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root=Tk()

filename=PhotoImage(file="1.png")
background_label = Label(root, image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

root.title("MEDICAL STORE MANAGEMENT SYSTEM")

width=900
height=700
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(width/2)
y=(screen_height/2)-(height/2)
root.geometry("%dx%d+%d+%d"%(width,height,x,y))
root.resizable(0,0)
root.config()

def login_user():
    root.destroy()
    import login
def login_reg():
    root.destroy()
    import reg
def add():
    root.destroy()
    import add
def delete():
    root.destroy()
    import delete

Top=Frame(root,width=500,bd=1,relief=SOLID)
Top.pack(side=TOP)

lbl_title1=Label(Top,text="REGISTRATION FORM",font=("Helvetica",16),bg="#2D1340",fg="white")
lbl_title1.grid(row=1,column=1,padx=10,pady=10)

Mid=Frame(root,width=100)
Mid.pack(side=TOP)

btn_userlogin=Button(Mid,text="USER LOGIN",width=40,command=login_user,bg="#8B4513",fg="white")
btn_userlogin.grid(row=3,columnspan=2,pady=10)

btn_userregister=Button(Mid,text="USER_REGISTER",width=40,command=login_reg,bg="#8B4513",fg="white")
btn_userregister.grid(row=5,columnspan=2,pady=10)

btn_addmedicine=Button(Mid,text="ADD_MEDICINE",width=40,command=add,bg="#8B4513",fg="white")
btn_addmedicine.grid(row=7,columnspan=2,pady=10)

btn_delmedicine=Button(Mid,text="DELETE_MEDICINE",width=40,command=delete,bg="#8B4513",fg="white")
btn_delmedicine.grid(row=9,columnspan=2,pady=10)


                                                    
              
 
