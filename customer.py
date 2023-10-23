from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkcalendar import *
import qrcode
from resizeimage import resizeimage
import pymysql

class customersClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Manage Customers")
        self.root.config(bg="white")
        self.root.focus_force()

        #Variable Declartion
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_cid=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_a_cus=StringVar()
        self.var_contact=StringVar()
        self.var_address=StringVar()

        #Search Frame
        SearchFrame=LabelFrame(self.root,text="Search Customers",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #Options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Cusid","Name","Contact","Email"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        #Search Entry Label
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("times new roman",15),bg="lightyellow")
        txt_search.place(x=200,y=10)

        #btn Search
        # btn_search=Entry(SearchFrame,font=("times new roman",15),bg="lightyellow")
        # btn_search.place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("times new roman",15),bg="#4caf50",fg="white",cursor="hand2")
        btn_search.place(x=410,y=9,width=150,height=30)

        #title
        title=Label(self.root,text="Customer Details",font=("times new roman",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

        #content
        #row1
        lbl_cid=Label(self.root,text="C ID",font=("times new roman",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("times new roman",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=750,y=150)

        txt_cid=Entry(self.root,text="Cus ID",textvariable=self.var_cid,font=("times new roman",15),bg="light yellow")
        txt_cid.place(x=150,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,text="Gender",textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)

        txt_contact=Entry(self.root,text="Contact+",textvariable=self.var_contact,font=("times new roman",15),bg="light yellow")
        txt_contact.place(x=850,y=150,width=180)

        #row2
        lbl_name=Label(self.root,text="Name",font=("times new roman",15),bg="white").place(x=50,y=190)
        txt_name=Entry(self.root,text="Name",textvariable=self.var_name,font=("times new roman",15),bg="light yellow")
        txt_name.place(x=150,y=190,width=180)
        
        
        #row3
        lbl_email=Label(self.root,text="Email",font=("times new roman",15),bg="white").place(x=50,y=230)
        txt_email=Entry(self.root,text="Email",textvariable=self.var_email,font=("times new roman",15),bg="light yellow")
        txt_email.place(x=150,y=230,width=180)
        
        #row4
        lbl_address=Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=50,y=270)
        self.txt_address=Text(self.root,font=("times new roman",15),bg="light yellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        
        
        #btns
        btn_add=Button(self.root,text="Save",command=self.add,font=("times new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("times new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)
        
        #Customer Details
        cus_frame=Frame(self.root,bd=3,relief=RIDGE)
        cus_frame.place(x=0,y=350,width=1000,height=350)

        scrolly=Scrollbar(cus_frame,orient=VERTICAL)
        scrollx=Scrollbar(cus_frame,orient=HORIZONTAL)

        self.CustomerTable=ttk.Treeview(cus_frame,columns=("cusid","cid","name","email","gender","contact","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CustomerTable.xview)
        scrolly.config(command=self.CustomerTable.yview)

        self.CustomerTable.heading("cusid",text="cusid")
        self.CustomerTable.heading("cid",text="Cid")
        self.CustomerTable.heading("name",text="Name")
        self.CustomerTable.heading("email",text="Email")
        self.CustomerTable.heading("gender",text="Gender")
        self.CustomerTable.heading("contact",text="Contact")
        self.CustomerTable.heading("address",text="Address")
       
        self.CustomerTable["show"]="headings"

        self.CustomerTable.column("cusid",width=200)
        self.CustomerTable.column("cid",width=200)
        self.CustomerTable.column("name",width=200)
        self.CustomerTable.column("email",width=200)
        self.CustomerTable.column("gender",width=200)
        self.CustomerTable.column("contact",width=200)
        self.CustomerTable.column("address",width=200)    
        self.CustomerTable.pack(fill=BOTH,expand=1)
        self.CustomerTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        #Footer
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed By SUBASHINI Student of CSE\n Adhiyamaan College Of Engineering(Autonomous),Hosur",font=("times new roman",12),bg="#010c48",fg="white").pack(side=BOTTOM,fill=X)
        
    #Function Calling
    def add(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        cur.execute(
                        "insert into customer (cid,name,email,gender,contact,address) values(%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_cid.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.txt_address.get("1.0", END),
                        ),
                   )
        con.commit()
        messagebox.showinfo(
                        "Success", "Customer Added Successfully", parent=self.root
                    )
        
        
    def show(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            cur.execute("Select * from customer")
            rows=cur.fetchall()
            self.CustomerTable.delete(*self.CustomerTable.get_children())
            for row in rows:
                self.CustomerTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    def get_data(self,ev):
        f=self.CustomerTable.focus()
        content=(self.CustomerTable.item(f))
        row=content['values']
        # print(row)
        self.var_cid.set(row[1])
        self.var_name.set(row[2])
        self.var_email.set(row[3])
        self.var_gender.set(row[4])
        self.var_contact.set(row[5])
        self.txt_address.delete("1.0",END),
        self.txt_address.insert(END,row[6]),
        
    def update(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.var_cid.get()=="":
                messagebox.showerror("Error","Customer ID must be Required",parent=self.root)
            else:
                cur.execute("Select * from customer where cid=%s",(self.var_cid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    cur.execute(
                            "UPDATE customer SET name=%s, email=%s, gender=%s, contact=%s, address=%s WHERE cid=%s",
                            (
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.txt_address.get("1.0", END),
                                self.var_cid.get()
                            )
                        )
                    con.commit()
                    messagebox.showinfo("Success", "Customer Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    def delete(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.var_cid.get()=="":
                messagebox.showerror("Error","Customer ID must be Required",parent=self.root)
            else:
                cur.execute("SELECT * FROM customer WHERE cid = %s", (self.var_cid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM customer WHERE id = %s", (self.var_cid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Customer Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    def clear(self):
        self.var_cid.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_contact.set("")
        self.txt_address.delete("1.0", END)
        #self.txt_address.insert("")
        self.var_searchtxt.get("")
        self.var_searchby.set("Select")
        self.show() 
        
    def search(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif  self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM customer WHERE " + self.var_searchby.get() + " LIKE %s", ('%' + self.var_searchtxt.get() + '%',))
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.CustomerTable.delete(*self.CustomerTable.get_children())
                    for row in rows:
                        self.CustomerTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 
    

        
if __name__=="__main__":
    root=Tk()
    obj=customersClass(root)
    root.mainloop()

