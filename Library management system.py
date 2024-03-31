import tkinter as tk
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import random
from datetime import datetime

import sqlite3
conn = sqlite3.connect('library.db')
cur = conn.cursor()
import datetime

root = tk.Tk()
root.title("Library Management System")
root.geometry("475x600")
root.configure(background='powder blue')
root.resizable(0,0)

my_label = tk.Label(root, font=('arial',25,'bold','underline'), text="Library Management System")
my_label.pack(side=tk.TOP)

#=============================Variables=============================

task=StringVar()

pname=StringVar()
bname=StringVar()
author=StringVar()
code=StringVar()
day=StringVar()
price=StringVar()
bname_m=StringVar()
author_m=StringVar()
code_m=StringVar()
price_m=StringVar()

#=============================Functions=============================

def Exit():
    iExit=tkinter.messagebox.askyesno('Library Managment System','Do you want to exit Library Management System?')
    if iExit>0:
        root.destroy()
        return

def borrow():
    win = tk.Toplevel()
    win.wm_title("Borrow book")
    win.geometry("400x400")
    win.configure(background='powder blue')
    win.resizable(0,0)

    my_label = tk.Label(win, font=('arial',25,'bold','underline'), text=":Borrow:")
    my_label.pack(side=tk.TOP)

    mdatalbl = tk.Label(win, font=('arial',17,'bold','underline'), text="Details: ").place(x = 25, y=66)

    pnamelbl = tk.Label(win, font=('arial',10,'bold'), text = "First Name: ").place(x = 25, y = 110)
    pnamecbo = ttk.Combobox(win, width=25, state='readonly', textvariable=pname)
    pnamecbo.place(x = 115, y = 110)
    tp=('--select--',)
    for i in cur.execute('SELECT * FROM stud'):
        tp=tp+(i[0],)
    pnamecbo['value'] = tp
    pnamecbo.current(0)
    
    bname_mlbl = tk.Label(win, font=('arial',10,'bold'), text = "Book Name: ").place(x = 25, y = 150)
    bname_mcbo = ttk.Combobox(win, width=22,state='readonly', textvariable=bname_m)
    bname_mcbo.place(x = 115, y = 150)
    tp=('--select--',)
    for i in cur.execute('SELECT * FROM books'):
        tp=tp+(i[0],)
    bname_mcbo['value'] = tp
    bname_mcbo.current(0)

    task.set('Borrow')
    
    executebtn = tk.Button(win, text = " EXECUTE ", font=('arial',12,'bold'), command= execute, activebackground = "green",  activeforeground = "blue").place(x = 225 , y = 285)
 
    closebtn = tk.Button(win, text='CLOSE', font=('arial',12,'bold'), command=win.destroy, activebackground = "red",activeforeground = "blue").place(x = 150 , y = 285)

def retrn():
    win = tk.Toplevel()
    win.wm_title("Return book")
    win.geometry("400x400")
    win.configure(background='powder blue')
    win.resizable(0,0)

    my_label = tk.Label(win, font=('arial',25,'bold','underline'), text=":Return:")
    my_label.pack(side=tk.TOP)

    mdatalbl = tk.Label(win, font=('arial',17,'bold','underline'), text="Details: ").place(x = 25, y=66)

    pnamelbl = tk.Label(win, font=('arial',10,'bold'), text = "First Name: ").place(x = 25, y = 110)
    pnamecbo = ttk.Combobox(win, width=25, state='readonly', textvariable=pname)
    pnamecbo.place(x = 115, y = 110)
    tp=('--select--',)
    for i in cur.execute('SELECT * FROM stud'):
        tp=tp+(i[0],)
    pnamecbo['value'] = tp
    pnamecbo.current(0)
    
    bname_mlbl = tk.Label(win, font=('arial',10,'bold'), text = "Book Name: ").place(x = 25, y = 150)
    bname_mcbo = ttk.Combobox(win, width=22,state='readonly', textvariable=bname_m)
    bname_mcbo.place(x = 115, y = 150)
    tp=('--select--',)
    for i in cur.execute('SELECT * FROM books'):
        tp=tp+(i[0],)
    bname_mcbo['value'] = tp
    bname_mcbo.current(0)

    task.set('Return')
    
    executebtn = tk.Button(win, text = " EXECUTE ", font=('arial',12,'bold'), command= execute, activebackground = "green",activeforeground = "blue").place(x = 225 , y = 285)

    closebtn = tk.Button(win, text='CLOSE', font=('arial',12,'bold'), command=win.destroy, activebackground = "red",activeforeground = "blue").place(x = 150 , y = 285)

def execute():
    day=datetime.date.today()
    book=bname_m.get()
    name=pname.get()
    phno=StringVar()
    cls=StringVar()
    membno=StringVar()

    for i in cur.execute('SELECT * FROM stud'):
        if pname==i[0]:
            phno.set(i[1])
            membno.set(i[2])
            cls.set(i[3])
        
    t=(name,phno.get(),cls.get(),membno.get(),book,task.get(),day)
    t1=(name,book,membno.get())

    if name=='--select--':
        errormsg=tkinter.messagebox.showinfo('Error','Please enter your name!!')
        return

    elif book=='--select--':
        errormsg=tkinter.messagebox.showinfo('Error','Please enter book name!!')
        return
    
    if task.get()=='Return':
        f=-1
        for i in cur.execute('SELECT * FROM dues'):
            if i[0]==name and i[1]==bname_m.get() and i[2]==membno.get():
                cur.execute('INSERT INTO log VALUES(?,?,?,?,?,?,?)',t)
                successmsg=tkinter.messagebox.showinfo('Success','Success!!')
                cur.execute('DELETE FROM dues WHERE pname == ? and bname == ? and membno == ?',t1)
                conn.commit()
                f=0
                return
        if f==-1:
            errormsg=tkinter.messagebox.showinfo('Error','You never borrowed this book!!')
            return
    elif task.get()=='Borrow':
        f=-1
        for i in cur.execute('SELECT * FROM dues'):
            if i[0]==name and i[1]==bname_m.get() and i[2]==membno.get():
                errormsg=tkinter.messagebox.showinfo('Error','Unable to borrow same book twice!!')
                f=0
                return
        if f==-1:
            cur.execute('INSERT INTO log VALUES(?,?,?,?,?,?,?)',t)
            cur.execute('INSERT INTO dues VALUES(?,?,?)',t1)
            conn.commit()
            successmsg=tkinter.messagebox.showinfo('Success','Success!!')
            return

def register():
    win = tk.Toplevel()
    win.wm_title("Register")
    win.geometry("800x400")
    win.configure(background='powder blue')
    win.resizable(0,0)
    
    regtdisp =Text(win, font=('arial',12,'bold'),width=82,heigh=19,padx=10,pady=4)
    regtdisp.place(x=20, y=10)

    for i in cur.execute("SELECT * FROM log"):
        regtdisp.insert(END,i[0]+'      '+i[1]+'      '+i[2]+'      '+i[3]+'      '+i[4]+'      '+i[5]+'      '+i[6]+'      '+'\n')

def booklist():
    win = tk.Toplevel()
    win.wm_title("Book List")
    win.geometry("700x400")
    win.configure(background='powder blue')
    win.resizable(0,0)
    
    regtdisp =Text(win,font=('arial',12,'bold'),width=75,heigh=19,padx=10,pady=4)
    regtdisp.place(x=20, y=10)

    for i in cur.execute("SELECT * FROM books"):
        regtdisp.insert(END,i[0]+'      '+i[1]+'      '+i[2]+'      '+i[3]+'\n')

#==============================Buttons==============================

returnbtn = tk.Button(root, text = " RETURN ", font=('arial',18,'bold'), command = retrn, activebackground = "green", activeforeground = "blue").place(x = 160 , y = 110)

borrowbtn = tk.Button(root, text = " BORROW ", font=('arial',18,'bold'), command = borrow, activebackground = "green", activeforeground = "blue").place(x = 155 , y = 200)

booklistbtn = tk.Button(root, text = " BOOK LIST ", font=('arial',18,'bold'), command = booklist, activebackground = "green", activeforeground = "blue").place(x = 145 , y = 290)

registorbtn = tk.Button(root, text = " SHOW REGISTER ", font=('arial',18,'bold'), command = register, activebackground = "green", activeforeground = "blue").place(x = 110 , y = 380)

exitbtn = tk.Button(root, text = " EXIT ", font=('arial',18,'bold'), command = Exit, activebackground = "red", activeforeground = "blue").place(x = 185 , y = 470)

root.mainloop()
