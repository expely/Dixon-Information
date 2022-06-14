# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import pickle
import tkinter as tk

class Customer:
    def __init__(self, code, reportName, companyName, address, city, labNumber):
        self.code = code
        self.reportName = reportName
        self.companyName = companyName
        self.address = address
        self.city = city
        self.labNumber = labNumber

cust_dict = {}
if os.path.getsize("custList") > 0:
    with open("custList", 'rb') as f:
        unpickler = pickle.Unpickler(f)
        cust_dict = unpickler.load()

if __name__ == "__main__":
    first_window = tk.Tk()


    def new_window():
        first_window.destroy()
        import customerInfo


    def new_customer():
        first_window.destroy()
        import NewCustomer

    def changeNumber():
        first_window.destroy()
        import SetBatchLab

    def remove_customer():
        first_window.destroy()
        import RemoveCustomer



    button = tk.Button(
        text="Login Batch",
        width=25,
        height=5,
        bg="black",
        fg="white",
        command=new_window
    )
    custButton = tk.Button(
        text="Add Customer",
        width=25,
        height=5,
        bg="black",
        fg="white",
        command=new_customer
    )
    removeButton = tk.Button(
        text="Remove Customer",
        width=25,
        height=5,
        bg="black",
        fg="white",
        command=remove_customer
    )
    changeButton = tk.Button(
        text="Change Batch or Lab Number",
        width=25,
        height=5,
        bg="black",
        fg="white",
        command=changeNumber
    )

    button.configure(font=("Times New Roman", 20, "bold"))
    button.pack()
    custButton.configure(font=("Times New Roman", 20, "bold"))
    custButton.pack()
    removeButton.configure(font=("Times New Roman", 20, "bold"))
    removeButton.pack()
    changeButton.configure(font=("Times New Roman", 20, "bold"))
    changeButton.pack()

    first_window.mainloop()


