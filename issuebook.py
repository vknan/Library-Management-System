from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "root"
mydatabase = "db"

con = pymysql.connect(host = "localhost", user="root", password = mypass, database = mydatabase)
cur = con.cursor()

issueTable = 'books_issued'
bookTable = "books"


allbid=[]
def issue():

    bid = inf1.get()
    issueto = inf2.get()

    extractbid = "select bid from "+bookTable
    try:
        cur.execute(extractbid)
        con.commit()

        for  i in cur:
            allbid.append(i[0])
        
        if bid in allbid:
            checkavail = "select status from "+bookTable+" where bid = "+bid
            cur.execute(checkavail)
            con.commit()
            for i in cur:
                check = i[0]
            
            if check =="avail":
                status = True
            else:
                status = False
            
        else:
            messagebox.showinfo("Error", "Book ID not present")

    except:
        messagebox.showinfo("error", "Can't fetch Book ID's")

    issuesql = "insert into "+issueTable+" values("+bid+","+issueto+")"
    
    updatestatus = "update "+bookTable+" set status = 'issued' where bid= "+bid

    try:
        if bid in allbid and status ==True:
            cur.execute(issuesql)
            con.commit()
            cur.execute(updatestatus)
            con.commit()
            messagebox.showinfo("Success", "Book issued successfully")
            root.destroy()
        elif(bid in allbid and status ==False):
            allbid.clear()
            messagebox.showinfo("Message", "Book already issued")
            root.destroy()
            return

    except:
        messagebox.showinfo("Search error", "The value entered is wrong, Try again")

    allbid.clear()


def issuebook():
    global issuebtn, lframe, lbl, inf1, inf2, quitbtn, root, Canvas1, status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height= 400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg= "#D6ED17")
    Canvas1.pack(expand = True, fill = BOTH)

    headingframe = Frame(root, bg = "#FFBB00", bd = 5)
    headingframe.place(relx=0.25, rely=0.1, relwidth = 0.5, relheight=0.13)

    headinglabel = Label(headingframe, text = "Issue Book", bg = "black", fg = "white", font = ("Courier", 15))
    headinglabel.place(relx=0, rely = 0, relwidth=1, relheight = 1)

    lframe = Frame(root, bg='black')
    lframe.place(relx = 0.1, rely=0.3, relwidth = 0.8, relheight = 0.5)

    #Book ID
    lbl = Label(lframe, text = "Book ID : ", bg = 'black', fg="white")
    lbl.place(relx = 0.05, rely = 0.2)

    inf1 = Entry(lframe)
    inf1.place(relx = 0.3, rely= 0.2, relwidth =0.62 )

    #issued to
    lbl2 = Label(lframe, text = "Issued To : ", bg = 'black', fg="white")
    lbl2.place(relx = 0.05, rely = 0.4)

    inf2 = Entry(lframe)
    inf2.place(relx = 0.3, rely= 0.4, relwidth =0.62 )


    issuebtn = Button(root, text = "Issue", bg="#d1ccc0", fg= "black", command =issue)
    issuebtn.place(relx = 0.28, rely=0.9, relwidth = 0.18, relheight=0.08)

    quitbtn = Button(root, text = "QUIT", bg = "#aaa69d", fg="black", command = root.destroy)
    quitbtn.place(relx = 0.53, rely = 0.9, relwidth = 0.18, relheight = 0.08)

    root.mainloop() 



