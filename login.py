import sqlite3
import tkinter as tk
from imp import reload
from tkinter import messagebox, END
from tkinter import Button
from imp import reload


#Colour codes Initialization
rootBG = '#C7F3CA'
btnBG = '#82E3AC'



# root window
root_userlogin = tk.Tk()
MyLeftPos = int(root_userlogin.winfo_screenwidth() - 450) / 2
myTopPos = int(root_userlogin.winfo_screenheight() - 450) / 2
root_userlogin.geometry("%dx%d+%d+%d" % (240, 100, MyLeftPos, myTopPos))
root_userlogin.geometry("400x380")
root_userlogin.iconbitmap('images\\icons\\main.ico')
root_userlogin.resizable(False, False)
root_userlogin['background'] = rootBG
root_userlogin.title('Electricity Billing System')
#root_userlogin.state('zoomed')



def checkLogin():
    if username_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror("Error!", "Operator ID and Password can't be blank")
    else:
        import databaseConnection

        # Connect to sqlite database
        conn = databaseConnection.getsqliteconnection()
        try:
            cur = conn.cursor()

            cur.execute("select * from operatorinfo where operatorID=? and password=?", (username_entry.get(),password_entry.get()))

            row = cur.fetchone()
            if row != None:
                root_userlogin.destroy()
                import menu
                reload(menu)

            else:
                messagebox.showerror("Error !", "Invalid Operator ID or Password !")
                username_entry.delete(0, END)
                password_entry.delete(0, END)

        except sqlite3.Error as error:
            print("Problem with SQlite table", error)
        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")
def launchRegistor():
    root_userlogin.destroy()
    import registorOperator
    reload(registorOperator)

root_userlogin.columnconfigure(0, weight=1)
root_userlogin.columnconfigure(1, weight=3)

# loginframe
loginframe = tk.Frame(root_userlogin, bg=rootBG)
loginframe.pack(padx= 0, pady=20)
loginframe.columnconfigure(0, weight=1)

#Operator Login Heading

operatorlogin_label = tk.Label(loginframe, text="OPERATOR LOGIN", font=("impress", 25,"bold"), bg=rootBG)
operatorlogin_label.grid(column=0, row=0,columnspan=2, sticky=tk.W, padx=10, pady=20)

# username
username_label = tk.Label(loginframe, text="Operator ID:", bg=rootBG, font=15)
username_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

username_entry = tk.Entry(loginframe,width=25)
username_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# password
password_label = tk.Label(loginframe, text="Password:", bg=rootBG, font=15)
password_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)


password_entry = tk.Entry(loginframe,  show="*", width=25)
password_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

# login button
login_button = Button(loginframe, text="Login", foreground="black",bg=btnBG, activebackground="lightgrey", width=16, height=3, font= ('impress' ,13), relief=tk.FLAT, command=checkLogin)
login_button.grid(column=0, row=4, sticky=tk.E, padx=5, pady=20)
#Exit Button
exitBtn = Button(loginframe, text="Exit", foreground="black", bg=btnBG, activebackground="lightgrey",width=16, height=3, font= ('impress' ,13), relief=tk.FLAT, command= root_userlogin.destroy)
exitBtn.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

#Register Button
registerBtn = Button(loginframe, text="Register an Operator (ADMIN)", foreground="black", bg=btnBG, activebackground="lightgrey",width=34, height=3, font= ('impress' ,13), relief=tk.FLAT, command=launchRegistor)
registerBtn.grid(column=0, row=5,columnspan=2, sticky=tk.E, padx=5, pady=5)

root_userlogin.mainloop()