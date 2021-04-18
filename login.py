from tkinter import *
import os
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
root=Tk()
filename = PhotoImage(file = "1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.title("USER LOGIN PAGE")
width=900
height=700
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(width/2)
y=(screen_height/2)-(height/2)
root.geometry("%dx%d+%d+%d"%(width,height,x,y))
root.resizable(0,0)
root.config()

USERNAME=StringVar()

PASSWORD=StringVar()

USERNAME.set("")
PASSWORD.set("")


conn=sqlite3.connect("database.db")
cursor=conn.cursor()
cursor.execute("create table if not exists 'medicinereg1'(username text primary key,password text)")

def Savedata():
    
    if USERNAME.get()=="" or PASSWORD.get()=="":
        tkMessageBox.showwarning('',"PLEASE ENTER CREDENTIALS",icon="warning")

    else:
        conn=sqlite3.connect("database.db")
        cursor=conn.cursor()
        cursor.execute("select username from 'medicinereg1'")
        myresultset=cursor.fetchall()
        a=1
        b=USERNAME.get()
        c="('"
        d="',)"
        b=c+b+d
        for data in myresultset:
            if (str(data) == str(b)):
                a=0
                break
                
            
        if a==0:

            conn=sqlite3.connect("database.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM 'medicinereg1' WHERE 'USERNAME'=? AND 'PASSWORD'=?",(USERNAME.get(),PASSWORD.get()))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            
            tkMessageBox.showwarning('',"LOGIN SUCCESSFULLY",icon="warning")
            
        else:
             tkMessageBox.showwarning('',"Username INVALID",icon="warning")



def back():
    root.destroy()
    import home
   
        


   

Top=Frame(root,width=500,bd=1,relief=SOLID)
Top.pack(side=TOP)

Mid=Frame(root,width=500)
Mid.pack(side=TOP)

lbl_title1=Label(Top,text="LOGIN FORM",font=("Helvetica",16),bg="#3D9140",fg="white")
lbl_title1.grid(row=0,column=1,padx=10, pady=10)


lbl_uname=Label(Mid,text="User Name",font=('arial',14),bg="black",fg="white")
lbl_uname.grid(row=1,sticky=W,padx=10, pady=10)
lbl_pass=Label(Mid,text="Password",font=('arial',14),bg="black",fg="white")
lbl_pass.grid(row=2,sticky=W,padx=10, pady=10)


username=Entry(Mid,textvariable=USERNAME,font=("arial",14))
username.grid(row=1,column=1)
password=Entry(Mid,textvariable=PASSWORD,show="*",font=("arial",14))
password.grid(row=2,column=1)

btn_userlogin=Button(Mid,text="LOGIN",width=20,command=Savedata,bg="#8B4513",fg="white")
btn_userlogin.grid(row=3,columnspan=2,pady=10)
btn_back=Button(Mid,text="BACK",width=20,command=back,bg="#8B4513",fg="white")
btn_back.grid(row=4,columnspan=2,pady=10)


