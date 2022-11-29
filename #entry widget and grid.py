#entry widget and grid 
from tkinter import *
root = Tk()

root.geometry("655x333")

user = Label(root,text = "Username")
password = Label(root,text = "Password")
user.grid()
password.grid(row = 1)

#variable classes in tkiter
# DoubleVar,StringVar,BooleanVar,IntVar


uservalue = StringVar()
passvalue = StringVar()
 

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row= 0,column= 1)
passentry.grid(row = 1,column= 1)
def getvals():
    pass
Button(text = "submit",command=getvals).grid()











root.mainloop()