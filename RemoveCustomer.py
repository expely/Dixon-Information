import pickle
import subprocess
from tkinter import *

import main

def remove_cust(event):
    enteredCode = entryDelete.get()
    if enteredCode in main.cust_dict:
        file = open("custList", 'wb')
        main.cust_dict.pop(entryDelete.get())
        pickle.dump(main.cust_dict, file)
        file.close()
        window.destroy()
        subprocess.call("main.py", shell=True)
    entryDelete.delete(0, 'end')
    popup = Toplevel(window)
    popup.lift()
    popup.attributes("-topmost", True)
    popup.after(1, lambda: window.focus_force())
    labelPop = Label(popup, text="Code not found, please try again").grid(row=1)
    removeButton = Button(
        popup,
        text="Ok",
        width=25,
        height=5,
        command= lambda: popup.destroy()
    ).grid(row=2)


window = Tk()
window.lift()
window.attributes("-topmost", True)
window.after(1, lambda: window.focus_force())

custCodes = main.cust_dict.keys()

labelCodes = Label(window, text="List of Customer Codes: " + " ".join(custCodes))
labelCodes.grid(row=1)

labelDelete = Label(window, text="Code to delete ")
labelDelete.grid(row=2)
entryDelete = Entry(window, bd=5)
entryDelete.grid(row=2, column=1)
entryDelete.bind('<Return>', remove_cust)

