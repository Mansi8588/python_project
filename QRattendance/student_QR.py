# this program create qrcode for each student according to their name present in student.txt file


from MyQR import myqr
import os
import base64

# create  and read
f=open("student.txt",'r')
lines=f.read().split("\n") # split use to define that text separated by \n
print(lines)

# create QR
for i in range(0,len(lines)):
    data=lines[i].encode()
    name=base64.b64encode(data)
    version,level,qr_name=myqr.run(
    str(name),
    level='H',
    version=1,

    # background

    picture="ajeet.png",
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name=str(lines[i]+'.bmp'),
    save_dir=os.getcwd()

)
