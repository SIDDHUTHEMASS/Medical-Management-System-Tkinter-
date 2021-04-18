from tkinter import *
import os
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
root=Tk()
filename = PhotoImage(file = "1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.title("DELETE MEDICINE PAGE")
width=900
height=700
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(width/2)
y=(screen_height/2)-(height/2)
root.geometry("%dx%d+%d+%d"%(width,height,x,y))
root.resizable(0,0)
root.config()

MEDICINE_NAME=StringVar()
MEDICINE_TYPE=StringVar()
MEDICINE_COST=IntVar()

MEDICINE_NAME.set("")
MEDICINE_TYPE.set("")
MEDICINE_COST.set("")

conn=sqlite3.connect("database.db")
cursor=conn.cursor()
cursor.execute("create table if not exists 'medicinereg3'(medicine_name text primary key,medicine_type text,medicine_cost text)")

def Savedata():
    
    if MEDICINE_NAME.get()=="" or MEDICINE_TYPE.get()=="" or MEDICINE_COST.get()=="":
        tkMessageBox.showwarning('',"PLEASE ENTER CREDENTIALS",icon="warning")

    else:
        conn=sqlite3.connect("database.db")
        cursor=conn.cursor()
        cursor.execute("select MEDICINE_NAME from 'medicinereg3'")
        myresultset=cursor.fetchall()
        a=1
        b=MEDICINE_NAME.get()
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
            cursor.execute("delete from 'medicinereg3' where 'MEDICINE_NAME'=? and 'MEDICINE_TYPE'=? and 'MEDICINE_COST'=?",(MEDICINE_NAME.get(),MEDICINE_TYPE.get(),MEDICINE_COST.get()))
            conn.commit()
            MEDICINE_NAME.set("")
            MEDICINE_TYPE.set("")
            MEDICINE_COST.set("")
            
            tkMessageBox.showwarning('',"DELETED SUCCESSFULLY",icon="warning")
            
        else:
             tkMessageBox.showwarning('',"doesnot exists",icon="warning")


def abc():
    tkMessageBox.showwarning('',"cancelled",icon="warning")
    
 
    
def back():
    root.destroy()
    import home
        
        


   

Top=Frame(root,width=500,bd=1,relief=SOLID)
Top.pack(side=TOP)

Mid=Frame(root,width=500)
Mid.pack(side=TOP)

lbl_title1=Label(Top,text="DELETE MEDICINE PAGE",font=("helvetica",16),bg="#3D9140",fg="white")
lbl_title1.grid(row=0,column=1,padx=10, pady=10)

lbl_medicine_name=Label(Mid,text="MEDICINE NAME",font=('arial',14),bg="black",fg="white")
lbl_medicine_name.grid(row=1,sticky=W,padx=10, pady=10)
lbl_medicine_type=Label(Mid,text="MEDICINE TYPE",font=('arial',14),bg="black",fg="white")
lbl_medicine_type.grid(row=2,sticky=W,padx=10, pady=10)
lbl_medicine_cost=Label(Mid,text="MEDICINE COST",font=('arial',14),bg="black",fg="white")
lbl_medicine_cost.grid(row=3,sticky=W,padx=10, pady=10)


medicine_name=Entry(Mid,textvariable=MEDICINE_NAME,font=("arial",14))
medicine_name.grid(row=1,column=1)
medicine_type=Entry(Mid,textvariable=MEDICINE_TYPE,font=("arial",14))
medicine_type.grid(row=2,column=1)
medicine_cost=Entry(Mid,textvariable=MEDICINE_COST,font=("arial",14))
medicine_cost.grid(row=3,column=1)


btn_userlogin=Button(Mid,text="DELETE",width=30,command=Savedata,bg="#8B4513",fg="white")
btn_userlogin.grid(row=4,columnspan=2,pady=10)

btn_back=Button(Mid,text="BACK",width=30,command=back,bg="#8B4513",fg="white")
btn_back.grid(row=5,columnspan=2,pady=10)
