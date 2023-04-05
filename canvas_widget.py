<<<<<<< HEAD
from tkinter import *
root=Tk()
canvas_width=600
canvas_heigth=400
root.geometry(f"{canvas_width}x{canvas_heigth}")

canvas_widget=Canvas(root,width=canvas_width,height=canvas_heigth)
canvas_widget.pack()
# to make line you have to use coordinates in ths order- x1,y1,x2,y2

canvas_widget.create_line(0,0,600,400)
canvas_widget.create_line(0,400,600,0)
#canvas_widget.create_line(0,200,300,0)

#in order to make rectangle specify its  parameter in order top left and bottom right 

#canvas_widget.create_rectangle(600,400,400,300)
#canvas_widget.create_text(200,200,text="this is meenal")


#canvas_widget.create_oval(0,200,300,0)

#canvas_widget.create_arc(0,0,100,200)
#canvas_widget.create_arc(0,400,600,0)

#canvas_widget.create_rectangle(100,100,200,200)

=======
from tkinter import *
root=Tk()
canvas_width=600
canvas_heigth=400
root.geometry(f"{canvas_width}x{canvas_heigth}")

canvas_widget=Canvas(root,width=canvas_width,height=canvas_heigth)
canvas_widget.pack()
# to make line you have to use coordinates in ths order- x1,y1,x2,y2

canvas_widget.create_line(0,0,600,400)
canvas_widget.create_line(0,400,600,0)
#canvas_widget.create_line(0,200,300,0)

#in order to make rectangle specify its  parameter in order top left and bottom right 

#canvas_widget.create_rectangle(600,400,400,300)
#canvas_widget.create_text(200,200,text="this is meenal")


#canvas_widget.create_oval(0,200,300,0)

#canvas_widget.create_arc(0,0,100,200)
#canvas_widget.create_arc(0,400,600,0)

#canvas_widget.create_rectangle(100,100,200,200)

>>>>>>> c9620fbf3a4515d86fcebd2f69f58b69fe37309f
root.mainloop()