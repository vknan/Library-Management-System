from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "root"
mydatabase = "db"

con = pymysql.connect(host = "localhost", user="root", password = mypass, database = mydatabase)
cur = con.cursor()
bookTable = "books"

def view():
    root= Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9", bd = 5)
    Canvas1.pack(expand = True, fill=BOTH)

    headingframe1 = Frame(root, bg="#FFBB00", bd=5)
    headingframe1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headinglabels = Label(headingframe1, text="View Books", bg='black', fg='white', font = ('Courier', 15))
    headinglabels.place(relx=0, rely =0, relwidth=1, relheight=1)

    labelframe = Frame(root, bg='black')
    labelframe.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    

    y=0.25
    Label(labelframe, text="%-10s%-40s%-30s%-20s"%('BID','TITLE', 'AUTHOR', 'STATUS') , bg ='black', fg='white').place(relx=0.07, rely=0.1)
    Label(labelframe, text="-------------------------------------------------------------------", bg="black", fg="white").place(relx=0.05, rely=0.2)
    getbooks = "select * from "+bookTable
    try:
        cur.execute(getbooks)
        con.commit()

        for i in cur:
            Label(labelframe, text = "%-10s%-40s%-30s%-20s"%(i[0], i[1], i[2], i[3]), bg='black', fg='white').place(relx=0.07,rely=y)
            y+=0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitbtn = Button(root, text="Quit", bg='#f7f1e3', fg = 'black', command=root.destroy)
    quitbtn.place(relx = 0.4, rely=0.9, relwidth = 0.18, relheight =0.08)

    root.mainloop()