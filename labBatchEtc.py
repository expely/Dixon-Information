import pickle
import subprocess
import tkinter as tk
import time

import main

import datetime

todays_date = datetime.datetime.today()
dateTime_Object = datetime.datetime.strptime(str(todays_date.month), "%m")
full_month_name = dateTime_Object.strftime("%B")

batchNumber = open('BatchNumber', 'r').read()


def start(code, address, samples):
    start.window = tk.Tk()
    start.customer = main.cust_dict[code]
    start.saveSamples = samples
    start.custCode = code
    start.address = address

    labelBatch = tk.Label(text="Batch Number: " + batchNumber, font=("Arial", 25)).grid(row=0)

    labelN = tk.Label(text=start.customer.companyName, font=("Arial", 25)).grid(row=1)
    labelLab = tk.Label(text="Lab#: "+ str(start.customer.labNumber) + " to " + str(start.customer.labNumber+samples-1), font=("Arial", 25)).grid(row=2)

    start.labelPrompt = tk.Label(text="Is this correct Y/N?", font=("Arial", 25))
    start.labelPrompt.grid(row=3)

    start.entryPrompt = tk.Entry(bd=5, font=("Arial", 25))
    start.entryPrompt.grid(row=3, column=1)
    start.entryPrompt.bind('Y'+'<Return>', Clear_Program)
    start.entryPrompt.bind('y' + '<Return>', Clear_Program)
    start.entryPrompt.bind('N'+'<Return>', go_Back)
    start.entryPrompt.bind('n' + '<Return>', go_Back)

    start.window.mainloop()

def go_Back(event):
    start.window.destroy()
    subprocess.call("customerInfo.py", shell=True)

def Clear_Program(event):
    start.entryPrompt.delete(0, 'end')
    start.labelPrompt['text'] = "Saving Program..."
    Save_Program()

def Save_Program():
    with open("BatchNumber", 'w') as f:
        newBatch = str(int(batchNumber) + 1)
        f.write(newBatch)
    with open('D:\\HOLDBAT.txt', 'w') as file:
        file.write(batchNumber)
    with open('D:\\HOLDCUST.txt', 'w') as file:
        file.write(start.customer.code)
    with open('D:\\POINTERS\\' + batchNumber + '.txt', 'w') as file:
        file.write(start.customer.code+'\n'+str(start.customer.labNumber)+'\n'+str(start.customer.labNumber+start.saveSamples-1)+'\n'+str(start.saveSamples)+'\n'+str(todays_date.year)+'-'+full_month_name+'\n'+batchNumber+'\n'+start.address)
    file = open("custList", 'wb')
    main.cust_dict[start.custCode].labNumber = start.customer.labNumber + start.saveSamples
    pickle.dump(main.cust_dict, file)
    file.close()
    start.window.destroy()