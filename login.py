from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import os
import email_pass
import smtplib
import time

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        #images
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)
        
        #Login_Frame
        self.name=StringVar()
        self.password=StringVar()
        
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)
        
        title=Label(login_frame,text="Login",font=("Elephant",30,"bold"),bg="White").place(x=0,y=30,relwidth=1)
            
        lbl_name=Label(login_frame,text="Name",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_name=Entry(login_frame,textvariable=self.name,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=190)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)
        
        btn_login=Button(login_frame,text="Log In",command=self.login,font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)
        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=360)
        
        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_window,font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)

        #Frame2
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)
        
        lbl_reg=Label(register_frame,text="Don't have an account?",font=("times new roman",13),bg="white").place(x=80,y=20)
        btn_signup=Button(register_frame,text="Sign Up",command=self.signup_window,font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=237,y=17)

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
        self.root.destroy()
        os.system("python signup.py")
        
    def  login(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.name.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select utype from employee where name=%s AND password=%s",(self.name.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid USERNAME/PASSWORD",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python bill.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)   
            
    def forget_window(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        try:
            if self.name.get()=="":
                messagebox.showerror("Error","Employee Name must be required",parent=self.root)
            else:
                cur.execute("Select email from employee where name=%s",(self.name.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid Employee Name,try again",parent=self.root)
                else:
                    self.var_otp=StringVar()
                    self.var_password=StringVar()
                    self.var_conf_pass=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_id=StringVar()
                    #call send_email_function()
                    
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror("Error","Connection Error,try again",parent=self.root)
                    else:
                        
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title("RESET PASSWORD")
                        self.forget_win.geometry("400x350+500+100")
                        self.forget_win.focus_force()
                        
                        title=Label(self.forget_win,text="Reset Password",font=("Times new roman",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                        lbl_reset=Label(self.forget_win,text="Enter OTP Sent on Registered Email",font=("Times new roman",15)).place(x=20,y=60)
                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("Times new roman",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                        self.btn_reset=Button(self.forget_win,text="SUBMIT",command=self.validate_otp,font=("Times new roman",15),bg="lightblue")
                        self.btn_reset.place(x=280,y=100,width=100,height=30)
                        
                        
                        lbl_new_pass=Label(self.forget_win,text="New Password",font=("Times new roman",15,"bold")).place(x=20,y=160)
                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("Times new roman",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)
                        
                        
                        lbl_c_pass=Label(self.forget_win,text="Confirm Password",font=("Times new roman",15,"bold")).place(x=20,y=225)
                        txt_c_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("Times new roman",15)).place(x=20,y=255,width=250,height=30)
                        
                        self.btn_update=Button(self.forget_win,text="Update",command=self.update_password,state=DISABLED,font=("Times new roman",15),bg="lightblue")
                        self.btn_update.place(x=150,y=300,width=100,height=30)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror("Error","Password is required",parent=self.forget_win)
        elif self.var_new_pass.get()!= self.var_conf_pass.get():
            messagebox.showerror("Error","Password & Confirm Paasword must be same",parent=self.forget_win)
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="ims")
            cur=con.cursor()
            try:
                cur.execute("UPDATE employee SET password=%s where id=%s",(self.var_new_pass.get(),self.var_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password updated sucessfully",parent=self.forget_win)
                self.forget_win.destroy()
                
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
              
             
    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP,Try again",parent=self.forget_win)
            
    def send_email(self,to_):
        s=smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_
        
        s.login(email_,pass_)
        
        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))

        subj="IMS-Reset Password OTP"
        msg=f"Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\n with Regards,\nIMS Team"
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'
        
    
                
if __name__=="__main__":       
    root=Tk()
    obj=Login_System(root)
    root.mainloop()
