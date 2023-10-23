from tkinter import*
import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import qrcode
from resizeimage import resizeimage

class Qr_Generator:
    def __init__(self, root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator")
        self.root.resizable(False,False)
        
        title=Label(self.root,text="Qr Code Generator",font=("times new roman",40),bg="#063246",fg="white").place(x=0,y=0,relwidth=1)
        
        self.var_cid=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_address=StringVar()
    
     #qr frame
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        qr_Frame.place(x=50,y=100,width=500,height=380)

        qr_title=Label(qr_Frame,text="Customer Details",font=("times new roman",30),bg="#043256",fg="white").place(x=0,y=0,relwidth=1)
        
        lbl_cus_id=Label(qr_Frame,text="Customer ID",font=("times new roman",15,'bold'),bg="white").place(x=20,y=60)   
        lbl_name=Label(qr_Frame,text="Customer Name",font=("times new roman",15,'bold'),bg="white").place(x=20,y=100)
        lbl_email=Label(qr_Frame,text="Customer Email",font=("times new roman",15,'bold'),bg="white").place(x=20,y=140)
        lbl_gender=Label(qr_Frame,text="Customer Gender",font=("times new roman",15,'bold'),bg="white").place(x=20,y=180)
        lbl_contact=Label(qr_Frame,text="Customer Contact",font=("times new roman",15,'bold'),bg="white").place(x=20,y=220)
        lbl_address=Label(qr_Frame,text="Customer Address",font=("times new roman",15,'bold'),bg="white").place(x=20,y=260)
        
        txt_cus_id=Entry(qr_Frame,text="Customer ID",textvariable=self.var_cid,font=("times new roman",15,'bold'),bg="white").place(x=200,y=60)   
        txt_name=Entry(qr_Frame,text="Customer Name",textvariable=self.var_name,font=("times new roman",15,'bold'),bg="white").place(x=200,y=100)
        txt_email=Entry(qr_Frame,text="Customer Email",textvariable=self.var_email,font=("times new roman",15,'bold'),bg="white").place(x=200,y=140)
        #txt_gender=Entry(qr_Frame,text="Customer Gender",font=("times new roman",15,'bold'),bg="white").place(x=200,y=180)
        cmb_gender=ttk.Combobox(qr_Frame,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',font=("times new roman",15))
        cmb_gender.place(x=200,y=180,width=205)
        cmb_gender.current(0)
        txt_contact=Entry(qr_Frame,text="Customer Contact",textvariable=self.var_contact,font=("times new roman",15,'bold'),bg="white").place(x=200,y=220)
        txt_address=Entry(qr_Frame,text="Customer Address",textvariable=self.var_address,font=("times new roman",15,'bold'),bg="white").place(x=200,y=260)
        
        btn_generate=Button(qr_Frame,text="QR Generate",command=self.generate,font=("times new roman",18,'bold'),bg="#2196f3",fg="white").place(x=50,y=300,width=200,height=30)
        btn_clr=Button(qr_Frame,text="Clear",command=self.clear,font=("times new roman",18,'bold'),bg="#607d8b",fg="white").place(x=300,y=300,width=150,height=30)
        
        self.msg=""
        self.lbl_msg=Label(qr_Frame,text=self.msg,font=("times new roman",20),bg="white",fg="green")
        self.lbl_msg.place(x=0,y=340,relwidth=1)
        
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        qr_Frame.place(x=600,y=100,width=250,height=380)

        qr_title=Label(qr_Frame,text="Customer QR",font=("times new roman",30),bg="#043256",fg="white").place(x=0,y=0,relwidth=1)
        
        self.qr_code=Label(qr_Frame,text=" No QR  \n available",font=("times new roman",15),bg="#3f51b5",fg="white")
        self.qr_code.place(x=35,y=100,width=180,height=180)
        
        
    def clear(self):
        self.var_cid.set('')
        self.var_name.set('')
        self.var_email.set('')
        self.var_gender.set('')
        self.var_contact.set('')
        self.var_address.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg,fg='red')
        self.qr_code.config(image='')
        
    def generate(self):
        if self.var_cid.get()=="" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_address.get()=="":
            self.msg="All fields are required"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Customer ID:{self.var_cid.get()}\n Customer Name:{self.var_name.get()}\n Customer Email:{self.var_email.get()}\n Customer Gender:{self.var_gender.get()}\n Customer Contact:{self.var_contact.get()}\n Customer Address:{self.var_address.get()}")
            qr_code=qrcode.make(qr_data) 
            #print(qr_code)     
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("qrcode_generation"+str(self.var_cid.get()+'.png'))
            
            #QR Code Image Update 
            self.im=ImageTk.PhotoImage(file="qrcode_generation"+str(self.var_cid.get()+'.png'))
            self.qr_code.config(image=self.im)
            
            #Update Notification
            self.msg="QR Generated Successfully!!!"
            self.lbl_msg.config(text=self.msg,fg="green")
        
    

if __name__=="__main__":
    root=Tk()
    obj=Qr_Generator(root)
    root.mainloop()