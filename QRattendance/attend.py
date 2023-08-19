import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import smtplib as st
import pybase64

# start webcame

cap=cv2.VideoCapture(0)

names=[]


# function for attendence file

fob =open('attendence','a+')
def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        fob.write(z+'\n')
        return names
def send_mail_function():  # defined function to send mail post fire detection using threading

    ob = st.SMTP('smtp.gmail.com', 587)
    ob.ehlo()
    ob.starttls()
    ob.login('younliacmh@gmail.com', 'mrtnaaovjjcxgsxn')
    subject = "python code"
    body = "i am mansi rai ,trying to learn python"
    message = "subject:{}\n\n{}".format(subject, body)
    listadd = ['softenginee12@gmail.com', 'ajmrhw12@gmail.com']
    ob.sendmail('younliacmh@gmail.com', listadd, message)
    print("send mail")
    ob.close()

# function data present or not

def checkData(data):
  data=str(data)
  if data in names:
    print('Already present')
    print(data)

  else:
    print('\n'+str(len(names)+1)+'\n'+'present done')
    if (data == str(b"b'TWFuc2kgUmFp'")):
       send_mail_function()
    enterData(data)




while True:
   _,frame=cap.read()
   decodeObject=pyzbar.decode(frame)
   for obj in decodeObject:
     checkData(obj.data)
     time.sleep(1)

   cv2.imshow('Frame',frame)

   if cv2.waitKey(1) & 0xff==ord('q'):
      cv2.destroyAllWindows()
      break


fob.close()

