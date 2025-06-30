import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import png
import tkinter as tk
import sqlite3
import random
import time

db = sqlite3.connect('Library.db')
cr = db.cursor()
def crqrcode():
    bookname = kitapadientry.get()
    bookwriter = kitapyazarentry.get()
    booknum = kitapnumentry.get()
    bookedition = kitapbaskientry.get()
    qr = pyqrcode.create(bookname+"/"+bookwriter+"/"+booknum+"/"+bookedition)
    qr.png("{}.png".format(bookname),scale=8)
    cr.execute("INSERT INTO Library VALUES(?,?,?,?,?,?,?)",(0,0,bookname,bookwriter,booknum,bookedition,1))
    db.commit()
    label = tk.Label(win,text="QRcode oluşturuldu ve veriler veri tabanına keydedildi.")
    label.place(x=100,y=300)
    breakpoint
    

win = tk.Tk()
win.geometry('500x500')
win.title("QRcode Generator")
kitapadi = tk.Label(win,text="Kitap Adı: ",font="Times 14 bold")
kitapadi.place(x=100,y=100)
kitapyazari = tk.Label(win,text="Kitap Yazarı: ",font="Times 14 bold")
kitapyazari.place(x=100,y=150)
kitapnum = tk.Label(win,text="Kitap Numarası: ",font="Times 14 bold")
kitapnum.place(x=100,y=200)
kitapbaski = tk.Label(win,text="Kitap Baskı Numarası: ",font="Times 14 bold")
kitapbaski.place(x=100,y=250)
kitapadientry = tk.Entry(win)
kitapadientry.place(x=200,y=98)
kitapyazarentry = tk.Entry(win)
kitapyazarentry.place(x=225,y=150)
kitapnumentry = tk.Entry(win)
kitapnumentry.place(x=250,y=198)
kitapbaskientry = tk.Entry(win)
kitapbaskientry.place(x=300,y=248)
qrcodebuton = tk.Button(win,text="QR oluştur",command=crqrcode)
qrcodebuton.place(x=100,y=350)
win.mainloop()