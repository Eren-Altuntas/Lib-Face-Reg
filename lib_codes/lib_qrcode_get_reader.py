import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import png
import cv2
import os
import time
import sqlite3

db = sqlite3.connect('Library.db')
cr = db.cursor()
file = open(os.getcwd()+"/yoklama.txt","r",encoding="utf-8")

lines = file.readlines()
lines = lines[-1]
lines = lines.split("|")
alim_tarihi = lines[1]
alici_ismi = lines[0]
print(alici_ismi,alim_tarihi)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
camera = True
used_codes= []
while camera == True:
    success,frame = cap.read()

    for code in decode(frame):
        if code.data.decode("utf-8") not in used_codes:
            print(code.data.decode("utf-8"))
            data = code.data.decode("utf-8")
            data1 = data.split("/")
            data2 = data1[0]
            data3 = data1[3]
            #file.write(data)
            #file.write("\n")
            used_codes.append(code.data.decode("utf-8"))
            time.sleep(3)
            cr.execute("UPDATE Library set Alici_ismi = ? WHERE Kitap_adi = ? and kitap_baski_numarasi = ?",(alici_ismi,data2,data3,))
            cr.execute("UPDATE Library set Alim_Tarihi = ? WHERE Kitap_adi = ? and kitap_baski_numarasi = ?",(alim_tarihi,data2,data3,))
            cr.execute("UPDATE Library set Durum = ? WHERE Kitap_adi = ? and kitap_baski_numarasi = ?",(0,data2,data3,))
            db.commit()
        elif code.data.decode("utf-8") in used_codes:
            print("Bu kod daha önceden kullanılmıştır.")
    cv2.imshow("Code Scan",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit()