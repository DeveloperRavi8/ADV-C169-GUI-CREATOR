from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("GUI CREATOR")
root.geometry("500x500")

class CreateElement:
    def __init__(self):
        print("This is CreateElements class")
        self.numList = ["1", "2", "3", "4"]

    def createLabel(self):
        label = Label(root, text="A new label has been created using class", fg="red")
        label.pack(pady=10)

    def createButton(self):
        button = Button(root, text="Button", command=self.message)
        button.pack(pady=10)

    def createDropdown(self):
        self.numVal = StringVar()
        dropdown = ttk.Combobox(root, values=self.numList, textvariable=self.numVal, state="readonly")
        dropdown.pack(pady=10)

    def message(self):
        messagebox.showinfo("Message", "You clicked the button created using class")
    
    def choose(self):
        element = comboboxVal.get()
        if(element == "Label"):
            self.createLabel()
        elif(element == "Button"):
            self.createButton()
        elif(element == "Dropdown"):
            self.createDropdown()

comboboxText = ["Label", "Button", "Dropdown"]
comboboxVal = StringVar()
combobox = ttk.Combobox(root, state="readonly", values=comboboxText, textvariable=comboboxVal)
combobox.pack(pady=10)

instance_of_create_element = CreateElement()
button = Button(root, text="Create Element", command=instance_of_create_element.choose)
button.pack(pady=10)
root.mainloop()