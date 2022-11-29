#sirf plus minus krne wala 
from tkinter import *
root = Tk()

root.geometry("655x333")
root.title("adition device")
num1 = Label(root,text = "First Number",font="integralcf 32 bold" )
num2 = Label(root , text = "Second Number",font="integralcf 32 bold")
num1.grid()
num2.grid()

num1value = StringVar()
num2value = StringVar()

num1entry = Entry(root , textvariable=num1value)

num2entry = Entry(root , textvariable=num2value)
num1entry.grid(row = 0,column=1)
num2entry.grid(row = 1 ,column= 1)



k = 0 




def getvals():
    V_1 = int(num1value.get())
    V_2 = int(num2value.get())
    k = V_1 + V_2
    result = Label(root,text=k,font="integralcf 32 bold" ).grid(row = 2 , column=1)






Button(text = "Submit",font="integralcf 32 bold",fg="red",command=getvals).grid(row=2)
result = Label(root,text=k,font="integralcf 32 bold" ).grid(row = 2 , column=1)




#checkbutton
happinessvalue = IntVar()

happiness = Checkbutton(text = "u happy wid dis ?",font="integralcf 20 bold",fg="green",pady = 15, variable = happinessvalue).grid(row = 3 , column=0)






root.mainloop()