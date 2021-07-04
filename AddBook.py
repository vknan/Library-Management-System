from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

def bookregister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"', '"+author+"', '"+status+"')"
    issuebook = "insert into "+issuetable+" values('"+bid+"', '"+status+"')"

    try:
        cur.execute(insertBooks)
        con.commit()
        if(status == "issued"):
            cur.execute(issuebook)
            con.commit()
        else:
            pass
        messagebox.showinfo("Success", "Book added successfully")
    except: 
        messagebox.showinfo("Error", "Can't add data into Database")
        

def addbook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, issuetable

    root = Tk()
    root.title("Library")
    root.minsize(width = 400, height = 400)
    root.geometry("600x500")

    mypass = "root"
    mydatabase = "db"

    con = pymysql.connect(host = "localhost", user="root", password = mypass, database = mydatabase)
    cur = con.cursor()
    
    #Enter table names here
    bookTable = 'books'
    issuetable = "books_issued"

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#FF6E40")
    Canvas1.pack(expand=True, fill = BOTH)

    headingframe1 = Frame(root, bg="#FFBB00", bd=5)
    headingframe1.place(relx=0.25, rely = 0.1, relwidth = 0.5, relheight=0.13)
    headinglabel = Label(headingframe1, text="Add Books", bg = "black", fg = 'white', font=('courier', 15))
    headinglabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    
    lframe = Frame(root, bg="black")
    lframe.place(relx=0.1, rely=0.4, relwidth = 0.8, relheight = 0.4)
    
    #BookID
    lbl = Label(lframe, text = 'Book ID : ', bg="black", fg="White")
    lbl.place(relx=0.05, rely=0.2, relheight= 0.08)

    bookInfo1 = Entry(lframe)
    bookInfo1.place(relx = 0.3, rely=0.2, relwidth=0.62, relheight=0.08)
    
    #Title
    lbl2 = Label(lframe, text = 'Title : ', bg="black", fg="White")
    lbl2.place(relx=0.05, rely=0.35, relheight= 0.08)

    bookInfo2 = Entry(lframe)
    bookInfo2.place(relx = 0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    #Author
    lbl3 = Label(lframe, text = 'Author : ', bg="black", fg="White")
    lbl3.place(relx=0.05, rely=0.5, relheight= 0.08)

    bookInfo3 = Entry(lframe)
    bookInfo3.place(relx = 0.3, rely=0.5, relwidth=0.62, relheight=0.08)
    
    #Status
    lbl4 = Label(lframe, text = 'Status :(avail/issued) ', bg="black", fg="White")
    lbl4.place(relx=0.05, rely=0.65, relheight= 0.08)

    bookInfo4 = Entry(lframe)
    bookInfo4.place(relx = 0.3, rely=0.65, relwidth=0.62, relheight=0.08)


    submitbtn = Button(root, text="SUBMIT", bg = "#d1ccc0", fg="black", command = bookregister)
    submitbtn.place(relx = 0.28, rely=0.9, relwidth = 0.18, relheight=0.08)

    quitbtn = Button(root, text="Quit", bg = "#f7f1e3", fg="black", command = root.destroy)
    quitbtn.place(relx = 0.53, rely=0.9, relwidth = 0.18, relheight=0.08)
    

    root.mainloop()