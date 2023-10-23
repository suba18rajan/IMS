from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
#import sqlite3
import pymysql


class productClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Manage Products")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_pno=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        
        
        #Frame
        product_Frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)
        
        #Title
        title=Label(product_Frame,text="Products Details",font=("times new roman",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        #Column1
        lbl_pno=Label(product_Frame,text="P No",font=("times new roman",18),bg="white").place(x=50,y=60)
        lbl_category=Label(product_Frame,text="Category",font=("times new roman",18),bg="white").place(x=30,y=110)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("times new roman",18),bg="white").place(x=30,y=160)
        lbl_product_name=Label(product_Frame,text="Product Name",font=("times new roman",18),bg="white").place(x=30,y=210)
        lbl_price=Label(product_Frame,text="Price",font=("times new roman",18),bg="white").place(x=30,y=260)
        lbl_quantity=Label(product_Frame,text="Quantity",font=("times new roman",18),bg="white").place(x=30,y=310)
        lbl_status=Label(product_Frame,text="Status",font=("times new roman",18),bg="white").place(x=30,y=350)
        
        #txt_category=Label(product_Frame,text="Category",font=("times new roman",18),bg="white")
        
        #Column2
        txt_pno=Entry(product_Frame,textvariable=self.var_pno,font=("times new roman",15),bg="lightyellow").place(x=180,y=60,width=200)
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_cat.place(x=150,y=110,width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_sup.place(x=150,y=160,width=200)
        cmb_sup.current(0)
    
        txt_product_name=Entry(product_Frame,textvariable=self.var_name,font=("times new roman",15),bg="lightyellow").place(x=180,y=210,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow").place(x=150,y=260,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=150,y=310,width=200)
        
        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Select","Active","Inactive"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_status.place(x=150,y=350,width=200)
        cmb_status.current(0)
        
        
        #btns
        btn_add=Button(product_Frame,text="Save",command=self.add,font=("times new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("times new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("times new roman",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("times new roman",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)
        
        
        #Search Frame
        SearchFrame=LabelFrame(self.root,text="Search Products",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #Options
        cmb_search=ttk.Combobox(SearchFrame,text="Search Products",textvariable=self.var_searchby,values=("Select","Pid","Pno","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        #Search Entry Label
        txt_search=Entry(SearchFrame,text="Search Products",textvariable=self.var_searchtxt,font=("times new roman",15),bg="lightyellow")
        txt_search.place(x=200,y=10)

        #btn Search
        # btn_search=Entry(SearchFrame,font=("times new roman",15),bg="lightyellow")
        # btn_search.place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("times new roman",15),bg="#4caf50",fg="white",cursor="hand2")
        btn_search.place(x=410,y=9,width=150,height=30)

        #Footer
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed By SUBASHINI Student of CSE\n Adhiyamaan College Of Engineering(Autonomous),Hosur",font=("times new roman",12),bg="#010c48",fg="white").pack(side=BOTTOM,fill=X)

        #Product Details
        product_Frame=Frame(self.root,bd=3,relief=RIDGE)
        product_Frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(product_Frame,orient=VERTICAL)
        scrollx=Scrollbar(product_Frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(product_Frame,columns=("pid","pno","category","supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("pid",text="P ID")
        self.ProductTable.heading("pno",text="P No")
        self.ProductTable.heading("category",text="Category")
        self.ProductTable.heading("supplier",text="Supplier")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("qty",text="Qty")
        self.ProductTable.heading("status",text="Status")
        self.ProductTable["show"]="headings"

        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("pno",width=90)
        self.ProductTable.column("category",width=100)
        self.ProductTable.column("supplier",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("status",width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        self.fetch_cat_sup()
        
    #Function Calling
    def fetch_cat_sup(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            self.cat_list.append("Empty")
            self.sup_list.append("Empty")
            cur.execute("Select name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0]) 
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
        
    def add(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        cur.execute(
                        "insert into product (pno,category,supplier,name,price,qty,status) values(%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_pno.get(),
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                        ),
                    )
        con.commit()
        messagebox.showinfo(
                        "Success", "Product Added Successfully", parent=self.root
                    )
        self.show()
        
    def show(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        #print(row)
        self.var_pno.set(row[1])
        self.var_cat.set(row[2])
        self.var_sup.set(row[3])
        self.var_name.set(row[4])
        self.var_price.set(row[5])
        self.var_qty.set(row[6])
        self.var_status.set(row[7])
        
    def update(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.var_pno.get()=="":
                messagebox.showerror("Error","Product ID must be Required",parent=self.root)
            else:
                cur.execute("Select * from product where pno=%s",(self.var_pno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    cur.execute(
                            "UPDATE product SET category=%s,supplier=%s,name=%s,price=%s,qty=%s,status=%s WHERE pno=%s",
                            (
                            
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            self.var_pno.get()
                            
                            )
                        )
                    con.commit()
                    messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
     
    def delete(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.var_pno.get()=="":
                messagebox.showerror("Error","Product ID must be Required",parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE pno = %s", (self.var_pno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM product WHERE pno = %s", (self.var_pno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        self.show()

    def clear(self):
        self.var_pno.set("")
        self.var_cat.set("")
        self.var_sup.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("")
        self.var_searchtxt.set("")
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
                cur.execute("SELECT * FROM product WHERE " + self.var_searchby.get() + " LIKE %s", ('%' + self.var_searchtxt.get() + '%',))
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 

            
    
        
# if __name__=="__main__":
#     root=Tk()
#     obj=productClass(root)
#     root.mainloop()