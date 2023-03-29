from tkinter import * #tkinter module
import mysql.connector #mysql connector library(pip install mysql-connector-python)
import tkinter.messagebox as msg
#connect to database

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_1"
        )

#insert data to table in database
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert status","All fields are mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("insert status","data inserted successfully")

#search data by id

def search_data():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')

    if e_id.get=="":
        msg.showinfo("search status","id is mandatory for search")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select *from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])
        else:
             msg.showinfo("search status","id not found")
        conn.close()

#update data

def update_data():
    if e_fname.get()=="" or e_lname.get=="" or e_email.get()=="" or e_mobile.get()=="" or e_mobile.get()=="":
        msg.showinfo("update status","all fields are mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update student set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("update status","data updated successfully")

#delete data

def delete_data():
    if e_id.get=="":
        msg.showinfo("delete status","is in=s mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("delete status","data deleted successfully")

       
root=Tk() #object of tk class
root.geometry("400x380")
root.title("my tkinter example")
root.resizable(width=False,height=False)


#Label creation
l_id=Label(root,text="ID",font=("Arial",15))
l_id.place(x=50,y=50)

l_fname=Label(root,text="first name",font=("Arial",15))
l_fname.place(x=50,y=100)

l_lname=Label(root,text="last name",font=("Arial",15))
l_lname.place(x=50,y=150)

l_email=Label(root,text="email",font=("Arial",15))
l_email.place(x=50,y=200)

l_mobile=Label(root,text="mobile",font=("Arial",15))
l_mobile.place(x=50,y=250)

#Textfield(Emtry)

e_id=Entry(root)
e_id.place(x=200,y=50)

e_fname=Entry(root)
e_fname.place(x=200,y=100)

e_lname=Entry(root)
e_lname.place(x=200,y=150)

e_email=Entry(root)
e_email.place(x=200,y=200)

e_mobile=Entry(root)
e_mobile.place(x=200,y=250)

#Button creation

insert=Button(root,text="INSERT",font=("arial",10),fg="white",bg="black",command=insert_data)
insert.place(x=50,y=300)

search=Button(root,text="SEARCH",font=("arial",10),fg="white",bg="black",command=search_data)
search.place(x=110,y=300)

update=Button(root,text="UPDATE",font=("arial",10),fg="white",bg="black",command=update_data)
update.place(x=178,y=300)

delete=Button(root,text="DELETE",font=("arial",10),fg="white",bg="black",command=delete_data)
delete.place(x=244,y=300)



