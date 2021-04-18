from tkinter import *
import os
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
root=Tk()
filename = PhotoImage(file = "1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
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

USERNAME=StringVar()
NAME=StringVar()
EMAIL=StringVar()
PHONE=IntVar()
PASSWORD=StringVar()
CPASSWORD=StringVar()
LOCATION=StringVar()
TYPE_OF_MEDICINE=StringVar()
USERNAME.set("")
PASSWORD.set("")
CPASSWORD.set("")
NAME.set("")
EMAIL.set("")
PHONE.set("")
LOCATION.set("")
TYPE_OF_MEDICINE.set("")
conn=sqlite3.connect("database.db")
cursor=conn.cursor()
cursor.execute("create table if not exists 'medicinereg1'(username text primary key,name text,email text,phone text,password text,cpassword text,location text,type_of_medicine text)")

def Savedata():
    
    if(PASSWORD.get()) != (CPASSWORD.get()):
        tkMessageBox.showwarning('',"PASSWORD MISMATCH",icon="warning")

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
                
            
        if a==1:

            conn=sqlite3.connect("database.db")
            cursor=conn.cursor()
            cursor.execute("insert into 'medicinereg1'(username,name,email,phone,password,cpassword,location,type of medicine)values(?,?,?,?,?,?,?,?)",(str(USERNAME.get()),str(NAME.get()),str(EMAIL.get()),str(PHONE.get()),str(PASSWORD.get()),str(CPASSWORD.get()),str(LOCATION.get()),str(TYPE_OF_MEDICINE.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            CPASSWORD.set("")
            NAME.set("")
            EMAIL.set("")
            PHONE.set("")
            LOCATION.set("")
            TYPE_OF_MEDICINE.set("")
            tkMessageBox.showwarning('',"REGISTERED SUCCESSFULLY",icon="warning")
            
        else:
             tkMessageBox.showwarning('',"Username already taken",icon="warning")


def abc():
    
    root.destroy()
 
    import login
 
def back():
    root.destroy()
    import home
def login_user():
    root.destroy()
    import login

        


   

Top=Frame(root,width=500,bd=1,relief=SOLID)
Top.pack(side=TOP)
 
lbl_title1=Label(Top,text="REGISTRATION FORM",font=("Helvetica",16),bg="#3D9140",fg="white")
lbl_title1.grid(row=0,column=1,padx=10, pady=10)


 
Mid=Frame(root,width=500)
Mid.pack(side=TOP)

lbl_name=Label(Mid,text="NAME",font=('arial',14),bg="black",fg="white")
lbl_name.grid(row=1,sticky=W,padx=10, pady=10)
lbl_email=Label(Mid,text="EMAIL",font=('arial',14),bg="black",fg="white")
lbl_email.grid(row=2,sticky=W,padx=10, pady=10)
lbl_phone=Label(Mid,text="PHONE",font=('arial',14),bg="black",fg="white")
lbl_phone.grid(row=3,sticky=W,padx=10, pady=10)

lbl_uname=Label(Mid,text="User Name",font=('arial',14),bg="black",fg="white")
lbl_uname.grid(row=4,sticky=W,padx=10, pady=10)
lbl_pass=Label(Mid,text="Password",font=('arial',14),bg="black",fg="white")
lbl_pass.grid(row=5,sticky=W,padx=10, pady=10)
lbl_cpass=Label(Mid,text="Confirm Password",font=('arial',14),bg="black",fg="white")
lbl_cpass.grid(row=6,padx=10, pady=10)

lbl_loc=Label(Mid,text="location",font=('arial',14),bg="black",fg="white")
lbl_loc.grid(row=7,sticky=W,padx=10, pady=10)
lbl_tom=Label(Mid,text="type_of_medicine",font=('arial',14),bg="black",fg="white")
lbl_tom.grid(row=8,sticky=W,padx=10, pady=10)


name=Entry(Mid,textvariable=NAME,font=("arial",14))
name.grid(row=1,column=1)
email=Entry(Mid,textvariable=EMAIL,font=("arial",14))
email.grid(row=2,column=1)
phone=Entry(Mid,textvariable=PHONE,font=("arial",14))
phone.grid(row=3,column=1)

username=Entry(Mid,textvariable=USERNAME,font=("arial",14))
username.grid(row=4,column=1)
password=Entry(Mid,textvariable=PASSWORD,show="*",font=("arial",14))
password.grid(row=5,column=1)
cpassword=Entry(Mid,textvariable=CPASSWORD,show="*",font=("arial",14))
cpassword.grid(row=6,column=1)
location=Entry(Mid,textvariable=LOCATION,font=("arial",14))
location.grid(row=7,column=1)
type_of_room=Entry(Mid,textvariable=TYPE_OF_MEDICINE,font=("arial",14))
type_of_room.grid(row=8,column=1)

btn_reg=Button(Mid,text="REGISTER",width=40,command=Savedata,bg="#8B4513",fg="white")
btn_reg.grid(row=9,columnspan=2,pady=10)

lbl_abc=Label(Mid,text="Already User?",font=('arial',14),bg="black",fg="white")
lbl_abc.grid(row=10,sticky=W)
btn_log=Button(Mid,text="LOGIN",width=30,command=login_user,bg="#8B4513",fg="white")
btn_log.grid(row=10,column=1,pady=10)
btn_back=Button(Mid,text="BACK",width=30,command=back,bg="#8B4513",fg="white")
btn_back.grid(row=11,column=1,pady=10)



