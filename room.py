from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
import mysql.connector as m
from tkinter import messagebox
import random 
from mysql.connector import Error
from time import strftime
from datetime import datetime
import details
from tkcalendar import Calendar
class roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Window For Hotel Management System")
        self.root.geometry("1150x440+206+297")
        headlabel=Label(self.root,text="ROOM BOOING DETAILS",bg="black",fg="red",font=("times new roman", 20, "bold"))
        self.var_contact=StringVar()
        self.var_check_in_date=StringVar()
        self.var_check_out_date=StringVar()
        self.var_room_type=StringVar()
        self.var_avlroom=StringVar()
        self.var_meal=StringVar()
        self.var_tex=StringVar()
        self.var_no_of_days=StringVar()
        self.var_sub_total=StringVar()
        self.var_total_cost=StringVar()
        self.cal=StringVar()
        self.cal=None

        headlabel.place(x=0,y=0,width=1150,height=50)
        loimage=Image.open("lo.jpg")
        reimage1=loimage.resize((60,48))
        self.photo3=ImageTk.PhotoImage(reimage1)
        mujeem3= Label(self.root,image=self.photo3)
        mujeem3.place(x=0,y=0)
        labelleft=LabelFrame(self.root,bd=1,text="Roombooking Details",font=("times new roman", 15, "bold"))
        labelleft.place(x=0,y=50,height=350,width=400)
        contact_cust=Label(labelleft,text="Customer Contact:",font=("times new roman", 10, "bold"),padx=5,pady=5)
        contact_cust.grid(row=0,column=0,sticky="w")
        conatct_entry=ttk.Entry(labelleft,width="20",textvariable=self.var_contact,font=("times new roman", 10, "bold"))
        conatct_entry.grid(row=0,column=1,padx=10,sticky="w")
        fetch_data_btn=Button(labelleft,command=self.fetch,font=("times new roman", 11, "bold"),width=9,text="Fetch Data",bg="black",fg="gold")
        fetch_data_btn.place(x=290,y=-1)
        check_date=Label(labelleft,text="Check_in_date:",font=("times new roman", 10, "bold"),padx=5,pady=5)
        check_date.grid(row=1,column=0,sticky="w")
        check_entry=ttk.Entry(labelleft,width="20",textvariable=self.var_check_in_date,font=("times new roman", 10, "bold"))
        check_entry.grid(row=1,column=1,padx=10,sticky="w")
        in_btn=Button(labelleft,font=("times new roman", 10, "bold"),command=self.indate,width=5,text="indate",height=1,bg="black",fg="gold")
        in_btn.place(x=290,y=30)
        show_btn=Button(labelleft,font=("times new roman", 10, "bold"),command=self.show,width=5,text="show",height=1,bg="black",fg="gold")
        show_btn.place(x=336,y=30)
        check_out_date=Label(labelleft,text="Check_out_date:",font=("times new roman", 10, "bold"),padx=5,pady=5)
        check_out_date.grid(row=2,column=0,sticky="w")
        check_out_entry=ttk.Entry(labelleft,width="20",textvariable=self.var_check_out_date,font=("times new roman", 10, "bold"))
        check_out_entry.grid(row=2,column=1,padx=10,sticky="w")
        out_btn=Button(labelleft,font=("times new roman", 10, "bold"),command=self.outdate,width=5,text="utdate",height=1,bg="black",fg="gold")
        out_btn.place(x=290,y=58)
        dest_btn=Button(labelleft,font=("times new roman", 10, "bold"),command=self.dest,width=5,text="hide",height=1,bg="black",fg="gold")
        dest_btn.place(x=336,y=58)
        rtype=Label(labelleft,text="Room Type:",font=("times new roman", 10, "bold"),padx=5,pady=5)
        rtype.grid(row=3,column=0,sticky="w")
        conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
        cursor=conn.cursor()
        cursor.execute("select Room_Type from details")
        id=cursor.fetchall()
        rtype_combo=ttk.Combobox(labelleft,font=("times new roman", 10, "bold"),textvariable=self.var_room_type,width=18,state="readonly")
        rtype_combo["value"]=id
        rtype_combo.current(0)
        rtype_combo.place(x=128,y=88)
        avlroom=Label(labelleft,text="Availabel Room:",font=("times new roman", 10, "bold"),padx=5,pady=5)
        avlroom.grid(row=4,column=0,sticky="w")
        conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
        cursor=conn.cursor()
        cursor.execute("select Room_No from details")
        row=cursor.fetchall()
        avg_combo=ttk.Combobox(labelleft,font=("times new roman", 10, "bold"),textvariable=self.var_avlroom,width=18,state="readonly")
        avg_combo["value"]=row
        avg_combo.current(0)
        avg_combo.place(x=128,y=118)
        # avlroom_entry=ttk.Entry(labelleft,width="30",textvariable=self.var_avlroom,font=("times new roman", 10, "bold"))
        # avlroom_entry.grid(row=4,column=1,padx=10)
        meal=Label(labelleft,text="Meal:",font=("times new roman", 10, "bold"),padx=5,pady=5)
        meal.grid(row=5,column=0,sticky="w")
        meal_entry=ttk.Entry(labelleft,width=20,textvariable=self.var_meal,font=("times new roman", 10, "bold"))
        meal_entry.place(x=128,y=144)
        No_days=Label(labelleft,text="No of Days:",font=("times new roman", 10, "bold"),padx=5,pady=5)
        No_days.grid(row=6,column=0,sticky="w")
        No_days_entry=ttk.Entry(labelleft,width=20,textvariable=self.var_no_of_days,font=("times new roman", 10, "bold"))
        No_days_entry.place(x=128,y=171)
        tex=Label(labelleft,text="Paid Tax:",font=("times new roman", 10, "bold"),padx=5,pady=5)
        tex.grid(row=7,column=0,sticky="w")
        tex_entry=ttk.Entry(labelleft,width=20,textvariable=self.var_tex,font=("times new roman", 10, "bold"))
        tex_entry.place(x=128,y=201)
        Sub_Total=Label(labelleft,text="Sub Total:",font=("times new roman", 10, "bold"),padx=5,pady=5)
        Sub_Total.grid(row=8,column=0,sticky="w")
        sub_entry=ttk.Entry(labelleft,width=20,textvariable=self.var_sub_total,font=("times new roman", 10, "bold"))
        sub_entry.place(x=128,y=232)
        Total_cost=Label(labelleft,text="Total cost:",font=("times new roman", 10, "bold"),padx=5,pady=5)
        Total_cost.grid(row=9,column=0,sticky="w")
        total_entry=ttk.Entry(labelleft,width=20,textvariable=self.var_total_cost,font=("times new roman", 10, "bold"))
        total_entry.place(x=128,y=260)
        billbtn=Button(labelleft,font=("times new roman", 11, "bold"),command=self.total,width=7,text="Bill",bg="black",fg="gold")
        billbtn.place(x=10,y=290)
        
        btn_frame=Frame(labelleft,bd=1,relief="sunken")
        btn_frame.place(x=90,y=290,width=290,height=35)
        savebtn=Button(btn_frame,font=("times new roman", 11, "bold"),command=self.add_details,width=7,text="Save",bg="black",fg="gold")
        savebtn.grid(row=0,column=0)
        Updatebtn=Button(btn_frame,font=("times new roman", 11, "bold"),command=self.update,width=7,text="Update",bg="black",fg="gold")
        Updatebtn.grid(row=0,column=1,padx=2)
        Deletebtn=Button(btn_frame,font=("times new roman", 11, "bold"),command=self.delete,width=7,text="Delete",bg="black",fg="gold")
        Deletebtn.grid(row=0,column=2)
        Resetbtn=Button(btn_frame,font=("times new roman", 11, "bold"),command=self.reset,width=7,text="Reset",bg="black",fg="gold")
        Resetbtn.grid(row=0,column=3,padx=2)
        image=Image.open("new11.jpg")
        reimage2=image.resize((680,192))
        self.photo4=ImageTk.PhotoImage(reimage2)
        mujeem4= Label(self.root,image=self.photo4,bd=1, highlightbackground="black")
        mujeem4.place(x=657,y=50)
        rightlbl=LabelFrame(self.root,bd=2,text="Search and view Details",font=("times new roman", 14, "bold"))
        rightlbl.place(x=405,y=238,height=170,width=750)
        search_By=Label(rightlbl,text="Search By:",font=("times new roman", 12, "bold") ,bg="red",fg="black")
        search_By.place(x=0,y=0)
        self.combo_var=StringVar()
        serach_combo=ttk.Combobox(rightlbl,font=("times new roman", 11, "bold"),textvariable=self.combo_var,width=15,state="readonly")
        serach_combo["value"]=("Contact","Room_No.")
        serach_combo.current(0)
        serach_combo.place(x=95,y=0)
        self.text_var=StringVar()
        number_entry=ttk.Entry(rightlbl,width=20,textvariable=self.text_var,font=("times new roman", 11, "bold"))
        number_entry.place(x=250,y=0)
        searchbtn=Button(rightlbl,font=("times new roman", 10, "bold"),width=9,command=self.search,text="Search",bg="black",fg="gold")
        searchbtn.place(x=440,y=0)
        showallbtn=Button(rightlbl,font=("times new roman", 10, "bold"),command=self.fetch_data,width=9,text="Show all",bg="black",fg="gold")
        showallbtn.place(x=520,y=0)
        table_frame=Frame(rightlbl,bd=3,relief="sunken")
        table_frame.place(x=6,y=30,width=740,height=112) 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.room_details=ttk.Treeview(table_frame,columns=("Contact","Check_in_date","Check_out_date","Room_type","Room_No.","Meal","No_of_days","Sub_total","Total_cost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM ,fill="x")
        scroll_y.pack(side=RIGHT ,fill="y")
        scroll_x.config(command=self.room_details.xview)
        scroll_y.config(command=self.room_details.yview)

        self.room_details.heading("Contact",text="Contact")
        self.room_details.heading("Check_in_date",text="Check_in_date")
      
        self.room_details.heading("Check_out_date",text="Check_out_date")
        self.room_details.heading("Room_type",text="Room_type")
        self.room_details.heading("Room_No.",text="Room_No.")
        self.room_details.heading("Meal",text="Meal")
        self.room_details.heading("No_of_days",text="No_of_days")
        self.room_details.heading("Sub_total",text="Sub_total")
        self.room_details.heading("Total_cost",text="Total_cost")
        
        self.room_details["show"]="headings" 

        self.room_details.column("Contact",width=140)
        self.room_details.column("Check_in_date",width=140)
        self.room_details.column("Check_out_date",width=140)
        self.room_details.column("Room_type",width=140)
        self.room_details.column("Room_No.",width=140)
        self.room_details.column("Meal",width=140)
        self.room_details.column("No_of_days",width=140)
        self.room_details.column("Sub_total",width=140)
        self.room_details.column("Total_cost",width=140)
        self.fetch_data()
        self.room_details.pack(fill=BOTH,expand=1)
        self.fetch_data()

        self.room_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
      
        # cal.destroy() 

    def fetch(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
              conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
              cursor=conn.cursor()
              query="SELECT `Customer Name` FROM customer  WHERE `Mobile Number`= %s"
              value=(self.var_contact.get(),)
              cursor.execute(query,value)
              row=cursor.fetchone()
             
              if row==None:
                  messagebox.showerror("Error","Please Enter Valid Conatct Number",parent=self.root)
              else:
                  conn.commit()
                  conn.close()  
                  dataframe=Frame(self.root,bd=2,relief="sunken",width=250,height=184)
                  dataframe.place(x=405, y=51)  
                  lb1=Label(dataframe,text="Name: ",font=("times new roman", 13, "bold"))    
                  lb1.place(x=0,y=0)   
                  lb2=Label(dataframe,text=row,font=("times new roman", 13, "bold"))    
                  lb2.place(x=60,y=0)  
                  lb3=Label(dataframe,text="Gender:  ",font=("times new roman", 13, "bold"))    
                  lb3.place(x=0,y=47)
                  lb17=Label(dataframe,text="Ref.No: ",font=("times new roman", 13, "bold"))    
                  lb17.place(x=0,y=23)    
                  conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                  cursor=conn.cursor()
                  query="SELECT `Ref.No` FROM customer  WHERE `Mobile Number`= %s"
                  value=(self.var_contact.get(),)
                  cursor.execute(query,value)
                  row=cursor.fetchone()
                  lb40=Label(dataframe,text=row,font=("times new roman", 13, "bold"))    
                  lb40.place(x=62,y=23)

             
                  conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                  cursor=conn.cursor()
                  query="SELECT `Gender` FROM customer  WHERE `Mobile Number`= %s"
                  value=(self.var_contact.get(),)
                  cursor.execute(query,value)
                  row=cursor.fetchone()
                  lb4=Label(dataframe,text=row,font=("times new roman", 13, "bold"))    
                  lb4.place(x=65,y=47)
                  lb5=Label(dataframe,text="Email: ",font=("times new roman", 13, "bold"))    
                  lb5.place(x=0,y=69)
                  

             
                  conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                  cursor=conn.cursor()
                  query="SELECT `Email` FROM customer  WHERE `Mobile Number`= %s"
                  value=(self.var_contact.get(),)
                  cursor.execute(query,value)
                  row=cursor.fetchone()
                  lb6=Label(dataframe,text=row,font=("times new roman", 13, "bold"))    
                  lb6.place(x=63,y=69)
                  lb7=Label(dataframe,text="Nationality :",font=("times new roman", 13, "bold"))    
                  lb7.place(x=0,y=90)

             
                  conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                  cursor=conn.cursor()
                  query="SELECT `Nationality` FROM customer  WHERE `Mobile Number`= %s"
                  value=(self.var_contact.get(),)
                  cursor.execute(query,value)
                  row=cursor.fetchone()
                  lb8=Label(dataframe,text=row,font=("times new roman", 13, "bold"))    
                  lb8.place(x=108,y=90)
                  lb9=Label(dataframe,text="Address :",font=("times new roman", 13, "bold"))    
                  lb9.place(x=0,y=111)

             
                  conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                  cursor=conn.cursor()
                  query="SELECT `Address` FROM customer  WHERE `Mobile Number`= %s"
                  value=(self.var_contact.get(),)
                  cursor.execute(query,value)
                  row=cursor.fetchone()
                  lb10=Label(dataframe,text=row,font=("times new roman", 14, "bold"))    
                  lb10.place(x=100,y=111)
                  lb12=Label(dataframe,text="Id Number :",font=("times new roman", 13, "bold"))    
                  lb12.place(x=0,y=133)

             
                  conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                  cursor=conn.cursor()
                  query="SELECT `Id Number` FROM customer  WHERE `Mobile Number`= %s"
                  value=(self.var_contact.get(),)
                  cursor.execute(query,value)
                  row=cursor.fetchone()
                  lb13=Label(dataframe,text=row,font=("times new roman", 13, "bold"))    
                  lb13.place(x=105,y=133) 
                  lb126=Label(dataframe,text="Post Code :",font=("times new roman", 13, "bold"))    
                  lb126.place(x=0,y=155)

             
                  conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                  cursor=conn.cursor()
                  query="SELECT `Post Code` FROM customer  WHERE `Mobile Number`= %s"
                  value=(self.var_contact.get(),)
                  cursor.execute(query,value)
                  row=cursor.fetchone()
                  lb13=Label(dataframe,text=row,font=("times new roman", 13, "bold"))    
                  lb13.place(x=105,y=155) 
    def add_details(self):
        if self.var_contact.get() == "" or self.var_check_in_date.get() == "" or self.var_room_type.get() == "":
            messagebox.showerror("Error", "Please fill required fields", parent=self.root)
        else:
            conn = m.connect(host="localhost", user="root", password="ms8410", database="hotel_management")
            cursor = conn.cursor()
        
            query = "SELECT `Mobile Number` FROM customer WHERE `Mobile Number` = %s"
            value = (self.var_contact.get(),)
            cursor.execute(query, value)
            row = cursor.fetchone()
        
        if row is not None and int(row[0]) == int(self.var_contact.get()):
            try:
                cursor.execute("INSERT INTO room2 VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)", (
                    self.var_contact.get(), self.var_check_in_date.get(), self.var_check_out_date.get(),
                    self.var_room_type.get(), self.var_avlroom.get(), self.var_meal.get(), self.var_no_of_days.get()
                ,self.var_sub_total.get(),self.var_total_cost.get()))
                messagebox.showinfo("Success", "Room has been booked successfully", parent=self.root)
                conn.commit()
                conn.close()
                self.fetch_data()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
        else:
            messagebox.showerror("Error", "Non Regested Mobile Number", parent=self.root)
        
        conn.close()             

    
         
    def delete(self):
               self.fetch_data()
               mdelete = messagebox.askyesno("Hotel Management System", "Do you want to Delete this Booking Details", parent=self.root)
               if mdelete:
                    conn = m.connect(host="localhost", user="root", password="ms8410", database="hotel_management")
                    cursor = conn.cursor()
                    query = "DELETE FROM room2 WHERE `Room_No.`=%s"
                    value = (self.var_avlroom.get(),)
                    cursor.execute(query, value)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                   
               else:
                    return
               self.fetch_data()
       
                           
    def fetch_data(self):
               conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
               cursor=conn.cursor()
               cursor.execute("select * from room2")
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
         self.var_contact.set(row[0])
         self.var_check_in_date.set(row[1])
         self.var_check_out_date.set(row[2])
         self.var_room_type.set(row[3])
         self.var_avlroom.set(row[4])
         self.var_meal.set(row[5])
         self.var_no_of_days.set(row[6])
      
    
   
                 
    def reset(self):
       self.var_check_in_date.set(""),
       self.var_check_out_date.set(""),
       self.var_room_type.set(""),
       self.var_avlroom.set(""),
       self.var_meal.set(""),
       self.var_no_of_days.set(""),
       self.var_contact.set("")
       self.var_tex.set(""),
       self.var_sub_total.set(""),
       self.var_total_cost.set("")
    def update(self):
            
              if self.var_contact.get()=="" or self.var_room_type.get()=="" or  self.var_check_in_date.get()=="":
                     messagebox.showerror("Error","Please fill required field",parent=self.root)
                       
              else:
                  conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                  cursor=conn.cursor()
                  cursor.execute("""
    UPDATE room2 
    SET  `Check_in_date` = %s,
        Check_out_date = %s,
        `Room_type` = %s,
        `Room_No.` = %s,
        Meal = %s,
        No_of_days = %s,
        Sub_total=%s,
        total_cost=%s                                                         
    WHERE `Contact` = %s
""", (
  
    self.var_check_in_date.get(),
    self.var_check_out_date.get(),
    self.var_room_type.get(),
    self.var_avlroom.get(),
    self.var_meal.get(),
    self.var_no_of_days.get(),
    self.var_sub_total.get(),
    self.var_total_cost.get(),
    self.var_contact.get()
))  
                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  messagebox.showinfo("Update","Booking details Update successfully",parent=self.root)
    def total(self):
         indate=self.var_check_in_date.get()
         outdate=self.var_check_out_date.get()
         indate = datetime.strptime(indate, '%d-%m-%Y')
         outdate = datetime.strptime(outdate, '%d-%m-%Y') 
         self.var_no_of_days.set(abs(outdate-indate).days)
         if(self.var_meal.get()=="BreakFast" and self.var_room_type.get()=="Luxury"):
              q1=float(300)
              q2=float(700)
              q3=float(self.var_no_of_days.get())
              q4=float(q1+q2)
              q5=float(q3+q4)
              tax="Rs."+str("%.2f"%((q5)*0.1))
              st="Rs."+str("%.2f"%((q5)))
              tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
              self.var_tex.set(tax)
              self.var_sub_total.set(st)
              self.var_total_cost.set(tt)
         elif(self.var_meal.get()=="BreakFast" and self.var_room_type.get()=="Single"):
              q1=float(200)
              q2=float(500)
              q3=float(self.var_no_of_days.get())
              q4=float(q1+q2)
              q5=float(q3+q4)
              tax="Rs."+str("%.2f"%((q5)*0.1))
              st="Rs."+str("%.2f"%((q5)))
              tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
              self.var_tex.set(tax)
              self.var_sub_total.set(st)
              self.var_total_cost.set(tt)
         elif(self.var_meal.get()=="BreakFast" and self.var_room_type.get()=="Double"):
              q1=float(250)
              q2=float(600)
              q3=float(self.var_no_of_days.get())
              q4=float(q1+q2)
              q5=float(q3+q4)
              tax="Rs."+str("%.2f"%((q5)*0.1))
              st="Rs."+str("%.2f"%((q5)))
              tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
              self.var_tex.set(tax)
              self.var_sub_total.set(st)
              self.var_total_cost.set(tt)
         elif(self.var_meal.get()=="Launch" and self.var_room_type.get()=="Single"):
              q1=float(400)
              q2=float(800)
              q3=float(self.var_no_of_days.get())
              q4=float(q1+q2)
              q5=float(q3+q4)
              tax="Rs."+str("%.2f"%((q5)*0.1))
              st="Rs."+str("%.2f"%((q5)))
              tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
              self.var_tex.set(tax)
              self.var_sub_total.set(st)
              self.var_total_cost.set(tt)
         elif(self.var_meal.get()=="Launch" and self.var_room_type.get()=="Double"):
              q1=float(500)
              q2=float(1000)
              q3=float(self.var_no_of_days.get())
              q4=float(q1+q2)
              q5=float(q3+q4)
              tax="Rs."+str("%.2f"%((q5)*0.1))
              st="Rs."+str("%.2f"%((q5)))
              tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
              self.var_tex.set(tax)
              self.var_sub_total.set(st)
              self.var_total_cost.set(tt)
         elif(self.var_meal.get()=="Launch" and self.var_room_type.get()=="Luxury"):
              q1=float(700)
              q2=float(1500)
              q3=float(self.var_no_of_days.get())
              q4=float(q1+q2)
              q5=float(q3+q4)
              tax="Rs."+str("%.2f"%((q5)*0.1))
              st="Rs."+str("%.2f"%((q5)))
              tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
              self.var_tex.set(tax)
              self.var_sub_total.set(st)
              self.var_total_cost.set(tt)
         elif(self.var_meal.get()=="Dinner" and self.var_room_type.get()=="Single"):
              q1=float(500)
              q2=float(700)
              q3=float(self.var_no_of_days.get())
              q4=float(q1+q2)
              q5=float(q3+q4)
              tax="Rs."+str("%.2f"%((q5)*0.1))
              st="Rs."+str("%.2f"%((q5)))
              tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
              self.var_tex.set(tax)
              self.var_sub_total.set(st)
              self.var_total_cost.set(tt)
         elif(self.var_meal.get()=="Dinner" and self.var_room_type.get()=="Double"):
              q1=float(700)
              q2=float(900)
              q3=float(self.var_no_of_days.get())
              q4=float(q1+q2)
              q5=float(q3+q4)
              tax="Rs."+str("%.2f"%((q5)*0.1))
              st="Rs."+str("%.2f"%((q5)))
              tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
              self.var_tex.set(tax)
              self.var_sub_total.set(st)
              self.var_total_cost.set(tt)
         elif(self.var_meal.get()=="Dinner" and self.var_room_type.get()=="Luxury"):
              q1=float(1000)
              q2=float(2000)
              q3=float(self.var_no_of_days.get())
              q4=float(q1+q2)
              q5=float(q3+q4)
              tax="Rs."+str("%.2f"%((q5)*0.1))
              st="Rs."+str("%.2f"%((q5)))
              tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
              self.var_tex.set(tax)
              self.var_sub_total.set(st)
              self.var_total_cost.set(tt)
    def search(self):
        try:
            conn = m.connect(host="localhost", user="root", password="ms8410", database="hotel_management")
            cursor = conn.cursor()

            query = "SELECT * FROM room2 WHERE `{}` LIKE %s".format(self.combo_var.get())
            cursor.execute(query, ('%' + self.text_var.get() + '%',))
        
            rows = cursor.fetchall()
        
        
            if rows:
                self.room_details.delete(*self.room_details.get_children())
                for row in rows:
                     self.room_details.insert("", END, values=row)
                conn.commit()
        except m.Error as err:
            print("Error:", err)
        finally:
        
            if conn.is_connected():
                cursor.close()
                conn.close()
    def show(self):
            self.cal = Calendar(self.root, selectmode="day", date_pattern="dd-mm-yyyy",width=200,height=102)
            self.cal.place(x=405, y=51)

    def dest(self):
        if hasattr(self, 'cal'):  # Check if the 'cal' attribute exists
            self.cal.destroy() 
         
    def indate(self):
        if self.cal==None:
              messagebox.showwarning("Check In Date","Please Select the Check in_date From Calendar",parent=self.root)
        else:
            
            indate = self.cal.get_date()
            self.var_check_in_date.set(indate)
                
                

    def outdate(self):
       if self.cal==None:
              messagebox.showwarning("Check Out Date","Please Select the Check out_date From Calendar",parent=self.root)
       else:
           outdate = self.cal.get_date()
           self.var_check_out_date.set(outdate)
            
              
                
if __name__== "__main__":
    root=Tk()
    obj=roombooking(root)
    root.mainloop()