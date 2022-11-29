#calculator

from tkinter import *
root = Tk()
root.geometry("400x625")
root.title("CALCULATOR")

root.wm_iconbitmap("images.ico")


scvalue = StringVar()
scvalue.set("")

screen = Entry(root,textvariable=scvalue,font= "integralcf 30 bold",bg="yellow")
screen.pack(fill = X, ipadx=8,pady=10,padx=10)

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()            
    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()








# 1 frame me 3 button are packed

f = Frame(root, bg = "grey")
b = Button(f,text="9",padx = 20,pady = 1,font = "integralcf 20 bold")
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1 >",click)

b = Button(f,text="8",padx = 20,pady = 1,font = "integralcf 20 bold")
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1 >",click)

b = Button(f,text="7",padx = 20,pady = 1,font = "integralcf 20 bold")
b.pack(side=LEFT,padx= 20,pady=10)
b.bind("<Button-1 >",click)

f.pack()





f = Frame(root, bg = "grey")
b = Button(f,text="6",padx = 20,pady = 1,font = "integralcf 20 bold")
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1 >",click)

b = Button(f,text="5",padx = 20,pady = 1,font = "integralcf 20 bold")
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1 >",click)

b = Button(f,text="4",padx = 20,pady = 1,font = "integralcf 20 bold")
b.pack(side=LEFT,padx= 20,pady=10)
b.bind("<Button-1 >",click)

f.pack()



f = Frame(root, bg = "grey")
b = Button(f,text="3",padx = 20,pady = 1,font = "integralcf 20 bold")
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1 >",click)

b = Button(f,text="2",padx = 20,pady = 1,font = "integralcf 20 bold")
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1 >",click)

b = Button(f,text="1",padx = 20,pady = 1,font = "integralcf 20 bold")
b.pack(side=LEFT,padx= 20,pady=10)
b.bind("<Button-1 >",click)

f.pack()




f = Frame(root, bg = "grey")
b = Button(f,text="0",padx = 21,pady = 1,font = "integralcf 20 bold")
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1 >",click)

b = Button(f,text="+",padx = 21,pady = 1,font = "integralcf 20 bold")
b.pack(side=RIGHT,padx=20,pady=10)
b.bind("<Button-1 >",click)

b = Button(f,text="-",padx = 21,pady = 1,font = "integralcf 20 bold")
b.pack(side=RIGHT,padx= 20,pady=10)
b.bind("<Button-1 >",click)

f.pack()


f = Frame(root, bg = "grey")
b = Button(f,text="*",padx = 21,pady = 1,font = "integralcf 20 bold")
b.pack(side=RIGHT,padx=20,pady=10)
b.bind("<Button-1 >",click)

b = Button(f,text="/",padx = 21,pady = 1,font = "integralcf 20 bold")
b.pack(side=RIGHT,padx=20,pady=10)
b.bind("<Button-1 >",click)

b = Button(f,text="%",padx = 21,pady = 1,font = "integralcf 20 bold")
b.pack(side=RIGHT,padx= 20,pady=10)
b.bind("<Button-1 >",click)

f.pack()




f = Frame(root, bg = "purple")
b = Button(f,text="=",padx = 20,pady = 1,font = "integralcf 20 bold")
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1 >",click)

b = Button(f,text="c",padx = 20,pady = 1,font = "integralcf 20 bold")
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1 >",click)


f.pack()










root.mainloop()