import pickle
import subprocess
from tkinter import *

import main




def labNumber():
    def labEnter(event):
        if entryCode.get() in main.cust_dict:
            main.cust_dict[entryCode.get()].labNumber = int(entryLab.get())
            file = open("custList", 'wb')
            pickle.dump(main.cust_dict, file)
            file.close()
            labWindow.destroy()
            window.destroy()
            subprocess.call("main.py", shell=True)
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
            command=lambda: popup.destroy()
        ).grid(row=2)

    labWindow = Toplevel(window)
    labWindow.lift()
    labWindow.attributes("-topmost", True)
    labWindow.after(1, lambda: window.focus_force())

    labelCode = Label(labWindow,text="Customer Code")
    labelCode.grid(row=0)
    entryCode = Entry(labWindow,bd=5)
    entryCode.grid(row=0, column=1)

    labelLab = Label(labWindow,text="New Lab#")
    labelLab.grid(row=1)
    entryLab = Entry(labWindow,bd=5)
    entryLab.grid(row=1, column=1)

    entryCode.bind('<Return>', entryLab.focus_set())
    entryLab.bind('<Return>', labEnter)

def changeBatch():
    def Batch(event):
        with open("BatchNumber", 'w') as f:
            f.write(entryBatch.get())
        batchWindow.destroy()
        window.destroy()
        subprocess.call("main.py", shell=True)

    batchWindow = Toplevel(window)
    batchWindow.lift()
    batchWindow.attributes("-topmost", True)
    batchWindow.after(1, lambda: window.focus_force())

    labelBatch = Label(batchWindow,text="Change Batch# to")
    labelBatch.grid(row=0)
    entryBatch = Entry(batchWindow,bd=5)
    entryBatch.grid(row=0, column=1)
    entryBatch.bind('<Return>', Batch)


window = Tk()
window.lift()
window.attributes("-topmost", True)
window.after(1, lambda: window.focus_force())

button = Button(
    text="Change Lab#",
    width=25,
    height=5,
    bg="black",
    fg="white",
    command=labNumber
)
custButton = Button(
    text="Change Batch#",
    width=25,
    height=5,
    bg="black",
    fg="white",
    command=changeBatch
)
button.configure(font=("Times New Roman", 20, "bold"))
button.grid(row=0, column=0)
custButton.configure(font=("Times New Roman", 20, "bold"))
custButton.grid(row=0, column=1)

