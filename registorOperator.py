
import sqlite3
import tkinter as tk
from tkinter import StringVar, messagebox, ttk, END, IntVar, DISABLED, NORMAL, Button
from imp import reload



print("register Operator Launched")

#Colour codes Initialization
rootBG = '#C7F3CA'
btnBG = '#82E3AC'

#root window
root_registeroperator = tk.Tk()
MyLeftPos = int(root_registeroperator.winfo_screenwidth() - 400) / 2
myTopPos = int(root_registeroperator.winfo_screenheight() - 600) / 2
root_registeroperator.geometry("%dx%d+%d+%d" % (220, 20, MyLeftPos, myTopPos))
root_registeroperator.geometry("400x600")
root_registeroperator.iconbitmap('images\\icons\\main.ico')
root_registeroperator.resizable(False, False)
root_registeroperator['background'] = rootBG
root_registeroperator.title('Electricity Billing System')

#input variables for Tk

fullname = StringVar()
operatorID = StringVar()
mobile = StringVar()
password = StringVar()
adminpassword = StringVar()

#functons for validating and saving the Entries

def clear_data():
    txt_operetorName.delete(0, END)
    txt_operetorID.delete(0, END)
    txt_mobileNo.delete(0, END)
    txt_password.delete(0, END)
    txt_adminpassword.delete(0, END)

def entry_operator():
    print(fullname.get(),operatorID.get(), mobile.get(), password.get(),adminpassword.get())

    if fullname.get() == "" or mobile.get() == "" or password.get() == ""or operatorID.get() == ""or adminpassword.get() == "":
        messagebox.showerror("Error !", "All Fields are Required !")
    else:
        import databaseConnection

        # Connect to sqlite database
        conn = databaseConnection.getsqliteconnection()
        try:
            cur = conn.cursor()

            cur.execute("select * from operatorinfo where operatorID=?", (operatorID.get(),))

            row = cur.fetchone()
            if row != None:
                txt_operetorID.delete(0, END)
                messagebox.showerror("Error !", "Operator ID Already Exists ! Try with another one.")
            else:
                if adminpassword.get()== 'admin' :
                    query = ('insert into operatorinfo(fullname, operatorID, mobile, password )'
                             'values (:fname1, :operatorID1, :mobile1, :pass1);')
                    params = {
                        'fname1': fullname.get(),
                        'operatorID1': operatorID.get(),
                        'mobile1': mobile.get(),
                        'pass1': password.get(),
                    }

                    conn.execute(query, params)
                    conn.commit()
                    messagebox.showinfo("Success !", "Registration Completed !")
                    clear_data()
                else:
                    print("fail")
                    messagebox.showerror("Error !", "Wrong Admin Password.!")
        except sqlite3.Error as error:
            print("Problem with SQlite table", error)
        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")

def loginWin():
    root_registeroperator.destroy()
    import login
    reload(login)


# registerframe
registeroperator = tk.Frame(root_registeroperator, bg=rootBG)
registeroperator.pack(padx= 0, pady=20)
registeroperator.columnconfigure(0, weight=1)

#Operator Login Heading
operatorlogin_label = tk.Label(registeroperator, text="OPERATOR REGISTRATION", font=("impress", 16,"bold"), bg=rootBG)
operatorlogin_label.grid(column=0, row=0,columnspan=2, padx=10, pady=20)

#Operator Name
operetorName = tk.Label(registeroperator, text="Full Name :",  bg=rootBG, font=15)
operetorName.grid(column=0, row=1,sticky=tk.W, padx=10, pady=20)

txt_operetorName = tk.Entry(registeroperator, textvar=fullname, width=23)
txt_operetorName.grid(column=1, row=1, sticky=tk.W,padx=10, pady=20)

#OperatorID
operetorIDlabel = tk.Label(registeroperator, text="Operator ID :",  bg=rootBG, font=15)
operetorIDlabel.grid(column=0, row=2,sticky=tk.W, padx=10, pady=20)

txt_operetorID = tk.Entry(registeroperator, textvar=operatorID, width=23)
txt_operetorID.grid(column=1, row=2, sticky=tk.W,padx=10, pady=20)

#OperatorID
mobileNo = tk.Label(registeroperator, text="Mobile No :",  bg=rootBG, font=15)
mobileNo.grid(column=0, row=3, sticky=tk.W, padx=10, pady=20)

txt_mobileNo = tk.Entry(registeroperator, textvar=mobile, width=23)
txt_mobileNo.grid(column=1, row=3, sticky=tk.W,padx=10, pady=20)

#Password
passwordlabel = tk.Label(registeroperator, text="Password :",  bg=rootBG, font=15)
passwordlabel.grid(column=0, row=4,sticky=tk.W, padx=10, pady=20)

txt_password = tk.Entry(registeroperator, textvar=password, show="*", width=23)
txt_password.grid(column=1, row=4, sticky=tk.W,padx=10, pady=20)

#Admin Password
adminpasswordlabel = tk.Label(registeroperator, text="Admin Password :",  bg=rootBG, font=15)
adminpasswordlabel.grid(column=0, row=5,sticky=tk.W, padx=10, pady=20)

txt_adminpassword = tk.Entry(registeroperator, textvar=adminpassword, show="*", width=23)
txt_adminpassword.grid(column=1, row=5, sticky=tk.W,padx=10, pady=20)

#register Button
registerBtn = Button(registeroperator, text="Register", foreground="black", bg=btnBG, activebackground=rootBG,width=34, height=3, font= ('impress' ,13), relief=tk.FLAT, command=entry_operator)
registerBtn.grid(column=0, row=6,columnspan=2,sticky=tk.W, padx=5, pady=10)


# login button
loginwinBtn = Button(registeroperator, text="<- Back to Login", foreground="black",bg=btnBG, activebackground="lightgrey", width=16, height=3, font= ('impress' ,13), relief=tk.FLAT, command=loginWin)
loginwinBtn.grid(column=0, row=7, sticky=tk.E, padx=5, pady=5)
#Exit Button
exitBtn = Button(registeroperator, text="Exit", foreground="black", bg=btnBG, activebackground="lightgrey",width=16, height=3, font= ('impress' ,13), relief=tk.FLAT, command= root_registeroperator.destroy)
exitBtn.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)

registeroperator.mainloop()