from tkinter import*
import tkinter
import tkinter.messagebox as message
import mysql.connector as mysql

root= Tk()
root.geometry("1000x600")
root.title("Employee Mangement")

def insert():
    name=name_entry.get()
    phone=phone_entry.get()
    idd=idd_entry.get()
    email=email_entry.get()

    if(name=="" or phone=="" or idd=="" or email==""):
        message.showinfo("Insertion status","All the fields are required")
    else:
        mydb=mysql.connect(host="localhost",user="root",password="1234", database="employee")
        cursor=mydb.cursor()
        cursor.execute("insert into employee values('"+name+"','"+idd+"','"+phone+"','"+email+"')")
        cursor.execute("commit");

        name_entry.delete(0,'end')
        phone_entry.delete(0,'end')
        idd_entry.delete(0,'end')
        email_entry.delete(0,'end')
        all()
        message.showinfo("insertion status","insertion successfull")
        mydb.close();
def update():
    name=name_entry.get()
    phone=phone_entry.get()
    idd=idd_entry.get()
    email=email_entry.get()

    if(name=="" or phone=="" or idd=="" or email==""):
        message.showinfo("Update status","All the fields are required")
    else:
        mydb=mysql.connect(host="localhost",user="root",password="1234", database="employee")
        cursor=mydb.cursor()
        cursor.execute("update employee set name='"+name+"', phone = '"+ phone +"', email = '"+email+"'where id='"+idd_entry.get()+"'")
        cursor.execute("commit");

        name_entry.delete(0,'end')
        phone_entry.delete(0,'end')
        idd_entry.delete(0,'end')
        email_entry.delete(0,'end')
        all()
        message.showinfo("update status","update successfull")
        mydb.close();
def delete():
    if(idd_entry.get==""):
        message.showinfo("Delete status","ID is compolsary for delete")
    else:
        mydb=mysql.connect(host="localhost",user="root",password="1234", database="employee")
        cursor=mydb.cursor()
        cursor.execute("delete from employee where id='"+idd_entry.get()+"'")
        cursor.execute("commit");

        name_entry.delete(0,'end')
        phone_entry.delete(0,'end')
        idd_entry.delete(0,'end')
        email_entry.delete(0,'end')
        all()
        message.showinfo("Delete status","Delete successfull")
        mydb.close();
def info():
    idd=idd_entry.get()
    if(name==""):
         message.showinfo("Fetch status","ID field is required")
    else:
        mydb=mysql.connect(host="localhost",user="root",password="1234", database="employee")
        cursor=mydb.cursor()
        cursor.execute("select * from employee where id ='"+idd_entry.get()+"'")
        rows=cursor.fetchall()
        for row in rows:
            name_entry.insert(0,row[0])
            phone_entry.insert(0,row[2])
            email_entry.insert(0,row[3])
        mydb.close();

def all():
    mydb=mysql.connect(host="localhost",user="root",password="1234", database="employee")
    cursor=mydb.cursor()
    cursor.execute("select * from employee")
    rows=cursor.fetchall()
    listbox.delete(0,listbox.size())
    for row in rows:
        data = row[0]+'     '+str(row[1])+'     '+row[2]+'     '+row[3]
        listbox.insert(listbox.size()+1,data)
    mydb.close()


title= Label(root, text= 'Employee_Management_System', font=('bold',30))
title.place(x=20,y=10)

name= Label(root, text= 'Employee_name', font=('bold',13))
name.place(x=30,y=150)

phone= Label(root, text= 'Employee_phone_no', font=('bold',13))
phone.place(x=30,y=180)

idd= Label(root, text= 'Employee_ID', font=('bold',13))
idd.place(x=30,y=210)

email= Label(root, text= 'Employee_email', font=('bold',13))
email.place(x=30,y=240)

name_entry=Entry()
name_entry.place(x=230,y=150)

phone_entry=Entry()
phone_entry.place(x=230,y=180)

idd_entry=Entry()
idd_entry.place(x=230,y=210)

email_entry=Entry()
email_entry.place(x=230,y=240)

submit = Button(root, text="Submit",font=("italic",15),bg="white",command=insert)
submit.place(x=50,y=270)


update = Button(root, text="Update",font=("italic",15),bg="white",command=update)
update.place(x=150,y=270)


show = Button(root, text="Show",font=("italic",15),bg="white",command=info)
show.place(x=350,y=270)


delete = Button(root, text="Delete",font=("italic",15),bg="white",command=delete)
delete.place(x=250,y=270)


listbox = Listbox(root, width=80, height=7)
listbox.place(x=450,y=150)

all()




root.mainloop()















