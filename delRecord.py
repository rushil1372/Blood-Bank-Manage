from tkinter import Tk, Frame, Label, Entry, Button
from tkinter import messagebox
import pymysql

con = pymysql.connect( host="localhost",user="root",password="",database="test")
cur = con.cursor()

def deleteRecord():
    
    bid = Info1.get()
    
    deleteSql = "delete from blood where B_ID = '"+bid+"'"

    try:
        cur.execute(deleteSql)
        con.commit()

        messagebox.showinfo('Success',"Record Deleted Successfully")

    except:
        messagebox.showinfo("Please check Blood ID")
    
    print(bid)

    Info1.delete(0, 5)
    root.destroy()

def delete(): 
    
    global Info1, con, cur, root
    
    root = Tk()
    root.title("System")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Record", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    lb2 = Label(labelFrame,text="Blood ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteRecord)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()