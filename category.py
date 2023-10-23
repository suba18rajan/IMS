from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
#import sqlite3
import pymysql


class categoryClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Manage Category")
        self.root.config(bg="white")
        self.root.focus_force()
        
        
        #variables
        self.var_cid=StringVar()
        self.var_name=StringVar()
        #title
        title=Label(self.root,text="Manage Product Category",font=("times new roman",30),bg="#184a45",fg="white").pack(side=TOP,fill=X,padx=10,pady=2)
        
        name=Label(self.root,text="Enter Category Name",font=("times new roman",30),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",18),bg="white").place(x=50,y=170,width=300)
        
        btn_add=Button(self.root,text="ADD",command=self.add,font=("times new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("times new roman",15),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)
        
        #Category Details
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.category_Table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_Table.xview)
        scrolly.config(command=self.category_Table.yview)

        self.category_Table.heading("cid",text="C ID")
        self.category_Table.heading("name",text="Name")
        self.category_Table["show"]="headings"

        self.category_Table.column("cid",width=90)
        self.category_Table.column("name",width=100)
        self.category_Table.pack(fill=BOTH,expand=1)
        self.category_Table.pack(fill=BOTH,expand=1)
        self.category_Table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        #images
        self.im1=Image.open("images/cat.jpg")
        self.im1=self.im1.resize((500,250))
        self.im1=ImageTk.PhotoImage(self.im1)
        
        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)
        
        
        self.im2=Image.open("images/category.jpg")
        self.im2=self.im2.resize((500,250))
        self.im2=ImageTk.PhotoImage(self.im2)
        
        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)
        
        #Footer
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed By SUBASHINI Student of CSE\n Adhiyamaan College Of Engineering(Autonomous),Hosur",font=("times new roman",12),bg="#184a45",fg="white").pack(side=BOTTOM,fill=X)
        
        
    #Function Calling
    def add(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        cur.execute(
                        "insert into category (name) values(%s)",
                        (
                            #self.var_cid.get(),
                            self.var_name.get(),
                           
                        ),
                    )
        con.commit()
        messagebox.showinfo(
                        "Success", "Category Added Successfully", parent=self.root
                    )
        self.show()
        
        
    def show(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.category_Table.delete(*self.category_Table.get_children())
            for row in rows:
                self.category_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
                        
    def get_data(self,ev):
        f=self.category_Table.focus()
        content=(self.category_Table.item(f))
        row=content['values']
        #print(row)
        self.var_cid.set(row[0])
        self.var_name.set(row[1])
       
    def delete(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.var_cid.get()=="":
                messagebox.showerror("Error","Category ID must be Required",parent=self.root)
            else:
                cur.execute("SELECT * FROM Category WHERE cid = %s", (self.var_cid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM category WHERE cid = %s", (self.var_cid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        self.show()
        
        
        
        
# if __name__=="__main__":
#     root=Tk()
#     obj=categoryClass(root)
#     root.mainloop()

