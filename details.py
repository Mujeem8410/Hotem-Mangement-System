from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
import mysql.connector as m
from tkinter import messagebox
import random 
from mysql.connector import Error
from time import strftime
from datetime import datetime
class details:
    def __init__(self,root):
        self.root=root
        self.root.title("Detail Window For Hotel Management System")
        self.root.geometry("1150x440+206+297")
        headlabel=Label(self.root,text="ROOM DETAILS",bg="black",fg="red",font=("times new roman", 25, "bold"))
        headlabel.place(x=0,y=0,width=1150,height=50)
        loimage=Image.open("lo.jpg")
        reimage1=loimage.resize((60,48))
        self.photo3=ImageTk.PhotoImage(reimage1)
        mujeem3= Label(self.root,image=self.photo3)
        mujeem3.place(x=0,y=0)
        labelleft=LabelFrame(self.root,bd="4",relief="sunken",text="New Room Add",font=("times new roman", 20, "bold"))
        labelleft.place(x=0,y=60,height=350,width=500)
        floor=Label(labelleft,text="Floor :",font=("times new roman", 17, "bold"),padx=50,pady=7)
        floor.grid(row=0,column=0,sticky="w")
        self.var_floor=StringVar()
        floor_entry=ttk.Entry(labelleft,width="20",textvariable=self.var_floor,font=("times new roman", 13, "bold"))
        floor_entry.grid(row=0,column=1,padx=0,sticky="w")
            
        self.var_room=StringVar()

        Room_No=Label(labelleft,text="Room No. :",font=("times new roman", 17, "bold"),padx=50,pady=7)
        Room_No.grid(row=1,column=0,sticky="w")
        Room_No_entry=ttk.Entry(labelleft,width="20",textvariable=self.var_room,font=("times new roman", 13, "bold"))
        Room_No_entry.grid(row=1,column=1,padx=0,sticky="w")


        self.var_roomtype=StringVar()
        Room_type=Label(labelleft,text="Room Type :",font=("times new roman", 17, "bold"),padx=50,pady=7)
        Room_type.grid(row=2,column=0,sticky="w")
        Room_type_entry=ttk.Entry(labelleft,width="20",textvariable=self.var_roomtype,font=("times new roman", 13, "bold"))
        Room_type_entry.grid(row=2,column=1,padx=0,sticky="w")
        
        btn_frame=Frame(labelleft,bd=3,relief="sunken")
        btn_frame.place(x=70,y=200,width=300,height=40)
        savebtn=Button(btn_frame,font=("times new roman", 12, "bold"),command=self.add_details,width=7,text="Save",bg="black",fg="gold")
        savebtn.grid(row=0,column=0)
        Updatebtn=Button(btn_frame,font=("times new roman", 12, "bold"),command=self.update,width=7,text="Update",bg="black",fg="gold")
        Updatebtn.grid(row=0,column=1,padx=2)
        Deletebtn=Button(btn_frame,font=("times new roman", 12, "bold"),command=self.delete,width=7,text="Delete",bg="black",fg="gold")
        Deletebtn.grid(row=0,column=2)
        Resetbtn=Button(btn_frame,font=("times new roman", 12, "bold"),command=self.reset,width=7,text="Reset",bg="black",fg="gold")
        Resetbtn.grid(row=0,column=3,padx=2)

        rightlbl=LabelFrame(self.root,bd=4,relief="sunken",text="Show Room Details",font=("times new roman", 20, "bold"))
        rightlbl.place(x=515,y=60,height=340,width=620)
        scroll_x=ttk.Scrollbar(rightlbl,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(rightlbl,orient=VERTICAL)
        self.room_details=ttk.Treeview(rightlbl,columns=("Floor","Room_No","Room_Type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM ,fill="x")
        scroll_y.pack(side=RIGHT ,fill="y")
        scroll_x.config(command=self.room_details.xview)
        scroll_y.config(command=self.room_details.yview)
        
        self.room_details.heading("Floor",text="Floor")
        self.room_details.heading("Room_No",text="Room_No")
      
        self.room_details.heading("Room_Type",text="Room_Type")
     
        
        
        self.room_details["show"]="headings" 

        self.room_details.column("Floor",width=140)
        self.room_details.column("Room_No",width=140)
        self.room_details.column("Room_Type",width=140)
       
        
        self.room_details.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.room_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_details(self):
        if self.var_floor.get()=="" or self.var_room.get()=="" or  self.var_roomtype.get()=="":
            messagebox.showerror("Error","Please fill required field",parent=self.root)
        else:
              try:
               conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
               cursor=conn.cursor()
               cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(),self.var_room.get(),self.var_roomtype.get()))
               messagebox.showinfo("Successfully","Room has been added Successfully",parent=self.root)
               conn.commit()
               self.fetch_data()
               conn.close()
              except Exception as es:
                 messagebox.showwarning("Warning",f"Somerthing went wrong{str(es)}",parent=self.root)

    def fetch_data(self):
               conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
               cursor=conn.cursor()
               cursor.execute("select  * from details")
               row=cursor.fetchall()
               if len(row)!=0:
                    self.room_details.delete(*self.room_details.get_children())
                    for i in row:
                         self.room_details.insert("",END,values=i)
                         conn.commit()
               conn.close()
    def get_cursor(self,event=""):
         cursor_row=self.room_details.focus()
         content=self.room_details.item(cursor_row)
         row=content["values"]
         self.var_floor.set(row[0])
         self.var_room.set(row[1])
         self.var_roomtype.set(row[2])
    def delete(self):
               mdelete = messagebox.askyesno("Hotel Management System", "Do you want to Delete this Room Details", parent=self.root)
               if mdelete:
                    conn = m.connect(host="localhost", user="root", password="ms8410", database="hotel_management")
                    cursor = conn.cursor()
                    query = "DELETE FROM details WHERE `Room_No`=%s"
                    value = (self.var_room.get(),)
                    cursor.execute(query, value)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
               else:
                    return
    def update(self):
              if self.var_floor.get()=="" or self.var_room.get()=="" or  self.var_roomtype.get()=="":
                     messagebox.showerror("Error","Please fill required field",parent=self.root)
                       
              else:
                  conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                  cursor=conn.cursor()
                  cursor.execute("update details set `Floor`= %s,`Room_Type`= %s where `Room_No` = %s",(self.var_floor.get(),self.var_roomtype.get(), self.var_room.get()))  
                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  messagebox.showinfo("Update","Room details Update successfully",parent=self.root)


                
    def reset(self):
         self.var_floor.set("")
         self.var_room.set("")
         self.var_roomtype.set("")


if __name__== "__main__":
    root=Tk()
    obj=details(root)
    root.mainloop()