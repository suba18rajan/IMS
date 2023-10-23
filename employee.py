from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkcalendar import *
#import sqlite3
import pymysql
#from os import DirEntry

class employeeClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Manage Employees")
        self.root.config(bg="white")
        self.root.focus_force()

        #Variable Declartion
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        self.var_address=StringVar()

        #Search Frame
        SearchFrame=LabelFrame(self.root,text="Search Employees",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #Options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Empid","Name","Contact","Email"),state='readonly',justify=CENTER,font=("times new roman",15))
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
        title=Label(self.root,text="Employee Details",font=("times new roman",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

        #content
        #row1
        lbl_id=Label(self.root,text="ID",font=("times new roman",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("times new roman",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=750,y=150)

        txt_id=Entry(self.root,text="ID",textvariable=self.var_id,font=("times new roman",15),bg="light yellow")
        txt_id.place(x=150,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)

        txt_contact=Entry(self.root,text="Contact No",textvariable=self.var_contact,font=("times new roman",15),bg="light yellow")
        txt_contact.place(x=850,y=150,width=180)

        #row2
        lbl_name=Label(self.root,text="Name",font=("times new roman",15),bg="white").place(x=50,y=190)
        #lbl_dob=Label(self.root,text="D.O.B",font=("times new roman",15),bg="white").place(x=350,y=190)
        #lbl_doj=Label(self.root,text="D.O.J",font=("times new roman",15),bg="white").place(x=750,y=190)

        txt_name=Entry(self.root,text="Name",textvariable=self.var_name,font=("times new roman",15),bg="light yellow")
        txt_name.place(x=150,y=190,width=180)
        #txt_dob=Entry(self.root,textvariable=self.var_dob,text="D.O.B",font=("times new roman",15),bg="light yellow").place(x=500,y=190,width=180)
        #txt_doj=Entry(self.root,text="D.O.J",textvariable=self.var_doj,font=("times new roman",15),bg="light yellow").place(x=850,y=190,width=180)

        def pick_date(event):
            global cal,date_window
            date_window=Toplevel()
            date_window.grab_set()
            date_window.title('Choose Date Of Birth')
            date_window.geometry('250x220+590+370')
            cal=Calendar(date_window,selectmode="day",date_pattern="dd/mm/yyyy")
            cal.place(x=0,y=0)

            submit_btn=Button(date_window,text="Submit",command=grab_date)
            submit_btn.place(x=80,y=190)


        def grab_date():
           dob_entry.delete(0,END)
           dob_entry.insert(0,cal.get_date())
           date_window.destroy()

        dob=Label(self.root,text="D.O.B",bg="white",font=("Times new roman",15))
        dob.place(x=350,y=190)
        dob_entry=Entry(self.root,textvariable=self.var_dob,highlightthickness=0,relief=RIDGE,bg="light yellow",font=("Times new roman",15))
        dob_entry.place(x=500,y=190,width=180)
        dob_entry.insert(0,"dd/mm/yyyy")
        dob_entry.bind("<1>",pick_date)
        
        def pickdate(event):
            global cal,date_window
            date_window=Toplevel()
            date_window.grab_set()
            date_window.title('Choose Date Of Joining')
            date_window.geometry('250x220+590+370')
            cal=Calendar(date_window,selectmode="day",date_pattern="dd/mm/yyyy")
            cal.place(x=0,y=0)

            submit_btn=Button(date_window,text="Submit",command=grabdate)
            submit_btn.place(x=80,y=190)


        def grabdate():
           doj_entry.delete(0,END)
           doj_entry.insert(0,cal.get_date())
           date_window.destroy()
           
        doj=Label(self.root,text="D.O.J",font=("times new roman",15),bg="white")
        doj.place(x=750,y=190)
        doj_entry=Entry(self.root,text="D.O.J",textvariable=self.var_doj,font=("times new roman",15),bg="light yellow")
        doj_entry.place(x=850,y=190,width=180)
        doj_entry.insert(0,"dd/mm/yyyy")
        doj_entry.bind("<1>",pickdate)
        
        #row3
        lbl_email=Label(self.root,text="Email",font=("times new roman",15),bg="white").place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",font=("times new roman",15),bg="white").place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("times new roman",15),bg="white").place(x=750,y=230)

        txt_email=Entry(self.root,text="Email",textvariable=self.var_email,font=("times new roman",15),bg="light yellow")
        txt_email.place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,text="Password",textvariable=self.var_pass,font=("times new roman",15),bg="light yellow")
        txt_pass.place(x=500,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","Employee"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)

        #row4
        lbl_address=Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("times new roman",15),bg="white").place(x=500,y=270)
        txt_salary=Entry(self.root,text="Salary",textvariable=self.var_salary,font=("times new roman",15),bg="light yellow")
        txt_salary.place(x=600,y=270,width=180)


        self.txt_address=Text(self.root,font=("times new roman",15),bg="light yellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        
        
        #btns
        btn_add=Button(self.root,text="Save",command=self.add,font=("times new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("times new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)
        
        #Employee Details
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,width=1050,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("empid","id","name","email","gender","contact","dob","doj","pass","utype","salary","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("empid",text="Emp ID")
        self.EmployeeTable.heading("id",text="ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("salary",text="Salary")
        self.EmployeeTable.heading("address",text="Address")
       
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("empid",width=90)
        self.EmployeeTable.column("id",width=100)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        #Footer
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed By SUBASHINI Student of CSE\n Adhiyamaan College Of Engineering(Autonomous),Hosur",font=("times new roman",12),bg="#010c48",fg="white").pack(side=BOTTOM,fill=X)
        
    #Function Calling
    def add(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        cur.execute(
                        "insert into employee (id,name,email,gender,contact,dob,doj,password,utype,salary,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.var_salary.get(),
                            self.txt_address.get("1.0", END),
                        ),
                    )
        con.commit()
        messagebox.showinfo(
                        "Success", "Employee Added Successfully", parent=self.root
                    )
        self.show()
        
    def show(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
                        
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        #print(row)
        self.var_id.set(row[1])
        self.var_name.set(row[2])
        self.var_email.set(row[3])
        self.var_gender.set(row[4])
        self.var_contact.set(row[5])
        self.var_dob.set(row[6])
        self.var_doj.set(row[7])
        self.var_pass.set(row[8])
        self.var_utype.set(row[9])
        self.var_salary.set(row[10])
        self.txt_address.delete("1.0", END),
        self.txt_address.insert(END,row[11]),
        
    def update(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.var_id.get()=="":
                messagebox.showerror("Error","Employee ID must be Required",parent=self.root)
            else:
                cur.execute("Select * from employee where id=%s",(self.var_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    cur.execute(
                            "UPDATE employee SET name=%s, email=%s, gender=%s, contact=%s, dob=%s, doj=%s, password=%s, utype=%s, salary=%s, address=%s WHERE id=%s",
                            (
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_pass.get(),
                                self.var_utype.get(),
                                self.var_salary.get(),
                                self.txt_address.get("1.0", END),
                                self.var_id.get()
                            )
                        )
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        self.show()

    def delete(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.var_id.get()=="":
                messagebox.showerror("Error","Employee ID must be Required",parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE id = %s", (self.var_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM employee WHERE id = %s", (self.var_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        self.show()
        
    def clear(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("")
        self.var_salary.set("")
        self.txt_address.delete("1.0", END)
        #self.txt_address.insert("")
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
                cur.execute("SELECT * FROM employee WHERE " + self.var_searchby.get() + " LIKE %s", ('%' + self.var_searchtxt.get() + '%',))
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 
    
    
        
if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()

