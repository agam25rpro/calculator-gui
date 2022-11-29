#canvasbkchdoi
from tkinter import *
root = Tk()
canvas_width = 400
canvas_height = 800

root.geometry(f"{canvas_width}x{canvas_height}")

root.title("canvasss")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)

can_widget.pack()


can_widget.create_polygon(0, 100, 300, 0, 100, 200, fill="red")

can_widget.create_window(200, 0)

#for rect coor of top left and bottom right is requred only 
can_widget.create_rectangle(0,0,400,200,fill="grey")

can_widget.create_line(0,200,400,200,fill="purple")


root.mainloop()