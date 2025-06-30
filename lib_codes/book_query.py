from tkinter import font
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

def bq():
    book_name = book_query.get()
    cr.execute("SELECT * FROM Library WHERE Kitap_adi = ?",(book_name,))
    res = cr.fetchall()
    if res == []:
        newwindow = tk.Toplevel(win)
        newwindow.geometry('1000x200')
        label = tk.Label(newwindow,text="Aradığınız kitap kütüphanemizde mevcut değildir.",font="Times 18 bold")
        label.pack()
    else:
        a = res[0][0]
        b = res[0][1]
        if a == 0 and b == 0:
            newwindow = tk.Toplevel(win)
            newwindow.geometry('1000x200')
            label = tk.Label(newwindow,text="Aradığınız kitap kütüphanemizde mevcuttur.",font="Times 18 bold")
            label.pack()
        else:
            newwindow1 = tk.Toplevel(win)
            newwindow1.geometry('1000x200')
            label = tk.Label(newwindow1,text="Aradığınız kitap kütüphanemizde mevcuttur.",font="Times 18 bold")
            label.pack()
            label3 = tk.Label(newwindow1,text="Fakat {} tarafından {} tarihte alınmıştır.".format(a,b),font="Times 18 bold")
            label3.place(x=200,y=100)
        


win = tk.Tk()
win.geometry('500x500')
win.title("Book Query")
book_label = tk.Label(win,text="Kitap Adı Girin: ",font="Times 14 bold")
book_label.place(x=100,y=150)
book_query = tk.Entry(win)
book_query.place(x=244,y=148)
book_query_button = tk.Button(win,text="Kitap Sorgula",font="Times 14 bold",command=bq)
book_query_button.place(x=180,y=230)
win.mainloop()
