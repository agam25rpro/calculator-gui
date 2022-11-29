#animecon form
from tkinter import * 
root = Tk()
root.geometry("700x344")
root.title("ANIMECON FORM")
#labels
heading = Label(root,text="ANIMECON FORM",font= "integralcf 32 bold",fg = "purple",pady=15, padx=0).grid(row=0, column=1)

Name = Label(root,text="                   Name:",font="integralcf 15 bold",bg= "purple",fg="yellow").grid(row= 1,column=0)
Character = Label(root,text="            Character:",font="integralcf 15 bold",bg= "purple",fg="yellow").grid(row= 2,column=0,)
Anime = Label(root,text="                  Anime:",font="integralcf 15 bold",bg= "purple",fg="yellow").grid(row= 3,column=0)
RegistrationnNO = Label(root,text=" RegistrationNO.:",font="integralcf 15 bold",bg= "purple",fg="yellow").grid(row= 4,column=0)

#datavaluesetting
namevalue = StringVar()
Charactervalue = StringVar()
Animevalue =  StringVar()
RegistrationnNOvalue = IntVar()
waifuvalue = IntVar()



#entrys
nameentry = Entry(root,textvariable= namevalue).grid(row=1, column = 1)
characterentry = Entry(root,textvariable= Charactervalue).grid(row=2, column = 1)
animeentry = Entry(root,textvariable= Animevalue).grid(row=3, column = 1)
registrationno_entry = Entry(root,textvariable=RegistrationnNOvalue ).grid(row=4, column = 1)
waifuval = Checkbutton(text= "YOU WILL BRING YOUR OWN WAIFU", variable=waifuvalue,font="integralcf 15 bold",fg="purple")
waifuval.grid(row=5,column=1)


def submit():
    print("form submitted")
    print(f"{namevalue.get(),Charactervalue.get(),Animevalue.get(),RegistrationnNOvalue.get(),waifuvalue.get()}")

    with open("records.txt","a") as f :
        f.write(f"{namevalue.get(),Charactervalue.get(),Animevalue.get(),RegistrationnNOvalue.get(),waifuvalue.get()}\n")



submit1 = Button(text="submit",bg="purple",fg="white",command=submit,pady=15).grid(row=6,column=1)







root.mainloop()