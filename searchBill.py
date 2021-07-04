import tkinter as tk
from tkinter import StringVar, messagebox, ttk, END, IntVar, DISABLED, NORMAL, Button, CENTER, W,NO
import emailBill
from imp import reload

from imp import reload
print("manage consumer Launched")

#Colour codes Initialization
rootBG = '#C7F3CA'
btnBG = '#82E3AC'

# Database
import databaseConnection
conn = databaseConnection.getsqliteconnection()
cur = conn.cursor()

#root window
rootSearchBill = tk.Tk()
MyLeftPos = int(rootSearchBill.winfo_screenwidth() - 800) / 2
myTopPos = int(rootSearchBill.winfo_screenheight() - 800) / 2
rootSearchBill.geometry("%dx%d+%d+%d" % (220, 20, MyLeftPos, myTopPos))
rootSearchBill.geometry("900x800")
rootSearchBill.iconbitmap('images\\icons\\main.ico')
rootSearchBill.resizable(False, False)
rootSearchBill['background'] = rootBG
rootSearchBill.title('Electricity Billing System')

#frame for Contraints
searchBillFrame= tk.Frame(rootSearchBill, bg=rootBG)
searchBillFrame.pack(padx= 0, pady=20)
searchBillFrame.columnconfigure(0, weight=1)


#label
searchBill_label = tk.Label(searchBillFrame, text="All Bills", font=("impress", 20,"bold"), bg=rootBG)
searchBill_label.grid(column=0, row=0,columnspan=4, padx=10, pady=20)

#Treeview to View All The Consumers
billsTree = ttk.Treeview(searchBillFrame)

#defining Coloumns
billsTree['columns'] = ("Bill No","Meter No","Units Consumed","Total Amount","Creation Date")

#formating the coloumns
billsTree.column("#0", width=0, stretch=NO)
billsTree.column("Bill No",anchor=tk.CENTER, width=70)
billsTree.column("Meter No",anchor=tk.CENTER, width=70)
billsTree.column("Units Consumed", anchor=W, width=70)
billsTree.column("Total Amount", anchor=W, width=70)
billsTree.column("Creation Date", anchor=W, width=80)


#Headings for Treeviews
billsTree.heading("#0", text="",anchor = tk.W)
billsTree.heading("Bill No",text="Bill No",anchor=tk.CENTER)
billsTree.heading("Meter No",text="Meter No",anchor=tk.CENTER)
billsTree.heading("Units Consumed", text="Units",anchor=W)
billsTree.heading("Total Amount", text="Amount",anchor=W)
billsTree.heading("Creation Date", text="Date",anchor=W)
#positioning Treeview
billsTree.grid(row=1,column=0,columnspan=10, ipadx= 50, ipady =50)
# SELECT users.email, users.password, data.data_1, data.data_2
# FROM users,data
# WHERE users.user_id=data.user_id AND users.email='$user_email'
cur.execute("SELECT * from bills")
rows1 = cur.fetchall()
print(rows1)
count = 0
for row in rows1:
    billsTree.insert(parent='', index='end', iid=count,text="", values=(rows1[count]))
    count +=1

searchBill_label = tk.Label(searchBillFrame, text="Search Bills", font=("impress", 20,"bold"), bg=rootBG)
searchBill_label.grid(column=0, row=2,columnspan=4, padx=10, pady=20)

def searchBillbymeterno():
    print('triggered')
    cur.execute("SELECT * from bills where meterNo=?",(selectmeternoEntry.get()))
    rows2 = cur.fetchall()
    print(rows2)
    count = 0
    for i in billsTree.get_children():
        billsTree.delete(i)
    for row in rows2:
        billsTree.insert(parent='', index='end', iid=count, text="", values=(rows2[count]))
        count += 1

def searchBillbyBillno():
    print('triggered')
    cur.execute("SELECT * from bills where billNo=?",(selectBillnoEntry.get(),))
    rows3 = cur.fetchall()
    print(rows3)
    count = 0
    for i in billsTree.get_children():
        billsTree.delete(i)
    for row in rows3:
        billsTree.insert(parent='', index='end', iid=count, text="", values=(rows3[count]))
        count += 1


# Mter number Search
selectmeternoEntry = StringVar()
selectmeternoEntryl = tk.Label(searchBillFrame, text="Enter Meter Number:", bg=rootBG, font=15)
selectmeternoEntryl.grid(column=0, row=4, sticky=tk.E, padx=10, pady=20)
txt_selectmeternoEntry = tk.Entry(searchBillFrame, textvar=selectmeternoEntry, width=30, relief=tk.FLAT)
txt_selectmeternoEntry.grid(column=1, row=4, sticky=tk.W, padx=10, pady=20)

# Selected Row Button
SearchBillBtn = Button(searchBillFrame, text="Search", foreground="black", bg=btnBG,
                        activebackground=rootBG, width=20, height=3, font=('impress', 13), relief=tk.FLAT,command=searchBillbymeterno)
SearchBillBtn.grid(column=2, row=4,columnspan=1, padx=10, pady=20)
# Bill no search
selectBillnoEntry = StringVar()
selectBillnoEntryl = tk.Label(searchBillFrame, text="Enter Bill Number:", bg=rootBG, font=15)
selectBillnoEntryl.grid(column=0, row=3, sticky=tk.E, padx=10, pady=20)
txt_selectBillnoEntry = tk.Entry(searchBillFrame, textvar=selectBillnoEntry, width=30, relief=tk.FLAT)
txt_selectBillnoEntry.grid(column=1, row=3, sticky=tk.W, padx=10, pady=20)


#Email Functinality

def searchedBillEmail():
    conn = databaseConnection.getsqliteconnection()
    cur = conn.cursor()
    cur2 = conn.cursor()

    cur.execute("SELECT * from bills where billNo=?",(selectBillnoEntry.get(),))
    rowss = cur.fetchall()
    countt = 0

    for roww in rowss:
        meternocheck = str(roww[1])
        tempunits = str(roww[2])
        finalbillamount = str(roww[3])
        creationTime = str(roww[4])
        countt += 1

    meternumber = meternocheck

    cur2.execute("SELECT * from consumerDetails WHERE meterNo=?",(meternumber))
    rows = cur2.fetchall()
    count = 0
    for row in rows:
        meterNole = str(row[0])
        namele = str(row[1])
        mobileNole = str(row[2])
        emaille = str(row[3])
        addressle = str(row[4])
        count += 1
    billnotemp = selectBillnoEntry.get()

    emailBill.sendEmail(billnotemp)


# Selected Row Button
SearchBillBtn = Button(searchBillFrame, text="Search", foreground="black", bg=btnBG,
                        activebackground=rootBG, width=20, height=3, font=('impress', 13), relief=tk.FLAT,command=searchBillbyBillno)
SearchBillBtn.grid(column=2, row=3,columnspan=1, padx=10, pady=20)


# email Row Button
SearchedBillemailBtn = Button(searchBillFrame, text="Send Bill", foreground="black", bg=btnBG,
                        activebackground=rootBG, width=20, height=3, font=('impress', 13), relief=tk.FLAT,command=searchedBillEmail)
SearchedBillemailBtn.grid(column=3, row=3,columnspan=1, padx=10, pady=20)
def exittomain():
    rootSearchBill.destroy()
    import menu
    reload(menu)


# Exit Button
exitBtn = Button(searchBillFrame, text="Exit", foreground="black", bg=btnBG, activebackground="lightgrey",
                 width=20, height=3, font=('impress', 13), relief=tk.FLAT, command=exittomain)
exitBtn.grid(column=3, row=4, sticky=tk.E, padx=5, pady=5)



rootSearchBill.mainloop()