from tkinter import *
from PIL import Image,ImageTk

root = Tk()

#widht x hieght

root.geometry("500x500")

#width,hieght

root.minsize(200,100)



label1 = Label(text = "ayo u seeing dis" )
label1.pack()

#only works for png images 

photo1 = PhotoImage(file ="images.png" )
u_label = Label(image = photo1 )
u_label.pack()

#for jpg images diff procedure 

image = Image.open("lucy-cyberpunk-edgerunners-art-4k-wallpaper-uhdpaper.com-6021i.jpg")
photo = ImageTk.PhotoImage(image)
u_label = Label(image = photo )
u_label.pack()








root.mainloop()
