from optparse import Option
from tkinter import *
from tkinter import ttk

def fill(text):
    #Numbers.pop(0)
    Numbers=[]
    for n in range(text):
        Numbers.append(n)
    drop1["values"]=Numbers
    drop1.set(Numbers[1])

def sub():
    inp=drop1.get()
    print(inp)

root=Tk()
text=StringVar()
text1=IntVar()
option1=[10,8,4,12]
Numbers=[]

drop=OptionMenu(root,text,*option1,command=fill)
drop.grid(row=1,column=1)
drop1=ttk.Combobox(root,values=Numbers)
drop1.grid(row=2,column=1)

btn=Button(root,text="sub",command=sub).grid(row=3,column=3)

root.mainloop()