import subprocess
from tkinter import *
import copy

import labBatchEtc
import main
import AirProgram

window = Tk()

custName = None
custAdd = None

def next_window():
    custName = entryN.get()
    custAdd = entryA.get()
    custSample = entryB.get()
    window.destroy()

    labBatchEtc.start(custName, custAdd, int(custSample))

def air_prgm():
    custName = entryN.get()
    custAdd = entryA.get()
    custSample = entryB.get()

    popup = Toplevel(window)
    popup.lift()
    popup.attributes("-topmost", True)
    popup.after(1, lambda: window.focus_force())


    def move_on(event):
        custBlanks = entryBlank.get()
        window.destroy()
        AirProgram.start(custName, custAdd, int(custSample), int(custBlanks))

    labelBlank = Label(popup, text='Number of Blanks?').grid(row=1)
    entryBlank = Entry(popup, bd=5)
    entryBlank.grid(row=1, column=1)
    entryBlank.bind('<Return>', move_on)


def checkCode():
    if entryQ.get() == 'b' or entryQ.get() == 'B':
        if entryN.get() in main.cust_dict:
            next_window()
    if entryQ.get() == 'a' or entryQ.get() == 'A':
        if entryN.get() in main.cust_dict:
            air_prgm()
    else:
        wrongCode()
def wrongCode():
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

def goBack():
    window.destroy()
    subprocess.call("main.py", shell=True)

labelN = Label(text="Code").grid(row=0)
entryN = Entry(bd=5)
entryN.grid(row=0, column=1)

labelB = Label(text="Samples").grid(row=1)
entryB = Entry(bd=5)
entryB.grid(row=1, column=1)

labelQ = Label(text="Air or Bulk?").grid(row=2)
entryQ = Entry(bd=5)
entryQ.grid(row=2, column=1)

labelA = Label(text="Address").grid(row=3)
entryA = Entry(bd=5)
entryA.grid(row=3, column=1)


buttonBack = Button(
    text="Back",
    width=25,
    height=5,
    bg="black",
    fg="white",
    command=goBack
).grid(row=4, column=0)

button = Button(
    text="Finish",
    width=25,
    height=5,
    bg="black",
    fg="white",
    command=checkCode
).grid(row=4, column=1)





window.mainloop()