import pickle
import subprocess
import tkinter as tk

import main

window = tk.Tk()
window.lift()
window.attributes("-topmost", True)
window.after(1, lambda: window.focus_force())

labelN = tk.Label(text="Code")
labelN.grid(row=0)
entryN = tk.Entry(bd=5)
entryN.grid(row=0, column=1)

labelA = tk.Label(text="Address")
labelA.grid(row=1)
entryA = tk.Entry(bd=5)
entryA.grid(row=1, column=1)

labelRN = tk.Label(text="Report to be sent to")
labelRN.grid(row=2)
entryRN = tk.Entry(bd=5)
entryRN.grid(row=2, column=1)

labelCN = tk.Label(text="Company Name")
labelCN.grid(row=3)
entryCN = tk.Entry(bd=5)
entryCN.grid(row=3, column=1)

labelC = tk.Label(text="City")
labelC.grid(row=4)
entryC = tk.Entry(bd=5)
entryC.grid(row=4, column=1)

def finish():
    newCustomer = main.Customer(entryN.get(), entryRN.get(), entryCN.get(), entryA.get(), entryC.get(), 1)
    file = open("custList", 'wb')
    main.cust_dict[newCustomer.code] = newCustomer
    pickle.dump(main.cust_dict, file)
    file.close()
    with open('D:\\hold\\template\\' + newCustomer.code +'.txt', 'w') as file:
        file.write('Mr. ' + newCustomer.reportName+'\n' + newCustomer.companyName+'\n'+newCustomer.address+'\n'+newCustomer.city)
    window.destroy()
    subprocess.call("main.py", shell=True)

button = tk.Button(
    text="Finish",
    width=25,
    height=5,
    bg="black",
    fg="white",
    command=finish
)

button.grid(row=5)


window.mainloop()