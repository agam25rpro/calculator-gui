#frame.py 
from tkinter import*
root = Tk()
root.geometry("655x333")
f1 = Frame(root,bg = "grey",borderwidth=6,relief = SUNKEN)
f1.pack(side = LEFT,fill = "y")

f2 = Frame(root,bg = "black",borderwidth=8,relief= SUNKEN)
f2.pack(side = TOP,fill=X)

l = Label(f1,text = "project Tkinter")
l.pack(pady = 142)

l2 = Label(f2,text = "welcome to bankai editor")
l2.pack()








root.mainloop()
