from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import os

class Signup:
    def __init__(self,root):
        self.root=root
        self.root.title("SignUp")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        #images
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)
        
        #Signup frame
        self.var_pass=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_cno=StringVar()
        
        signup_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        signup_frame.place(x=650,y=90,width=350,height=460)
        
        #Frame2
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)
        
        lbl_reg=Label(register_frame,text="Don't have an account?",font=("times new roman",13),bg="white").place(x=80,y=20)
        btn_login=Button(register_frame,text="Log In",command=self.login_window,font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=237,y=17)

        title=Label(signup_frame,text="Sign Up",font=("Times new roman",30,"bold"),bg="White").place(x=0,y=30,relwidth=1)
        
             
        lbl_name=Label(signup_frame,text="Name",font=("Andalus",15),bg="white",fg="black").place(x=30,y=120)
        txt_name=Entry(signup_frame,textvariable=self.var_name,font=("times new roman",15),bg="white",bd=0)
        txt_name.place(x=120,y=120)      
        frame=Frame(signup_frame,bg="black").place(x=120,y=140,width=200,height=2)
        
        lbl_email=Label(signup_frame,text="Email",font=("Andalus",15),bg="white",fg="black").place(x=30,y=180)
        txt_email=Entry(signup_frame,textvariable=self.var_email,font=("times new roman",15),bg="white",bd=0)
        txt_email.place(x=120,y=180)     
        frame=Frame(signup_frame,bg="black").place(x=120,y=200,width=200,height=2)
    
        lbl_cno=Label(signup_frame,text="Contact No",font=("Andalus",15),bg="white",fg="black").place(x=10,y=240)
        txt_cno=Entry(signup_frame,textvariable=self.var_cno,font=("times new roman",15),bg="white",bd=0)
        txt_cno.place(x=120,y=240)     
        frame=Frame(signup_frame,bg="black").place(x=120,y=260,width=200,height=2)
        
        lbl_pass=Label(signup_frame,text="Password",font=("Andalus",15),bg="white",fg="black").place(x=10,y=300)
        txt_pass=Entry(signup_frame,textvariable=self.var_pass,show="*",font=("times new roman",15),bg="white",bd=0)
        txt_pass.place(x=120,y=300)     
        frame=Frame(signup_frame,bg="black").place(x=120,y=320,width=200,height=2)
        
        lbl_c_pass=Label(signup_frame,text="C_Password",font=("Andalus",15),bg="white",fg="black").place(x=0,y=360)
        txt_c_pass=Entry(signup_frame,show="*",font=("times new roman",15),bg="white",bd=0)
        txt_c_pass.place(x=120,y=360)     
        frame=Frame(signup_frame,bg="black").place(x=120,y=380,width=200,height=2)
        
        btn_signup=Button(signup_frame,text="Sign Up",command=self.signup_window,font=("Arial Rounded MT Bold",15),bg="#f44336",activebackground="#f44336",fg="white",activeforeground="white",cursor="hand2").place(x=100,y=400,width=150,height=35)

        #Animation Images
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")
        
        self.lbl_change_image=Label(self.root,bg="gray")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)
        
        self.animate()
        
        
    #Calling Functions
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
  
    def signup_window(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.var_name.get() == "" or self.var_email.get() == "" or self.var_cno.get() == "" or self.var_pass.get() == "":
                messagebox.showerror(
                    "Error", "All fields must be required", parent=self.root
                )
            else:
                cur.execute(
                        "insert into employee (name,contact,email,password) values(%s,%s,%s,%s)",
                        (
                            self.var_name.get(),
                            self.var_cno.get(),
                            self.var_email.get(),
                            self.var_pass.get()
                        ),
                )
                con.commit()
                messagebox.showinfo(
                                    "Success", "Sign Up Successfully", parent=self.root
                )  
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        self.login_window()

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")
        
if __name__=="__main__":       
    root=Tk()
    obj=Signup(root)
    root.mainloop()

        