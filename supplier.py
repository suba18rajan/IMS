from tkinter import*
import tkinter
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkcalendar import *
import pymysql
#import sqlite3

class supplierClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Manage Suppliers")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #All Variables
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_supno=StringVar()
        self.var_invoice=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_address=StringVar()
        
        #Search Frame
        SearchFrame=LabelFrame(self.root,text="Search Suppliers",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=900,y=70,width=600,height=70)

        #Options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Supid","Name","Contact"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        #Search Entry Label
        
        # lbl_search=Label(SearchFrame,text="Search By Invoice No.",font=("times new roman",15),bg="white")
        # lbl_search.place(x=10,y=10)
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("times new roman",15),bg="lightyellow")
        txt_search.place(x=200,y=10)

        #btn Search
        # btn_search=Entry(SearchFrame,font=("times new roman",15),bg="lightyellow")
        # btn_search.place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("times new roman",15),bg="#4caf50",fg="white",cursor="hand2")
        btn_search.place(x=410,y=9,width=150,height=30)

        #title
        title=Label(self.root,text="Supplier Details",font=("times new roman",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)

        #content
        #row1
        lbl_supno=Label(self.root,text="Supplier No",font=("times new roman",15),bg="white").place(x=50,y=80)
        txt_supno=Entry(self.root,text="Supplier No",textvariable=self.var_supno,font=("times new roman",15),bg="light yellow")
        txt_supno.place(x=160,y=80,width=180)
        lbl_invoice=Label(self.root,text="Invoice No",font=("times new roman",15),bg="white").place(x=50,y=120)
        txt_invoice=Entry(self.root,text="Sup ID",textvariable=self.var_invoice,font=("times new roman",15),bg="light yellow")
        txt_invoice.place(x=160,y=120,width=180)
        

        #row2
        lbl_name=Label(self.root,text="Name",font=("times new roman",15),bg="white").place(x=50,y=160)
    
        txt_name=Entry(self.root,text="Name",textvariable=self.var_name,font=("times new roman",15),bg="light yellow")
        txt_name.place(x=160,y=160,width=180)
    
        #row3
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=50,y=200)
        txt_contact=Entry(self.root,text="Email",textvariable=self.var_contact,font=("times new roman",15),bg="light yellow")
        txt_contact.place(x=160,y=200,width=180)
        
        #row4
        lbl_address=Label(self.root,text="address",font=("times new roman",15),bg="white").place(x=50,y=240)
        self.txt_address=Text(self.root,font=("times new roman",15),bg="light yellow")
        self.txt_address.place(x=160,y=240,width=300,height=60)
        
        
        #btns
        btn_add=Button(self.root,text="Save",command=self.add,font=("times new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=100,y=320,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("times new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=250,y=320,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15),bg="#f44336",fg="white",cursor="hand2").place(x=400,y=320,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15),bg="#607d8b",fg="white",cursor="hand2").place(x=550,y=320,width=110,height=28)
        
        #Employee Details
        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=900,y=150,width=600,height=350)

        scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(sup_frame,columns=("supid","supno","invoice","name","contact","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading("supid",text="Sup ID")
        self.supplierTable.heading("supno",text="Sup No")
        self.supplierTable.heading("invoice",text="Invoice No.")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("address",text="address")
       
        self.supplierTable["show"]="headings"

        self.supplierTable.column("supid",width=100)
        self.supplierTable.column("supno",width=100)
        self.supplierTable.column("invoice",width=100)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("address",width=100)
        
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        
        #Footer
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed By SUBASHINI Student of CSE\n Adhiyamaan College Of Engineering(Autonomous),Hosur",font=("times new roman",12),bg="#010c48",fg="white").pack(side=BOTTOM,fill=X)
        
    #Function Calling
    def add(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        cur.execute(
                        "insert into supplier (supno,invoice,name,contact,address) values(%s,%s,%s,%s,%s)",
                        (
                            self.var_supno.get(),
                            self.var_invoice.get(),
                            self.var_name.get(),
                            self.var_contact.get(),
                            # self.var_address.get(),
                            self.txt_address.get("1.0", END),
                        ),
                    )
        con.commit()
        messagebox.showinfo(
                        "Success", "Supplier Added Successfully", parent=self.root
                    )
        self.show()

    def show(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
                        
    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_supno.set(row[1])
        self.var_invoice.set(row[2])
        self.var_name.set(row[3])
        self.var_contact.set(row[4])
        self.txt_address.delete("1.0", END),
        self.txt_address.insert(END,row[5]),
        
    def update(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.var_supno.get()=="":
                messagebox.showerror("Error","Supplier ID must be Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where supno=%s",(self.var_supno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    cur.execute(
                            "UPDATE supplier SET invoice=%s,name=%s,contact=%s,address=%s WHERE supno=%s",
                            (
                                self.var_invoice.get(),
                                self.var_name.get(),
                                self.var_contact.get(),
                                self.txt_address.get("1.0", END),
                                self.var_supno.get()
                                
                            )
                        )
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def delete(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.var_supno.get()=="":
                messagebox.showerror("Error","Supplier No must be Required",parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE supno = %s", (self.var_supno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM supplier WHERE supno = %s", (self.var_supno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    def clear(self):
        self.var_supno.set("")
        self.var_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_address.delete("1.0", END)
        #self.txt_address.insert("")
        self.var_search.set("")
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
                cur.execute("SELECT * FROM supplier WHERE " + self.var_searchby.get() + " LIKE %s", ('%' + self.var_searchtxt.get() + '%',))
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                        self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 
        
# if __name__=="__main__":
#     root=Tk()
#     obj=supplierClass(root)
#     root.mainloop()
