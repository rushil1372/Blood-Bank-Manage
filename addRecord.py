from tkinter import Tk, Frame, Label, Entry, Button
from tkinter import messagebox
import pymysql

def Register():
    
    gender = DInfo1.get()
    age = DInfo2.get()
    height = DInfo3.get()
    weight = DInfo4.get()
    location = DInfo5.get()

    hemo = PInfo1.get()
    temp = PInfo2.get()
    pressure = PInfo3.get()
    pulse = PInfo4.get()

    blood_type = BInfo1.get()
    quantity = BInfo2.get()
    
    insertDonor = "insert into donor(gender,age,height,weight,location) values ('"+gender+"','"+age+"','"+height+"','"+weight+"','"+location+"')"
    insertPre   = "insert into pre_exam(hemogloblin_gdl,temp_f,blood_pressure,pulse_rate_BPM) values ('"+hemo+"','"+temp+"','"+pressure+"','"+pulse+"')"
    insertBlood = "insert into blood(Blood_Type,quantity) values ('"+blood_type+"','"+quantity+"')"

    try:
        cur.execute(insertDonor)
        cur.execute(insertPre)
        cur.execute(insertBlood)
        con.commit()
        messagebox.showinfo('Success',"Record added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(gender)
    print(location)
    print(hemo)
    print(pulse)
    print(quantity)
    root.destroy()

def add(): 
    
    global DInfo1, DInfo2, DInfo3, DInfo4, DInfo5, PInfo1, PInfo2, PInfo3, PInfo4, BInfo1, BInfo2, con, cur, root
    
    root = Tk()
    root.title("System")
    root.minsize(width=400,height=400)
    root.geometry("1000x700")

    con = pymysql.connect( host="localhost",user="root",password="",database="test")
    cur = con.cursor()
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=9)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Record", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.4)
        
    # Donor    
    lb1 = Label(labelFrame,text="Gender : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    DInfo1 = Entry(labelFrame)
    DInfo1.place(relx=0.2,rely=0.2, relwidth=0.25, relheight=0.08)
        
    lb2 = Label(labelFrame,text="Age : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    DInfo2 = Entry(labelFrame)
    DInfo2.place(relx=0.2,rely=0.35, relwidth=0.25, relheight=0.08)
        
    lb3 = Label(labelFrame,text="Height : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    DInfo3 = Entry(labelFrame)
    DInfo3.place(relx=0.2,rely=0.50, relwidth=0.25, relheight=0.08)
        
    lb4 = Label(labelFrame,text="Weight : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    DInfo4 = Entry(labelFrame)
    DInfo4.place(relx=0.2,rely=0.65, relwidth=0.25, relheight=0.08)

    lb5 = Label(labelFrame,text="Location : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.80, relheight=0.08)
        
    DInfo5 = Entry(labelFrame)
    DInfo5.place(relx=0.2,rely=0.80, relwidth=0.25, relheight=0.08)

    # Pre Exam
    lb6 = Label(labelFrame,text="Hemogloblin : ", bg='black', fg='white')
    lb6.place(relx=0.5,rely=0.2, relheight=0.08)
        
    PInfo1 = Entry(labelFrame)
    PInfo1.place(relx=0.65,rely=0.2, relwidth=0.25, relheight=0.08)

    lb7 = Label(labelFrame,text="Temperature : ", bg='black', fg='white')
    lb7.place(relx=0.5,rely=0.35, relheight=0.08)
        
    PInfo2 = Entry(labelFrame)
    PInfo2.place(relx=0.65,rely=0.35, relwidth=0.25, relheight=0.08)

    lb8 = Label(labelFrame,text="Blood Pressure : ", bg='black', fg='white')
    lb8.place(relx=0.5,rely=0.5, relheight=0.08)
        
    PInfo3 = Entry(labelFrame)
    PInfo3.place(relx=0.65,rely=0.5, relwidth=0.25, relheight=0.08)

    lb8 = Label(labelFrame,text="Pulse Rate : ", bg='black', fg='white')
    lb8.place(relx=0.5,rely=0.65, relheight=0.08)
        
    PInfo4 = Entry(labelFrame)
    PInfo4.place(relx=0.65,rely=0.65, relwidth=0.25, relheight=0.08)

    #Blood
    lb9 = Label(labelFrame,text="Blood Type : ", bg='black', fg='white')
    lb9.place(relx=0.5,rely=0.80, relheight=0.08)
        
    BInfo1 = Entry(labelFrame)
    BInfo1.place(relx=0.60,rely=0.80, relwidth=0.10, relheight=0.08)

    lb10 = Label(labelFrame,text="Quantity : ", bg='black', fg='white')
    lb10.place(relx=0.75,rely=0.80, relheight=0.08)
        
    BInfo2 = Entry(labelFrame)
    BInfo2.place(relx=0.85,rely=0.80, relwidth=0.10, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black', command=Register)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()