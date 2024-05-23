from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
import mysql.connector as m
from tkinter import messagebox 
class forgetwindow:
    def __init__(self,root):
        
        def forget():
          
            if self.user.get() =="" or self.mob.get()=="" or self.dob.get()=="" or self.newpass.get()=="":
                messagebox.showerror("Forget","Please Fill the required field",parent=self.root)
         
            else:
                conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                cursor=conn.cursor()
                query="select * from admin where username='{}'".format( self.user.get())
                cursor.execute(query)
                record=cursor.fetchone()    
                conn.close()
                if record==None:
                          messagebox.showerror("Forget","Please Enter the valid Usename",parent=self.root)
     
                elif str(self.dob.get())!=(record[2]):
                     
                     messagebox.showerror("Forget","Please Enter the valid Birth Date",parent=self.root)
                elif self.mob.get()!=record[3]:
                     messagebox.showerror("Forget","Please Enter the valid Mbile No",parent=self.root)
                else:
                       
                  conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                  cursor=conn.cursor()
                  query="update admin set password='{}' where username='{}'".format( self.newpass.get(),self.user.get())
                  cursor.execute(query)
                  messagebox.showinfo("Forget","Forget the Password Successfully",parent=self.root)
                  conn.commit()
                  conn.close()
                  self.root.destroy()
              
            
        self.root=root
        self.root.title("Forget Password window For Hotel Management System")
        self.root.geometry("2100x1100+0+0")
        image=Image.open("m1.jpg")
        img=image.resize((2500,1200))
        self.photo=ImageTk.PhotoImage(img)
        self.user=StringVar()
        self.dob=StringVar()
        self.mob=StringVar()
        self.newpass=StringVar()
        mujeem= Label(self.root,image=self.photo)
        mujeem.place(x=0,y=0,relwidth=1,relheight=1)
        main_label=Label(self.root,height=34,width=50,border=2,relief="sunken",bg="white")
        main_label.place(x=480,y=100)
        image1=Image.open("images (2).jpg")
        img2=image1.resize((70,70))
        self.photo1=ImageTk.PhotoImage(img2)
        mujeem1= Label(main_label,image=self.photo1)
        mujeem1.place(x=145,y=20)
        head_label=Label(main_label,text="Forget Password",fg="red",font=("Arial",20,"bold"))
        head_label.place(x=63,y=120)
        self.user_name=Label(main_label,text="UserName",fg="black",font=("Comic Sans MS", 12, "bold"))
        self.user_name.place(x=15,y=200)
 
        self.user_entry=ttk.Entry(main_label,textvariable=self.user,font=("Comic Sans MS", 12))
        self.user_entry.place(x=130,y=200)
        self.user_name=Label(main_label,text="Birth Date",fg="black",font=("Comic Sans MS", 12, "bold"))
        self.user_name.place(x=15,y=260)
        
        self.user_dob=ttk.Entry(main_label,textvariable=self.dob,font=("Comic Sans MS", 12))
        self.user_dob.place(x=130,y=260)
        self.user_name=Label(main_label,text="Moblie No.",fg="black",font=("Comic Sans MS", 12, "bold"))
        self.user_name.place(x=15,y=320)
        
        self.user_entry=ttk.Entry(main_label,textvariable=self.mob,font=("Comic Sans MS", 12))
        self.user_entry.place(x=130,y=320)
        self.user_name=Label(main_label,text="New Paswrd",fg="black",font=("Comic Sans MS", 12, "bold"))
        self.user_name.place(x=15,y=380)
     
        self.user_entry=ttk.Entry(main_label,textvariable=self.newpass,font=("Comic Sans MS", 12),show="*")
        self.user_entry.place(x=130,y=380)
        save_btn=Button(main_label,text="Save",bg="black",command=forget,foreground="red",width=10,font=("Comic Sans MS", 12, "bold"))
        save_btn.place(x=140,y=450)

        
if __name__== "__main__":
    root=Tk()
    main=forgetwindow(root)
    root.mainloop()