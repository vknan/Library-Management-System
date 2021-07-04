from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "root"
mydatabase = "db"

con = pymysql.connect(host = "localhost", user="root", password = mypass, database = mydatabase)
cur = con.cursor()

issueTable = 'books_issued'
bookTable = "books" # book table

def deletebook():
    bid = bookInfo1.get()
    deletesql = "delete from "+bookTable+" where bid = '"+bid+"'"
    deleteIssue = "delete from "+issueTable+" where bid = '"+bid+"'"
    try:
        cur.execute(deletesql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()

        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")

    
    bookInfo1.delete(0,END)
    root.destroy()


def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, root, bookTable

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingframe1 = Frame(root, bg="#FFBB00", bd=5)
    headingframe1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headinglabel = Label(headingframe1, text="Delete Book", bg="black", fg="white", font = ('Courier', 15))
    headinglabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    lframe = Frame(root, bg='black')
    lframe.place(relx=0.1, rely=0.3, relwidth = 0.8, relheight=0.5)

    # Book ID to delete
    lbl = Label(lframe, text = "Book ID : ", bg = 'black', fg='white')
    lbl.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(lframe)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth = 0.62)

    #submit
    submitbtn = Button(root, text = "SUBMIT", bg = "#d1ccc0", fg='black', command = deletebook)
    submitbtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #Quit
    quitbtn = Button(root, text = "QUIT", bg = "#f7f1e3", fg='black', command = root.destroy)
    quitbtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
