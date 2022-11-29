#newone 

from tkinter import *

root = Tk()
root.geometry("1920x1080")
root.title("joooiplace")


#important label options
#text - adds the text
#bd - background 
#fg - foreground 
#font - sets the font 
#padx - x padding
#pady - y _Padding
#relief - border styiling - SUNKEN,RAISED,GROOVE,RIDGE

title_label = Label(text ='''How to be a sigma male''', bg = "yellow", fg = "black", padx =0,pady=0, font = ("integral cf bold",42,"bold"),borderwidth= 3, relief=SUNKEN  )
title_label.pack(side = TOP,fill = X)



#imp pack options(alignments sa dene me help krta h )
#side naam ka bhi h ek (top,bottom,left,right)
#fill = x (isme jo bhi h label vo x ki side me fill hotajaega when stretched)
#_label.pack(side=BOTTOM,anchor = "se",fill = X )








root.mainloop()
