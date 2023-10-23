from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from employee import employeeClass
from supplier import supplierClass
from customer import customersClass
from bill import BillClass 
from category import categoryClass 
from product import productClass
from sales import salesClass
from qrcode_generation import Qr_Generator
from tkinter import messagebox
import time
import pymysql
import os

class IMS:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1520x800+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #title
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,padx=20,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w").place(x=0,y=0,relwidth=1,height=70)

        #btn_logout
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow").place(x=1350,y=10,height=50,width=150)
        
        #clock
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #Left Menu
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((120,120))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)


        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=750)

        lbl_menulogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")

        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        #lbl_admin=Button(LeftMenu,text="Admin",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_employees=Button(LeftMenu,text="Employees",command=self.employees,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_suppliers=Button(LeftMenu,text="Suppliers",command=self.suppliers,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_categories=Button(LeftMenu,text="Categories",command=self.categories,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_products=Button(LeftMenu,text="Products",command=self.products,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_customers=Button(LeftMenu,text="Customers",command=self.customers,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_bill=Button(LeftMenu,text="Bill",command=self.bill,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_qr_code=Button(LeftMenu,text="Customer_QR",command=self.qr_code,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_exit=Button(LeftMenu,text="Exit",command=self.exit,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        

        #Content
        self.lbl_employee=Label(self.root,text="Total Employees\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_suppliers=Label(self.root,text="Total Suppliers\n[0]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("times new roman",20,"bold"))
        self.lbl_suppliers.place(x=650,y=120,height=150,width=300)


        self.lbl_categories=Label(self.root,text="Total Categories\n[0]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("times new roman",20,"bold"))
        self.lbl_categories.place(x=1000,y=120,height=150,width=300)

        self.lbl_products=Label(self.root,text="Total Products\n[0]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("times new roman",20,"bold"))
        self.lbl_products.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("times new roman",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        self.lbl_customers=Label(self.root,text="Total Customers\n[0]",bd=5,relief=RIDGE,bg="crimson",fg="white",font=("times new roman",20,"bold"))
        self.lbl_customers.place(x=1000,y=300,height=150,width=300)
        
        self.update_date_time()
        self.update_content()
        #footer
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed By SUBASHINI Student of CSE\n Adhiyamaan College Of Engineering(Autonomous),Hosur",font=("times new roman",12),bg="#010c48",fg="white").pack(side=BOTTOM,fill=X)
    
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)
         
    #File Calling
    def employees(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        
    def suppliers(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    
    def customers(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=customersClass(self.new_win)
    
    def bill(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)
        
    def categories(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def products(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
        
    def qr_code(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Qr_Generator(self.new_win)

    def update_content(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            product=cur.fetchall()
            self.lbl_products.config(text=f"Total Product\n[{str(len(product))}]")
            
            cur.execute("Select * from supplier")
            supplier=cur.fetchall()
            self.lbl_suppliers.config(text=f"Total Supplier\n[{str(len(supplier))}]")
            
            cur.execute("Select * from category")
            category=cur.fetchall()
            self.lbl_categories.config(text=f"Total Categories\n[{str(len(category))}]")
            
            cur.execute("Select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employees\n[{str(len(employee))}]")
            
            
            cur.execute("Select * from customer")
            customer=cur.fetchall()
            self.lbl_customers.config(text=f"Total Customers\n[{str(len(employee))}]")
            
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales \n[{str(bill)}]')
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
            
    def exit(self):
        op = messagebox.askyesno(
            "Confirm", "Do you really want to Exit?", parent=self.root
        )
        if op == True:
            self.root.destroy()

   
        
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()
