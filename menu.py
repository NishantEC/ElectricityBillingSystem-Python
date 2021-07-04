# importing
import tkinter as tk
from tkinter import Tk, Menu, messagebox, LEFT, RIGHT, TOP, BOTTOM, Button
from tkinter.messagebox import showerror, showwarning, showinfo
from imp import reload

#Colour codes Initialization
rootBG = '#C7F3CA'
btnBG = '#82E3AC'

# root window
rootMain = tk.Tk()
MyLeftPos = int(rootMain.winfo_screenwidth() - 1200) / 10
myTopPos = int(rootMain.winfo_screenheight() - 650) / 3
rootMain.geometry("%dx%d+%d+%d" % (800, 500, MyLeftPos, myTopPos))
rootMain.geometry("350x700")
rootMain.iconbitmap('images\\icons\\main.ico')
rootMain.resizable(False, False)
rootMain['background'] = rootBG
rootMain.title('Electricity Billing System')
#root_userlogin.state('zoomed')

def loginWin():
    rootMain.destroy()
    import login
    reload(login)

def openAddCostumer():
    rootMain.destroy()
    import addCostumer
    reload(addCostumer)

def openManageCostumer():
    rootMain.destroy()
    import manageConsumers
    reload(manageConsumers)

def openBillGenerator():
    rootMain.destroy()
    import billGenerate
    reload(billGenerate)

def openSearchBill():
    rootMain.destroy()
    import searchBill
    reload(searchBill)




#MenuBarframe
menuBar = tk.Frame(rootMain, bg=rootBG)
menuBar.pack( fill= 'both', padx= 0, pady=0)

#menu Label
menul = tk.Label(menuBar, text="MENU", font=("impress", 18,"bold"), bg=rootBG)
menul.pack(side=TOP, padx=10, pady=50)
def about():
    messagebox.showinfo("About", "This Program is developed by Group-16\n\n\t-Nishant Gupta(0905EC191016)\n\n\t-Piyush Anchalia(0905EC191018)\n\n\t-Shiva Bhodoriya(0905EC191024)\n\n\t-sapna Suman(0905EC191021)")
#menu Btns

genBillBtn = Button(menuBar, text="Generate Bill", foreground="black",bg=btnBG, activebackground=rootBG, width=20, height=3, font= ('impress' ,13), relief=tk.FLAT, command= openBillGenerator)
searchBillBtn = Button(menuBar, text="Search Bill", foreground="black", bg=btnBG, activebackground=rootBG,width=20, height=3, font= ('impress' ,13),relief=tk.FLAT, command=openSearchBill)
addCostumerBtn = Button(menuBar, text="Add Costumer", foreground="black", bg=btnBG, activebackground=rootBG,width=20, height=3, font= ('impress' ,13),relief=tk.FLAT , command= openAddCostumer)
manageCostumersBtn = Button(menuBar, text="Manage Costumers", foreground="black", bg=btnBG, activebackground=rootBG,width=20, height=3, font= ('impress' ,13),relief=tk.FLAT,command=openManageCostumer)
logoutBtn = Button(menuBar, text="Logout", foreground="black",bg=btnBG,activebackground=rootBG, width=20, height=3, font= ('impress' ,13), relief=tk.FLAT, command=loginWin)
exitBtn = Button(menuBar, text="Exit", foreground="black", bg=btnBG, activebackground=rootBG,width=20, height=3, font= ('impress' ,13), relief=tk.FLAT, command= rootMain.destroy)
aboutBtn = Button(menuBar, text="About", foreground="black", bg=btnBG, activebackground=rootBG,width=20, height=3, font= ('impress' ,13), relief=tk.FLAT, command=about)

genBillBtn.pack( padx= 2,pady= 1)
searchBillBtn.pack(padx= 2,pady= 1)
addCostumerBtn.pack(padx= 2,pady= 1)
manageCostumersBtn.pack(padx= 2,pady= 1)
logoutBtn.pack(padx= 1,pady= 2)
exitBtn.pack(padx= 1,pady= 2)
aboutBtn.pack(padx= 1,pady= 2)

rootMain.mainloop()