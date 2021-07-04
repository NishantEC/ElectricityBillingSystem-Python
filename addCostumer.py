
import sqlite3
import tkinter as tk
from tkinter import StringVar, messagebox, ttk, END, IntVar, DISABLED, NORMAL, Button
from imp import reload




print("Add consumer Launched")

#Colour codes Initialization
rootBG = '#C7F3CA'
btnBG = '#82E3AC'

#root window
rootAddConsumer = tk.Tk()
MyLeftPos = int(rootAddConsumer.winfo_screenwidth() - 800) / 2
myTopPos = int(rootAddConsumer.winfo_screenheight() - 800) / 2
rootAddConsumer.geometry("%dx%d+%d+%d" % (220, 20, MyLeftPos, myTopPos))
rootAddConsumer.geometry("800x600")
rootAddConsumer.iconbitmap('images\\icons\\main.ico')
rootAddConsumer.resizable(False, False)
rootAddConsumer['background'] = rootBG
rootAddConsumer.title('Electricity Billing System')

#input variables for Tk

consumerfullname = StringVar()
consumermobileno = StringVar()
consumeremail = StringVar()
consumeraddress = StringVar()


#functons for validating and saving the Entries





def entry_consumer():
    print(consumerfullname.get(), consumermobileno.get(), consumeremail.get(),consumeraddress.get())

    if consumerfullname.get() == "" or consumermobileno.get() == "" or consumeremail.get() == ""or consumeraddress.get() == "":
        messagebox.showerror("Error !", "All Fields are Required !")
    else:
        import databaseConnection
        conn = databaseConnection.getsqliteconnection()
        try:
            cur = conn.cursor()

            cur.execute("select * from consumerDetails where consumerMobileNo=?", (consumermobileno.get(),))

            row = cur.fetchone()
            if row != None:
                txt_consumermobilenol.delete(0, END)
                messagebox.showerror("Error !", "consumer ID Already Exists ! Try with another one.")
            else:

                query = ('insert into consumerDetails(consumerFullname, consumerMobileNO, consumerEmail, consumerAddress)'
                         'values (:consumerfullname1, :consumermobileno1, :consumeremail1, :consumeraddress1);')
                params = {
                    'consumerfullname1': consumerfullname.get(),
                    'consumermobileno1': consumermobileno.get(),
                    'consumeremail1': consumeremail.get(),
                    'consumeraddress1': consumeraddress.get(),
                }

                conn.execute(query, params)
                conn.commit()
                messagebox.showinfo("Success !", "Comsumer Added!")

        except sqlite3.Error as error:
            print("Problem with SQlite table", error)
        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")



def mainWin():
    rootAddConsumer.destroy()
    import menu
    reload(menu)


# AddConsumerframe

AddConsumerframe = tk.Frame(rootAddConsumer, bg=rootBG)
AddConsumerframe.pack(padx= 100, pady=50, expand="yes", fill="both")
AddConsumerframe.columnconfigure(0, weight=1)

#consumer Login Heading
AddConsumer_label = tk.Label(AddConsumerframe, text="ADD CONSUMER", font=("impress", 25,"bold"), bg=rootBG)
AddConsumer_label.grid(column=0, row=0,columnspan=4, padx=10, pady=20)

#consumer Name
consumerName = tk.Label(AddConsumerframe, text="Full Name :",  bg=rootBG, font=15)
consumerName.grid(column=0, row=1,sticky=tk.W, padx=10, pady=20)
txt_consumerName = tk.Entry(AddConsumerframe, textvar=consumerfullname, width=60, relief=tk.FLAT)
txt_consumerName.grid(column=1, row=1, columnspan=3, sticky=tk.W,padx=10, pady=20)

#consumermobileno
consumermobilenol = tk.Label(AddConsumerframe, text="Mobile Number :",  bg=rootBG, font=15)
consumermobilenol.grid(column=0, row=2,sticky=tk.W, padx=10, pady=20)
txt_consumermobilenol = tk.Entry(AddConsumerframe, textvar=consumermobileno, width=60, relief=tk.FLAT)
txt_consumermobilenol.grid(column=1, row=2, columnspan=3, sticky=tk.W,padx=10, pady=20)

#consumerEmail
consumerEmaill = tk.Label(AddConsumerframe, text="Email :",  bg=rootBG, font=15)
consumerEmaill.grid(column=0, row=3,sticky=tk.W, padx=10, pady=20)
txt_consumerEmaill = tk.Entry(AddConsumerframe, textvar=consumeremail, width=60, relief=tk.FLAT)
txt_consumerEmaill.grid(column=1, row=3, columnspan=3, sticky=tk.W,padx=10, pady=20)


#consumerAddress
consumerAddressl = tk.Label(AddConsumerframe, text="Full Address :",  bg=rootBG, font=15)
consumerAddressl.grid(column=0, row=4,sticky=tk.W, padx=10, pady=20)
txt_consumerAddressl = tk.Entry(AddConsumerframe, textvar=consumeraddress, width=60, relief=tk.FLAT)
txt_consumerAddressl.grid(column=1, row=4, columnspan=3, sticky=tk.W,padx=10, pady=20)





#register Button
AddConsumerBtn = Button(AddConsumerframe, text="Save Details", foreground="black", bg=btnBG, activebackground=rootBG,width=35, height=3, font= ('impress' ,13), relief=tk.FLAT, command= entry_consumer)
AddConsumerBtn.grid(column=0, row=6,columnspan=4,sticky= tk.W, padx=5, pady=50)

#Exit Button
exitBtn = Button(AddConsumerframe, text="Exit", foreground="black", bg=btnBG, activebackground="lightgrey",width=26, height=3, font= ('impress' ,13), relief=tk.FLAT, command= mainWin)
exitBtn.grid(column=3, row=6, sticky=tk.E, padx=5, pady=5)



rootAddConsumer.mainloop()
