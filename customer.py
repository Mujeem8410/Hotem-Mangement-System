from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
import mysql.connector as m
from tkinter import messagebox
import random 
class custwindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer Window For Hotel Management System")
        self.root.geometry("1150x440+206+297")
        self.var_gender=StringVar()
        self.var_custname=StringVar()
        self.var_ref=StringVar()
        self.var_postcode=StringVar()
        self.var_mothername=StringVar()
        self.var_mobile=StringVar()
        self.var_idproof=StringVar()
        self.var_Idnumber=StringVar()
        self.var_addess=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        x=random.randint(1000,99999)
        self.var_ref.set(str(x))
 
        headlabel=Label(self.root,text="ADD CUSTOMER DETAILS",bg="black",fg="red",font=("times new roman", 25, "bold"))
        headlabel.place(x=0,y=0,width=1150,height=50)
        loimage=Image.open("lo.jpg")
        reimage1=loimage.resize((60,48))
        self.photo3=ImageTk.PhotoImage(reimage1)
        mujeem3= Label(self.root,image=self.photo3)
        mujeem3.place(x=0,y=0)
        labelleft=LabelFrame(self.root,bd="2",text="Customer Details",font=("times new roman", 15, "bold"))
        labelleft.place(x=0,y=50,height="400",width="330")
        lbl_cust_ref=Label(labelleft,text="Cust_Ref:",font=("times new roman", 10, "bold"),padx=3,pady=3)
        lbl_cust_ref.grid(row=0,column=0,sticky="w")
        custentry=ttk.Entry(labelleft,textvariable=self.var_ref,width="25",font=("times new roman", 10 ,"bold"),state="readonly")
        custentry.grid(row=0,column=1,padx=3)
        lbl_customer_name=Label(labelleft,text="Custome Name:",font=("times new roman", 10, "bold"),padx=3,pady=3)
        lbl_customer_name.grid(row=1,column=0,sticky="w")
        cust_name_entry=ttk.Entry(labelleft,textvariable=self.var_custname,width="25",font=("times new roman", 10, "bold"))
        cust_name_entry.grid(row=1,column=1,padx=3)
        lbl_mother_name=Label(labelleft,text="Mother Name:",font=("times new roman", 10, "bold"),padx=5,pady=5)
        lbl_mother_name.grid(row=2,column=0,sticky="w")
        cust_mname_entry=ttk.Entry(labelleft,textvariable=self.var_mothername,width="25",font=("times new roman", 10, "bold"))
        cust_mname_entry.grid(row=2,column=1,padx=3)
        Gender=Label(labelleft,text="Gender:",font=("times new roman", 10, "bold"),padx=3,pady=3)
        Gender.grid(row=3,column=0,sticky="w")
        gender_combo=ttk.Combobox(labelleft,textvariable=self.var_gender,font=("times new roman", 11, "bold"),width=20,state="readonly")
        gender_combo["value"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=1)
        Post_code=Label(labelleft,text="PostCode:",font=("times new roman", 10, "bold"),padx=3,pady=3)
        Post_code.grid(row=4,column=0,sticky="w")
        post_entry=ttk.Entry(labelleft,width="25",textvariable=self.var_postcode,font=("times new roman", 10, "bold"))
        post_entry.grid(row=4,column=1,padx=3)
        Mobile=Label(labelleft,text="Mobile:",font=("times new roman", 10, "bold"),padx=3,pady=3)
        Mobile.grid(row=5,column=0,sticky="w")
        Mobile_entry=ttk.Entry(labelleft,width="25",textvariable=self.var_mobile,font=("times new roman", 10, "bold"))
        Mobile_entry.grid(row=5,column=1,padx=3)
        Email=Label(labelleft,text="Email:",font=("times new roman", 10, "bold"),padx=3,pady=3)
        Email.grid(row=6,column=0,sticky="w")
        Email_entry=ttk.Entry(labelleft,width="25",textvariable=self.var_email,font=("times new roman", 10, "bold"))
        Email_entry.grid(row=6,column=1,padx=3)
        Nationality=Label(labelleft,text="Nationality:",font=("times new roman", 10, "bold"),padx=3,pady=3)
        Nationality.grid(row=7,column=0,sticky="w")
        nation_combo=ttk.Combobox(labelleft,textvariable=self.var_nationality,font=("times new roman", 11, "bold"),width=20,state="readonly")
        nation_combo["value"]=("India","America","Dubai")
        nation_combo.current(0)
        nation_combo.grid(row=7,column=1)
        Id_Proof_type=Label(labelleft,text="Id Proof type:",font=("times new roman", 10, "bold"),padx=3,pady=3)
        Id_Proof_type.grid(row=8,column=0,sticky="w")
        id_combo=ttk.Combobox(labelleft,textvariable=self.var_idproof,font=("times new roman", 11, "bold"),width=20,state="readonly")
        id_combo["value"]=("Aadhar","Passport","Driving Lineces","Identity card")
        id_combo.current(0)
        id_combo.grid(row=8,column=1)
        Id_number=Label(labelleft,text="Id Number:",font=("times new roman", 10, "bold"),padx=5,pady=5)
        Id_number.grid(row=9,column=0,sticky="w")
        Id_number_entry=ttk.Entry(labelleft,textvariable=self.var_Idnumber,width="25",font=("times new roman", 10, "bold"))
        Id_number_entry.grid(row=9,column=1,padx=3)

        Address=Label(labelleft,text="Address:",font=("times new roman", 10, "bold"),padx=3,pady=3)
        Address.grid(row=10,column=0,sticky="w")
        Address_entry=ttk.Entry(labelleft,width="25",textvariable=self.var_addess,font=("times new roman", 10, "bold"))
        Address_entry.grid(row=10,column=1,padx=3)
        btn_frame=Frame(labelleft,bd=3,relief="sunken")
        btn_frame.place(x=30,y=288,width=269,height=32)
        savebtn=Button(btn_frame,font=("times new roman", 12, "bold"),command=self.add_details,width=6,text="Save",bg="black",fg="gold")
        savebtn.grid(row=0,column=0)
        Updatebtn=Button(btn_frame,font=("times new roman", 12, "bold"),command=self.update,width=6,text="Update",bg="black",fg="gold")
        Updatebtn.grid(row=0,column=1,padx=2)
        Deletebtn=Button(btn_frame,font=("times new roman", 12, "bold"),command=self.delete,width=6,text="Delete",bg="black",fg="gold")
        Deletebtn.grid(row=0,column=2)
        Resetbtn=Button(btn_frame,font=("times new roman", 12, "bold"),command=self.reset,width=6,text="Reset",bg="black",fg="gold")
        Resetbtn.grid(row=0,column=3,padx=2)
        rightlbl=LabelFrame(self.root,bd="2",text="Search and view Details",font=("times new roman", 15, "bold"))
        rightlbl.place(x=320,y=50,height=400,width=830)
        search_By=Label(rightlbl,text="Search By:",font=("times new roman", 12, "bold") ,bg="red",fg="black")
        search_By.grid(row=0,column=0,sticky="w",padx=3,pady=1)
        self.combo_var=StringVar()
        serach_combo=ttk.Combobox(rightlbl,font=("times new roman", 11, "bold"),textvariable=self.combo_var,width=20,state="readonly")
        serach_combo["value"]=("Mobile Number","Ref.No")
        serach_combo.current(0)
        serach_combo.grid(row=0,column=1,padx=3,pady=3)
        self.text_var=StringVar()
        number_entry=ttk.Entry(rightlbl,width="25",textvariable=self.text_var,font=("times new roman", 11, "bold"))
        number_entry.grid(row=0,column=2,padx=3,pady=3)
        searchbtn=Button(rightlbl,font=("times new roman", 10, "bold"),command=self.search,width=7,text="Search",bg="black",fg="gold")
        searchbtn.grid(row=0,column=3,padx=5,pady=5)
        showallbtn=Button(rightlbl,font=("times new roman", 10, "bold"),command=self.fetch_data,width=7,text="Show all",bg="black",fg="gold")
        showallbtn.grid(row=0,column=4,padx=3,pady=3)
        table_frame=Frame(rightlbl,bd=3,relief="sunken")
        table_frame.place(x=10,y=40,width=810,height=285)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.cust_details=ttk.Treeview(table_frame,columns=("Ref.No","Customer Name","Mother Name","Gender","Post Code","Mobile Number","Email","Nationality","ID Proof","Id Number","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM ,fill="x")
        scroll_y.pack(side=RIGHT ,fill="y")
        scroll_x.config(command=self.cust_details.xview)
        scroll_y.config(command=self.cust_details.yview)

        self.cust_details.heading("Ref.No",text="Ref.No")
        self.cust_details.heading("Customer Name",text="Customer Name")
        self.cust_details.heading("Mother Name",text="Mother Name")
        self.cust_details.heading("Gender",text="Gender")
        self.cust_details.heading("Post Code",text="Post Code")
        self.cust_details.heading("Mobile Number",text="Mobile Number")
        self.cust_details.heading("Email",text="Email")
        self.cust_details.heading("Nationality",text="Nationality")
        self.cust_details.heading("ID Proof",text="ID Proof")
        self.cust_details.heading("Id Number",text="Id Number")
        self.cust_details.heading("Address",text="Address")
        self.cust_details["show"]="headings" 

        self.cust_details.column("Ref.No",width=130)
        self.cust_details.column("Customer Name",width=130)
        self.cust_details.column("Mother Name",width=130)
        self.cust_details.column("Gender",width=130)
        self.cust_details.column("Post Code",width=130)
        self.cust_details.column("Mobile Number",width=130)
        self.cust_details.column("Email",width=130)
        self.cust_details.column("Nationality",width=130)
        self.cust_details.column("ID Proof",width=130)
        self.cust_details.column("Id Number",width=130)
        self.cust_details.column("Address",width=130)
        self.cust_details.pack(fill=BOTH,expand=1)
        self.cust_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_details(self):
        if self.var_custname.get()=="" or self.var_mothername.get()=="" or  self.var_Idnumber.get()=="":
            messagebox.showerror("Error","Please fill required field",parent=self.root)
        else:
              try:
               conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
               cursor=conn.cursor()
               cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.      var_custname.get(),self.var_mothername.get(),self.var_gender.get(),self.var_postcode.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_idproof.get(),self.var_Idnumber.get(),self.var_addess.get      ()))
               messagebox.showinfo("Successfully","Customer has been added",parent=self.root)
               conn.commit()
               self.fetch_data()
               conn.close()
              except Exception as es:
                 messagebox.showwarning("Warning",f"Somerthing went wrong{str(es)}",parent=self.root)
    def add_details(self):
        if self.var_custname.get()=="" or self.var_mothername.get()=="" or  self.var_Idnumber.get()=="":
            messagebox.showerror("Error","Please fill required field",parent=self.root)
        else:
              try:
               conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
               cursor=conn.cursor()
               cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.      var_custname.get(),self.var_mothername.get(),self.var_gender.get(),self.var_postcode.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_idproof.get(),self.var_Idnumber.get(),self.var_addess.get      ()))
               messagebox.showinfo("Successfully","Customer has been added",parent=self.root)
               conn.commit()
               self.fetch_data()
               conn.close()
              except Exception as es:
                 messagebox.showwarning("Warning",f"Somerthing went wrong{str(es)}",parent=self.root)
    def fetch_data(self):
               conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
               cursor=conn.cursor()
               cursor.execute("select  * from customer")
               row=cursor.fetchall()
               if len(row)!=0:
                    self.cust_details.delete(*self.cust_details.get_children())
                    for i in row:
                         self.cust_details.insert("",END,values=i)
                         conn.commit()
               conn.close()
    def get_cursor(self,event=""):
         cursor_row=self.cust_details.focus()
         content=self.cust_details.item(cursor_row)
         row=content["values"]
         self.var_ref.set(row[0])
         self.var_custname.set(row[1])
         self.var_mothername.set(row[2])
         self.var_gender.set(row[3])
         self.var_postcode.set(row[4])
         self.var_mobile.set(row[5])
         self.var_email.set(row[6])
         self.var_nationality.set(row[7])
         
         self.var_idproof.set(row[8])
         self.var_Idnumber.set(row[9])
         self.var_addess.set(row[10])
    def update(self):
              if self.var_custname.get()=="" or self.var_mothername.get()=="" or  self.var_Idnumber.get()=="":
                     messagebox.showerror("Error","Please fill required field",parent=self.root)
                       
              else:
                  conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                  cursor=conn.cursor()
                  cursor.execute("""
    UPDATE customer 
    SET `Customer Name` = %s,
        `Mother Name` = %s,
        Gender = %s,
        `Post Code` = %s,
        `Mobile Number` = %s,
        Email = %s,
        Nationality = %s,
        `ID Proof` = %s,
        `Id Number` = %s,
        Address = %s 
    WHERE `Ref.No` = %s
""", (
    self.var_custname.get(),
    self.var_mothername.get(),
    self.var_gender.get(),
    self.var_postcode.get(),
    self.var_mobile.get(),
    self.var_email.get(),
    self.var_nationality.get(),
    self.var_idproof.get(),
    self.var_Idnumber.get(),
    self.var_addess.get(),
    self.var_ref.get()
))  
                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  messagebox.showinfo("Update","Customer details Update successfully",parent=self.root)
    def delete(self):
         mdelete=messagebox.askyesno("Hotele  Management System","Do you want to Delete this customer",parent=self.root)
         if mdelete>0:
                conn=m.connect(host="localhost",user="root",password="ms8410",database="hotel_management")
                cursor=conn.cursor()
                query="DELETE FROM customer WHERE `Ref.No`=%s"
                value=(self.var_ref.get(),)
                cursor.execute(query,value)
                conn.commit()
                self.fetch_data()
                conn.close()  
         else:
              if not mdelete:
                   return
                 
    def reset(self):
         self.var_custname.set("")
         self.var_mothername.set("")
         self.var_postcode.set("")
         self.var_mobile.set("")
         self.var_email.set("")
         self.var_Idnumber.set("")
         self.var_addess.set("")
         x=random.randint(1000,99999)
         self.var_ref.set(str(x))
 

    def search(self):
        try:
            conn = m.connect(host="localhost", user="root", password="ms8410", database="hotel_management")
            cursor = conn.cursor()

            query = "SELECT * FROM customer WHERE `{}` LIKE %s".format(self.combo_var.get())
            cursor.execute(query, ('%' + self.text_var.get() + '%',))
        
            rows = cursor.fetchall()
        
        
            if rows:
                self.cust_details.delete(*self.cust_details.get_children())
                for row in rows:
                     self.cust_details.insert("", END, values=row)
                conn.commit()
        except m.Error as err:
            print("Error:", err)
        finally:
        
            if conn.is_connected():
                cursor.close()
                conn.close()     
if __name__== "__main__":
    root=Tk()
    obj=custwindow(root)
    root.mainloop()