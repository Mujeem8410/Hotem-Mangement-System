from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
import mysql.connector as m
from tkinter import messagebox 
from  sinup import sinupwindow
from  forgett import forgetwindow
from  main import mainwindow
class loginwindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page For Hotel Management System")
        self.root.geometry("2100x1100+0+0")
        image=Image.open("m5.jpg")
        # image.resize((2100,800))
        self.photo=ImageTk.PhotoImage(image)
        mujeem= Label(self.root,image=self.photo)
        mujeem.place(x=0,y=0,relwidth=1,relheight=1)
        self.midframe=Frame(self.root,bd=2,relief="sunken",width=400,height=500 ,bg="snow2")
        self.midframe.place(x=480,y=100)
        self.login=Label(self.midframe,text="Login Page",bg="yellow",fg="red",font=("Comic Sans MS", 20, "bold"))
        self.login.place(x=100,y=50)
        image1=Image.open("download.jpg")
        img2=image1.resize((70,70))
        self.photo1=ImageTk.PhotoImage(img2)
        mujeem1= Label(self.midframe,image=self.photo1)
        mujeem1.place(x=150,y=120)
        self.user_name=Label(self.midframe,text="UserName",fg="black",font=("Comic Sans MS", 12, "bold"))
        self.user_name.place(x=15,y=250)
        self.user=StringVar()
        self.user_entry=ttk.Entry(self.midframe,textvariable=self.user,font=("Comic Sans MS", 12))
        self.user_entry.place(x=130,y=250)
        self.user_pass=Label(self.midframe,text="Password",fg="black",font=("Comic Sans MS", 12, "bold"))
        self.user_pass.place(x=15,y=300)
        self.passw=StringVar()
        self.user_pass=ttk.Entry(self.midframe,textvariable=self.passw,font=("Comic Sans MS", 12),show="*")
        self.user_pass.place(x=130,y=300)
        self.forgbtn=Button(self.midframe,text="Forget Pass",command=self.forget,font=("Comic Sans MS", 10, "bold"),bg="black",fg="red",cursor="hand2")
        self.forgbtn.place(x=20,y=380)  
        self.sinup=Button(self.midframe,text="Sin Up",command=self.sinupp,font=("Comic Sans MS", 10, "bold"),bg="black",width=12,fg="red",cursor="hand2")
        self.sinup.place(x=130,y=380)
       
        def login():
            # print(f"The Username is {self.user.get()} and the Password is{self.user_pass.get()}")
          
            if self.user.get() =="":
                messagebox.showerror("Login","Please Enter User Name")
            elif self.user_pass.get() =="":
                messagebox.showerror("Login","Please Enter Password")
            else:
                conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                cursor=conn.cursor()
                query="select * from admin where username='{}' and password='{}'".format( self.user_entry.get(),self.user_pass.get())
                cursor.execute(query)
                record=cursor.fetchone()
                if record==None:
                    messagebox.showerror("Login","Sorry Invlid User ID and Password")
                else:
                    ydata=messagebox.askyesno("Login","Do you want to login",parent=self.root)
                    if(ydata>0):
                         self.newwindow=Toplevel(self.root)
                         self.app=mainwindow(self.newwindow)
                         self.user.set("")
                         self.passw.set("")
                    else:
                        return
      
                conn.close()
        self.loginbtn=Button(self.midframe,text="Login",font=("Comic Sans MS", 10, "bold"),bg="black",width=12,command=login,fg="red",cursor="hand2")
        self.loginbtn.place(x=260,y=380)
    def sinupp(self):
        self.newwindow=Toplevel(self.root)
        self.app=sinupwindow(self.newwindow)
    def forget(self):
        self.newwindow=Toplevel(self.root)
        self.app=forgetwindow(self.newwindow)
                     
      
if __name__== "__main__":
    root=Tk()
    main=loginwindow(root)
    root.mainloop()
    
 