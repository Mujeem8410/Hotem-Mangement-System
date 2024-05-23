from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
import mysql.connector as m
from tkinter import messagebox 
class sinupwindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Sin Up Page  For  Hotel Management System")
        self.root.geometry("2100x1100+0+0")
        image=Image.open("sin2 (1).jpg")
        name=StringVar()
        uname=StringVar()
        mob=StringVar()
        email=StringVar()
        dob=StringVar()
        favq=StringVar()
        passw=StringVar()
        def sinup():
            if name.get() ==""or uname.get()==""or mob.get()==""or email.get()==""or passw.get()==""or dob.get()=="":
                messagebox.showerror("Sinup","Please Fill the required field",parent=self.root)
        
            else:
                conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                cursor=conn.cursor()
                query="insert into admin(goodname,username,dob,mobile,email,password) values('{}','{}','{}','{}','{}','{}')".format(name.get(),uname.get(),dob.get(),mob.get(),email.get(),passw.get())
                cursor.execute(query)
                conn.commit()
                conn.close()
                messagebox.showinfo("Sinup","Create account Successfully")
                self.entryemail.delete(0,END)
                self.entryn.delete(0,END)
                self.entrydob.delete(0,END)
                self.entrymob.delete(0,END)
                self.entrypas.delete(0,END)
                self.entrypas.delete(0,END)
                self.root.destroy()
                
        
        self.photo=ImageTk.PhotoImage(image)
        mujeem= Label(self.root,image=self.photo)
        mujeem.place(x=0,y=0,relwidth=1,relheight=1)
        self.frame=Frame(self.root,height=520,width=1000,relief="sunken",bd=2)
        self.frame.place(x=180,y=100)
        self.img2=Image.open("mid.jpg")
        res=self.img2.resize((1200,600))
        self.photo2=ImageTk.PhotoImage(res)
        mujeem2=Label(self.frame,image=self.photo2)
        mujeem2.place(x=0,y=0)
        self.labelh=Label(self.frame,text="Create an Account",fg="red",font=("Comic Sans MS",20, "bold"))
        self.labelh.place(x=450,y=50)  
        self.label1=Label(self.frame,text=" Good Name",fg="red",font=("Comic Sans MS",10, "bold"),bd=2,bg="black")
        self.label1.place(x=50,y=150)
        self.entryn=ttk.Entry(self.frame ,textvariable=name,font=("Comic Sans MS", 12))
        self.entryn.place(x=160,y=150)
        self.label2=Label(self.frame,text="User Name",fg="red",font=("Comic Sans MS",10, "bold"),bd=2,bg="black")
        self.label2.place(x=500,y=150)
        self.entrylm=ttk.Entry(self.frame ,textvariable=uname,font=("Comic Sans MS", 12))
        self.entrylm.place(x=600,y=150)
        self.labeldob=Label(self.frame,text="Date of",fg="red",font=("Comic Sans MS",10, "bold"),bd=2,width=8,bg="black")
        self.labeldob.place(x=50,y=250)
        self.entrydob=ttk.Entry(self.frame ,textvariable=dob,font=("Comic Sans MS", 12))
        self.entrydob.place(x=160,y=250)
        self.labelmob=Label(self.frame,text="Mobile",fg="red",font=("Comic Sans MS",10, "bold"),bd=2,width=8,bg="black")
        self.labelmob.place(x=500,y=250)
        self.entrymob=ttk.Entry(self.frame ,textvariable=mob,font=("Comic Sans MS", 12))
        self.entrymob.place(x=600,y=250)
        self.labelemail=Label(self.frame,text="Email Add.",fg="red",font=("Comic Sans MS",10, "bold"),bd=2,width=8,bg="black")
        self.labelemail.place(x=50,y=350)
        self.entryemail=ttk.Entry(self.frame ,textvariable=email,font=("Comic Sans MS", 12))
        self.entryemail.place(x=160,y=350)
        self.labelpas=Label(self.frame,text="Password",fg="red",font=("Comic Sans MS",10, "bold"),bd=2,width=8,bg="black")
        self.labelpas.place(x=500,y=350)
        self.entrypas=ttk.Entry(self.frame ,textvariable=passw,font=("Comic Sans MS", 12),show="*")
        self.entrypas.place(x=600,y=350)
        btn1=Button(self.frame,text="Create",command=sinup,bg="black",fg="red",width=13,font=("Comic Sans MS",13, "bold"))
        btn1.place(x=400,y=450)
        

        
if __name__== "__main__":
    root=Tk()
    main=sinupwindow(root)
    root.mainloop()
