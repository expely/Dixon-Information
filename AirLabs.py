import pickle
import subprocess
import tkinter as tk
import time

import main

import datetime


def start(labStart, labEnd):
    start.timesToRun = labStart - labEnd + 1
    start.labStart = labStart
    start.labEnd = labEnd
    windows()

def windows():
    windows.window = tk.Tk()

    labelN = tk.Label(text='lab# '+str(start.labStart)).grid(row=1)

    labelN = tk.Label(text='Sample Name').grid(row=2)
    entryN = tk.Entry(bd=5)
    entryN.grid(row=2, column=1)

    labelS = tk.Label(text='Sample Description').grid(row=3)
    entryS = tk.Entry(bd=5)
    entryS.grid(row=3, column=1)

    labelD = tk.Label(text='Date Sampled').grid(row=4)
    entryD = tk.Entry(bd=5)
    entryD.grid(row=4, column=1)

    labelTStart = tk.Label(text="Time Started").grid(row=5)
    entryTStart = tk.Entry(bd=5)
    entryTStart.grid(row=5, column=1)

    labelTEnd = tk.Label(text='Time Ended').grid(row=5, column=2)
    entryTEnd = tk.Entry(bd=5)
    entryTEnd.grid(row=5, column=3)

    labelF = tk.Label(text='Flow').grid(row=6)
    entryF = tk.Entry(bd=5)
    entryF.grid(row=6, column=1)

    def calculate(event):
        calculatedV = (float(entryTEnd.get()) - float(entryTStart.get())) * float(entryF.get())
        labelCalculated = tk.Label(text='Calculated Volume: ' + str(calculatedV)).grid(row=7, column=2)

        labelCorrect = tk.Label(text='Correct? Y/N').grid(row=1, column=1)
        entryCorrect = tk.Entry(bd=5)
        entryCorrect.grid(row=1, column=2)
        entryCorrect.bind('Y' + '<Return>' or 'y' + '<Return>', save)


    labelV = tk.Label(text='Volume').grid(row=7)
    entryV = tk.Entry(bd=7)
    entryV.grid(row=7, column=1)
    entryV.bind('<Return>', calculate)


    windows.window.mainloop()

def save(event):
    start.labStart += 1
    windows.window.destroy()
    if start.labStart > start.labEnd:
        move_on()
    windows()

def move_on():
    windows.window.destroy()
    quit()