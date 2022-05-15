from tkinter import *
from turtle import end_fill, width

root=Tk()
root.geometry("600x500")
f1=Frame(root,borderwidth=6)
f1.grid(row=2,columnspan=7)
Label(f1,text="Test").grid(row=3,column=1)

def do(e):
    print(listbox.get(ANCHOR))
    listbox.selection_clear(0,END)

scrollbar=Scrollbar(f1)
scrollbar.grid(column=3,sticky=E,ipady=50)
#scrollbar.grid_columnconfigure(3,weight=1)

listbox=Listbox(f1,yscrollcommand=scrollbar.set)

for i in range(350):
    listbox.insert(END,f"Iteam {i}")

listbox.grid(row=4,columnspan=3)
Entry(root).grid(row=6,column=4)
scrollbar.config(command=listbox.yview)

listbox.bind("<<ListboxSelect>>",do)


root.mainloop()