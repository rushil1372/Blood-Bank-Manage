from tkinter import Tk, Frame, Label, Button
import pymysql
from tkinter import messagebox
from addRecord import add
from delRecord import delete
from viewRecords import view

con = pymysql.connect(host="localhost",port=3306,db="blood_donation",user="root",password="")
cur = con.cursor()

root = Tk()
root.title("System")
root.minsize(width=400,height=400)
root.geometry("600x500")

headingFrame1 = Frame(root,bg="#FFFFFF",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Blood", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Record",bg='black', fg='white', command=add)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Withdraw Record",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Records",bg='black', fg='white', command=view)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
root.mainloop()