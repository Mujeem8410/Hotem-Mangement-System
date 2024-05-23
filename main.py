from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
import mysql.connector as m
from tkinter import messagebox    
from  sinup import sinupwindow
from  customer import custwindow
from  room import roombooking
from  forgett import forgetwindow
from details import details
class mainwindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Main Window For Hotel Management System")
        self.root.geometry("2100x1100+0+0")
        topframe=Frame(self.root,height=220 ,width=1400)
        topframe.pack(anchor="w")
        loimage=Image.open("lo.jpg")
        reimage1=loimage.resize((210,220))
        self.photo3=ImageTk.PhotoImage(reimage1)
        mujeem3= Label(topframe,image=self.photo3)
        mujeem3.place(x=0,y=0)
        image=Image.open("hotel3.jpg")
        reimage=image.resize((1170,310))
        self.photo=ImageTk.PhotoImage(reimage)
        mujeem= Label(topframe,image=self.photo)
        mujeem.place(x=200,y=0)
        headlabel=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",bg="black",fg="red",font=("times new roman", 30, "bold"))
        headlabel.place(x=0,y=221,width=1400,height=50)
        side_frame=Frame(self.root,height=650 ,width=210 ,border=1,relief="solid",padx="20",pady=20)
        side_frame.place(x=1,y=272)
        menu_label=Label(side_frame,text="MENU",bg="blue",fg="gold",font=("times new roman", 20, "bold"),bd=1 ,relief="solid")
        menu_label.place(x=-20,y=-20,width=220,height=50)
        custbtn=Button(side_frame,text="CUSTOMER",command=self.customer,bg="black",fg="gold",font=("times new roman", 20, "bold"),bd=1 ,relief="solid",cursor="hand2")
        custbtn.place(x=-20,y=31,width=220,height=50)
        roombtn=Button(side_frame,text="ROOM",bg="black",fg="gold",command=self.room,font=("times new roman", 20, "bold"),bd=1 ,relief="solid",cursor="hand2")
        roombtn.place(x=-20,y=82,width=220,height=50)
        detailbtn=Button(side_frame,text="DETAILS",bg="black",command=self.detail,fg="gold",font=("times new roman", 20, "bold"),bd=1 ,relief="solid",cursor="hand2")
        detailbtn.place(x=-20,y=133,width=220,height=50)
        logoutbtn=Button(side_frame,text="LOGOUT",bg="black",command=self.logout,fg="gold",font=("times new roman", 20, "bold"),bd=1 ,relief="solid",cursor="hand2")
        logoutbtn.place(x=-20,y=184,width=220,height=50)
        sd1image=Image.open("sideimg3.jpg")
        sreimage1=sd1image.resize((250,175))
        self.photo1=ImageTk.PhotoImage(sreimage1)
        mujeem= Label(side_frame,image=self.photo1)
        mujeem.place(x=-20,y=233)
        # sd2image=Image.open("sideimg3.jpg")
        # ssreimage1=sd2image.resize((350,145))
        # self.photo2=ImageTk.PhotoImage(ssreimage1)
        # mujeem2= Label(side_frame,image=self.photo2)
        # mujeem2.place(x=-20,y=452)
        sidelabel=Label(self.root,height=29,width=165,bd=2,relief="sunken")
        sidelabel.place(x=210,y=270) 
        simagee=Image.open("hotel1.jpg")
        reimage5=simagee.resize((1147,430))
        self.photo5=ImageTk.PhotoImage(reimage5)
        mujeem2= Label(sidelabel,image=self.photo5)
        mujeem2.place(x=0,y=0)
    def customer(self):
        self.newwindow=Toplevel(self.root)
        self.app=custwindow(self.newwindow)
    def room(self):
        self.newwindow=Toplevel(self.root)
        self.app=roombooking(self.newwindow)     
    def detail(self):
        self.newwindow=Toplevel(self.root)
        self.app=details(self.newwindow)  

    def logout(self):
        m=messagebox.askquestion("Logout Account","Do you want to Logout",parent=self.root)
        if(m=="yes"):
            self.root.destroy()
        else:
            return 

if __name__== "__main__":
    root=Tk()
    main=mainwindow(root)
    root.mainloop()
    