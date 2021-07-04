import tkinter as tk
from tkinter import StringVar, messagebox, ttk, END, IntVar, DISABLED, NORMAL, Button, CENTER, W,NO
import databaseConnection
from imp import reload
print("manage consumer Launched")

#Colour codes Initialization
rootBG = '#C7F3CA'
btnBG = '#82E3AC'

#root window
rootManageConsumer = tk.Tk()
MyLeftPos = int(rootManageConsumer.winfo_screenwidth() - 800) / 2
myTopPos = int(rootManageConsumer.winfo_screenheight() - 800) / 2
rootManageConsumer.geometry("%dx%d+%d+%d" % (220, 20, MyLeftPos, myTopPos))
rootManageConsumer.geometry("800x600")
rootManageConsumer.iconbitmap('images\\icons\\main.ico')
rootManageConsumer.resizable(False, False)
rootManageConsumer['background'] = rootBG
rootManageConsumer.title('Electricity Billing System')




# Database
conn = databaseConnection.getsqliteconnection()
cur = conn.cursor()


#Edit or Delete a consumer


def editConsumer():
    rootManageConsumer.destroy()

    def exit2mainWin():
        editConsumer.destroy()
    # root window
    editConsumer = tk.Tk()
    MyLeftPos = int(editConsumer.winfo_screenwidth() - 800) / 2
    myTopPos = int(editConsumer.winfo_screenheight() - 800) / 2
    editConsumer.geometry("%dx%d+%d+%d" % (220, 20, MyLeftPos, myTopPos))
    editConsumer.geometry("800x600")
    editConsumer.iconbitmap('images\\icons\\main.ico')
    editConsumer.resizable(False, False)
    editConsumer['background'] = rootBG
    editConsumer.title('Electricity Billing System')


    global txt_consumerNameEditor
    global txt_consumermobilenoEditorl
    global txt_consumerEmailEditorl
    global txt_consumerAddressEditorl

    # # input variables for Tk
    # consumerfullnameEditor = StringVar()
    # consumermobilenoEditor = StringVar()
    # consumeremailEditor = StringVar()
    # consumeraddressEditor = StringVar()

    cur.execute("SELECT * from consumerDetails where meterNo=?", (selectConsumerEntry.get()))
    selectedConsumer = cur.fetchall()

    # editConsumerframe

    editConsumerframe = tk.Frame(editConsumer, bg=rootBG)
    editConsumerframe.pack(padx=100, pady=50, expand="yes", fill="both")
    editConsumerframe.columnconfigure(0, weight=1)

    # consumer Login Heading
    editConsumer_label = tk.Label(editConsumerframe, text="EDIT CONSUMER DETAILS", font=("impress", 25, "bold"), bg=rootBG)
    editConsumer_label.grid(column=0, row=0, columnspan=4, padx=10, pady=20)

    # consumer Name
    consumerNameEditor = tk.Label(editConsumerframe, text="Full Name :", bg=rootBG, font=15)
    consumerNameEditor.grid(column=0, row=1, sticky=tk.W, padx=10, pady=20)
    txt_consumerNameEditor = tk.Entry(editConsumerframe,width=60, relief=tk.FLAT)
    txt_consumerNameEditor.grid(column=1, row=1, columnspan=3, sticky=tk.W, padx=10, pady=20)

    # consumermobileno
    consumermobilenoEditorl = tk.Label(editConsumerframe, text="Mobile Number :", bg=rootBG, font=15)
    consumermobilenoEditorl.grid(column=0, row=2, sticky=tk.W, padx=10, pady=20)
    txt_consumermobilenoEditorl = tk.Entry(editConsumerframe, width=60, relief=tk.FLAT)
    txt_consumermobilenoEditorl.grid(column=1, row=2, columnspan=3, sticky=tk.W, padx=10, pady=20)

    # consumerEmail
    consumerEmailEditorl = tk.Label(editConsumerframe, text="Email :", bg=rootBG, font=15)
    consumerEmailEditorl.grid(column=0, row=3, sticky=tk.W, padx=10, pady=20)
    txt_consumerEmailEditorl = tk.Entry(editConsumerframe, width=60, relief=tk.FLAT)
    txt_consumerEmailEditorl.grid(column=1, row=3, columnspan=3, sticky=tk.W, padx=10, pady=20)

    # consumerAddress
    consumerAddressEditorl = tk.Label(editConsumerframe, text="Full Address :", bg=rootBG, font=15)
    consumerAddressEditorl.grid(column=0, row=4, sticky=tk.W, padx=10, pady=20)
    txt_consumerAddressEditorl = tk.Entry(editConsumerframe,width=60, relief=tk.FLAT)
    txt_consumerAddressEditorl.grid(column=1, row=4, columnspan=3, sticky=tk.W, padx=10, pady=20)

    def clear_data():
        txt_consumerNameEditor.delete(0, END)
        txt_consumermobilenoEditorl.delete(0, END)
        txt_consumerEmailEditorl.delete(0, END)
        txt_consumerAddressEditorl.delete(0, END)
    def saveEditedConsumer():
        cur = conn.cursor()
        cur.execute("""UPDATE consumerDetails SET
                    consumerFullname = :consumerfullname1,
                    consumerMobileNO = :consumermobileno1,
                    consumerEmail = :consumeremail1,
                    consumerAddress = :consumeraddress1
                    WHERE meterNo=:meternumber""",
                    {'consumerfullname1': txt_consumerNameEditor.get(),
                    'consumermobileno1': txt_consumermobilenoEditorl.get(),
                    'consumeremail1': txt_consumerEmailEditorl.get(),
                     'consumeraddress1': txt_consumerAddressEditorl.get(),
                     'meternumber': selectConsumerEntry.get() })
        # query = (
        #     'UPDATE consumerDetails SET (consumerFullname, consumerMobileNO, consumerEmail, consumerAddress)'
        #     'values (:consumerfullname1, :consumermobileno1, :consumeremail1, :consumeraddress1);')
        # params = {
        #
        # }

        conn.commit()
        messagebox.showinfo("Success !", "Comsumer Details Updates!")
        clear_data()
        editConsumer.destroy()
        import manageConsumers

    # ====DataBase==
    for consumer in selectedConsumer:
        txt_consumerNameEditor.insert(0, consumer[1])
        txt_consumermobilenoEditorl.insert(0, consumer[2])
        txt_consumerEmailEditorl.insert(0, consumer[3])
        txt_consumerAddressEditorl.insert(0, consumer[4])

    def deleteConsumer():
        cur.execute("DELETE from consumerDetails where meterNo=?", (selectConsumerEntry.get()))
        messagebox.showinfo("Success !", "Comsumer Details Deleted!")
        conn.commit()
        editConsumer.destroy()
        import manageConsumers

    #Update Details Button
    editConsumerBtn = Button(editConsumerframe, text="Save Details", foreground="black", bg=btnBG,
                            activebackground=rootBG, width=30, height=3, font=('impress', 13), relief=tk.FLAT,command=saveEditedConsumer)
    editConsumerBtn.grid(column=0, row=6, columnspan=2, sticky=tk.W, padx=5, pady=50)

    # Update Details Button
    deleteConsumerBtn = Button(editConsumerframe, text="Delete Consumer", foreground="black", bg=btnBG,
                             activebackground=rootBG, width=20, height=3, font=('impress', 13), relief=tk.FLAT,
                             command=deleteConsumer)
    deleteConsumerBtn.grid(column=2, row=6, sticky=tk.W, padx=5, pady=50)

    # Exit Button
    exitBtn = Button(editConsumerframe, text="Exit", foreground="black", bg=btnBG, activebackground="lightgrey",
                     width=26, height=3, font=('impress', 13), relief=tk.FLAT, command=exit2mainWin)
    exitBtn.grid(column=3, row=6, sticky=tk.E, padx=5, pady=5)



def exitmainWin():
    rootManageConsumer.destroy()
    import menu
    reload(menu)

#frame for Contraints
mngConsumer= tk.Frame(rootManageConsumer, bg=rootBG)
mngConsumer.pack(padx= 0, pady=20)
mngConsumer.columnconfigure(0, weight=1)
#label
BillGenerate_label = tk.Label(mngConsumer, text="All Consumers", font=("impress", 20,"bold"), bg=rootBG)
BillGenerate_label.grid(column=0, row=0,columnspan=4, padx=10, pady=20)

#Treeview to View All The Consumers
consumerTree = ttk.Treeview(mngConsumer)

#defining Coloumns
consumerTree['columns'] = ("Meter No","Full Name", "Mobile Number","Email Address","Address")

#formating the coloumns
consumerTree.column("#0", width=0, stretch=NO)
consumerTree.column("Meter No",anchor=tk.CENTER, width=120)
consumerTree.column("Full Name", anchor=tk.W, width=120)
consumerTree.column("Mobile Number", anchor=W, width=120)
consumerTree.column("Email Address", anchor=W, width=120)
consumerTree.column("Address", anchor=W, width=120)

#Headings for Treeviews
consumerTree.heading("#0", text="",anchor = tk.W)
consumerTree.heading("Meter No",text="Meter No",anchor=tk.CENTER)
consumerTree.heading("Full Name", text="Full Name",anchor=tk.W)
consumerTree.heading("Mobile Number", text="Mobile Number",anchor=W)
consumerTree.heading("Email Address", text="Email Address",anchor=W)
consumerTree.heading("Address", text="Address",anchor=W)
#positioning Treeview
consumerTree.grid(row=1,column=0,columnspan=4, ipadx= 50, ipady =50)
# Add Data from DB
cur.execute("SELECT * from consumerDetails")
rows = cur.fetchall()
count = 0
for row in rows:
    consumerTree.insert(parent='', index='end', iid=count,text="", values=(rows[count]))
    count +=1


# consumer Name
selectConsumerEntry = StringVar()
selectConsumer = tk.Label(mngConsumer, text="Enter Meter Number:", bg=rootBG, font=15)
selectConsumer.grid(column=0, row=2, sticky=tk.E, padx=10, pady=20)
txt_selectConsumer = tk.Entry(mngConsumer, textvar=selectConsumerEntry, width=20, relief=tk.FLAT)
txt_selectConsumer.grid(column=1, row=2, sticky=tk.W, padx=10, pady=20)

# Selected Row Button
editConsumerBtn = Button(mngConsumer, text="EDIT CONSUMER DETAILS", foreground="black", bg=btnBG,
                        activebackground=rootBG, width=25, height=3, font=('impress', 13), relief=tk.FLAT,command=editConsumer)
editConsumerBtn.grid(column=2, row=2,columnspan=1, padx=10, pady=20)


# Exit Button
exitBtn = Button(mngConsumer, text="Exit", foreground="black", bg=btnBG, activebackground="lightgrey",
                 width=10, height=3, font=('impress', 13), relief=tk.FLAT, command=exitmainWin)
exitBtn.grid(column=3, row=2, sticky=tk.E, padx=5, pady=5)





# consumerTree.grid(row=0, coloumn=0)
rootManageConsumer.mainloop()