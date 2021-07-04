import emailBill
import sqlite3
import tkinter as tk
from tkinter import StringVar, messagebox, ttk, END, IntVar, DISABLED, NORMAL, Button, W
from datetime import  datetime
import databaseConnection
from imp import reload

print("Add consumer Launched")

#Colour codes Initialization
rootBG = '#C7F3CA'
btnBG = '#82E3AC'

#root window
rootBillGenerate = tk.Tk()
MyLeftPos = int(rootBillGenerate.winfo_screenwidth() - 800) / 2
myTopPos = int(rootBillGenerate.winfo_screenheight() - 800) / 2
rootBillGenerate.geometry("%dx%d+%d+%d" % (220, 20, MyLeftPos, myTopPos))
rootBillGenerate.geometry("800x450")
rootBillGenerate.iconbitmap('images\\icons\\main.ico')
rootBillGenerate.resizable(False, False)
rootBillGenerate['background'] = rootBG
rootBillGenerate.title('Electricity Billing System')

#variables for SQL Entery
meterNoEntry=  StringVar()
unitConsumedEntry=IntVar()


def enterDBBills():
    tempunits = unitConsumedEntry.get()
    meternumber= meterNoEntry.get()
    finalbillamount = tempunits * 8
    now = datetime.now()
    creationTime = now.strftime("%d/%m/%y")

    if unitConsumedEntry.get() == "" or meterNoEntry.get() == "":
        messagebox.showerror("Error !", "All Fields are Required !")
    else:
        conn = sqlite3.connect('ebsDatabase.sqlite')
        try:
            cur = conn.cursor()

            cur.execute("select * from consumerDetails where meterNo=?", (meterNoEntry.get(),))

            row = cur.fetchone()
            if row != None:
                cur.execute(
                    'INSERT INTO bills(meterNo,unitConsumed, billAmount,creationDate) VALUES(?,?,?, ?) returning billNo',
                    (meterNoEntry.get(), unitConsumedEntry.get(), finalbillamount, creationTime))
                billnodb = cur.fetchall()
                conn.commit()
                selectBillnoEntry = billnodb[0][0]
                clearEntries()
                # Bill Slip and Send through Email

                billslip = tk.Tk()
                MyLeftPos = int(billslip.winfo_screenwidth() - 800) / 2
                myTopPos = int(billslip.winfo_screenheight() - 800) / 2
                billslip.geometry("%dx%d+%d+%d" % (220, 20, MyLeftPos, myTopPos))
                billslip.geometry("400x600")
                billslip.iconbitmap('images\\icons\\main.ico')
                billslip.resizable(False, False)
                billslip['background'] = rootBG
                billslip.title('Electricity Billing System')

                # DaataBase Connectivity
                conn = databaseConnection.getsqliteconnection()
                cur = conn.cursor()
                cur.execute("SELECT * from consumerDetails WHERE meterNo=?", (meternumber))
                rows = cur.fetchall()
                count = 0
                BillSlipframe = tk.Frame(billslip, bg=rootBG)
                BillSlipframe.pack(padx=20, pady=20, expand="yes", fill="both")
                BillSlipframe.columnconfigure(0, weight=1)
                # consumer Login Heading
                BillGenerated = tk.Label(BillSlipframe, text="BILL GENERATED", font=("impress", 15, "bold"), bg=rootBG)
                BillGenerated.grid(column=0, row=0, columnspan=3, padx=10, pady=10)
            else:
                txt_meterNol.delete(0, END)
                messagebox.showerror("Error !", " Enter a Valid Meter Number")

        except sqlite3.Error as error:
            print("Problem with SQlite table", error)
        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")

    def sendemailBill():
        emailBill.sendEmail(selectBillnoEntry)

    for row in rows:
        meterNole = str(row[0])
        namele = str(row[1])
        mobileNole = str(row[2])
        emaille = str(row[3])
        addressle = str(row[4])


        meterNol = tk.Label(BillSlipframe, font=("impress",12, "bold"), bg=rootBG, text=f'Meter Number : {row[0]}')
        meterNol.grid(column=0, row=2, sticky=W, columnspan=4, padx=10, pady=10)
        namel = tk.Label(BillSlipframe, text=f'Costumer Name : {row[1]}', font=("impress",12, "bold"), bg=rootBG)
        namel.grid(column=0, row=3, columnspan=3, padx=10, pady=10, sticky=W)
        mobileNol = tk.Label(BillSlipframe, text=f'Mobile Number: {row[2]}', font=("impress",12, "bold"), bg=rootBG)
        mobileNol.grid(column=0, row=4, columnspan=3, padx=10, pady=10, sticky=W)
        emaill = tk.Label(BillSlipframe, text=f'Email : {row[3]}', font=("impress",12, "bold"), bg=rootBG)
        emaill.grid(column=0, row=5, columnspan=3, padx=10, pady=10, sticky=W)
        addressl = tk.Label(BillSlipframe, text=f'Address : {row[4]}', font=("impress",12, "bold"), bg=rootBG)
        addressl.grid(column=0, row=6, columnspan=3, padx=10, pady=10, sticky=W)
        unitsl = tk.Label(BillSlipframe, text=f'Units Consumed : {tempunits}', font=("impress",12, "bold"), bg=rootBG)
        unitsl.grid(column=0, row=7, columnspan=3, padx=10, pady=10, sticky=W)
        datel = tk.Label(BillSlipframe, text=f'Bill Generated On : {creationTime}', font=("impress",12, "bold"), bg=rootBG)
        datel.grid(column=0, row=8, columnspan=3, padx=10, pady=10, sticky=W)
        Ratel = tk.Label(BillSlipframe, text=f'Rate : 8 ₹ per Unit', font=("impress",12, "bold"), bg=rootBG)
        Ratel.grid(column=0, row=9, columnspan=3, padx=10, pady=10, sticky=W)
        totalBilll = tk.Label(BillSlipframe, text=f'Total Ammount : {finalbillamount} ₹', font=("impress",12, "bold"), bg=rootBG)
        totalBilll.grid(column=0, row=10, columnspan=3, padx=10, pady=10, sticky=W)

        emailBillBtn = Button(BillSlipframe, text="Email Bill", foreground="black", bg=btnBG, activebackground=rootBG,
                              width=35, height=3, font=('impress', 13), relief=tk.FLAT, command=sendemailBill)
        emailBillBtn.grid(column=0, row=11, columnspan=2, sticky=tk.W, padx=5, pady=10)

        exittBtn = Button(BillSlipframe, text="Exit", foreground="black", bg=btnBG, activebackground="lightgrey",
                         width=20, height=3, font=('impress', 13), relief=tk.FLAT, command=billslip.destroy)
        exittBtn.grid(column=2, row=11, sticky=tk.E, padx=5, pady=10)
        count += 1

def mainWin():
    rootBillGenerate.destroy()
    import menu
    reload(menu)

#
def clearEntries():
    txt_meterNol.delete(0,10)
    txt_unitConsumedl.delete(0,10)

# BillGenerateframe

BillGenerateframe = tk.Frame(rootBillGenerate, bg=rootBG)
BillGenerateframe.pack(padx= 100, pady=50, expand="yes", fill="both")
BillGenerateframe.columnconfigure(0, weight=1)

#consumer Login Heading
BillGenerate_label = tk.Label(BillGenerateframe, text="GENERATE BILL", font=("impress", 25,"bold"), bg=rootBG)
BillGenerate_label.grid(column=0, row=0,columnspan=4, padx=10, pady=20)

#Meter Number

meterNol = tk.Label(BillGenerateframe, text="Meter Number :",  bg=rootBG, font=15)
meterNol.grid(column=0, row=1,sticky=tk.W, padx=10, pady=20)

txt_meterNol = tk.Entry(BillGenerateframe, textvar=meterNoEntry, width=60, relief=tk.FLAT)
txt_meterNol.grid(column=1, row=1, columnspan=3, sticky=tk.W,padx=10, pady=20)

#Unit Consumed

unitConsumedl = tk.Label(BillGenerateframe, text="Units Consumed :",  bg=rootBG, font=15)
unitConsumedl.grid(column=0, row=2,sticky=tk.W, padx=10, pady=20)

txt_unitConsumedl = tk.Entry(BillGenerateframe, textvar=unitConsumedEntry, width=60, relief=tk.FLAT)
txt_unitConsumedl.grid(column=1, row=2, columnspan=3, sticky=tk.W,padx=10, pady=20)

#register Button
generateBillBtn = Button(BillGenerateframe, text="Generate", foreground="black", bg=btnBG, activebackground=rootBG,width=35, height=3, font= ('impress' ,13), relief=tk.FLAT, command= enterDBBills)
generateBillBtn.grid(column=0, row=4,columnspan=4,sticky= tk.W, padx=5, pady=50)

#Exit Button
exitBtn = Button(BillGenerateframe, text="Exit", foreground="black", bg=btnBG, activebackground="lightgrey",width=26, height=3, font= ('impress' ,13), relief=tk.FLAT, command= mainWin)
exitBtn.grid(column=3, row=4, sticky=tk.E, padx=5, pady=5)



rootBillGenerate.mainloop()
