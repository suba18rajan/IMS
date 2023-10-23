from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkcalendar import *
import pymysql
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image

class scanqr:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Scan QR")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #title
        title=Label(self.root,text="QR Code Scanner",font=("times new roman",15),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000)

        #btn
        btn_scanqr=Button(self.root,text="Scan QR",command=self.scanqr,font=("times new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)

    def scanqr(self):   
        cap=cv2.VideoCapture(0)
        cap.set(3,640)
        cap.set(4,480)
        while True:
            success,img=cap.read()
            for barcode in decode(img):
                print(barcode.data)
                mydata=barcode.data.decode('utf-8')
                print(mydata)
                pts=np.array([barcode.polygon],np.int32)
                pts=pts.reshape((-1,1,2))
                cv2.polylines(img,[pts],True,(255,0,255),5)
                pts2=barcode.rect
                cv2.putText(img,mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
                
            cv2.imshow('Result',img)
            cv2.waitKey(1)
    
if __name__=="__main__":
    root=Tk()
    obj=scanqr(root)
    root.mainloop()

