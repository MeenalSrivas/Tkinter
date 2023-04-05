<<<<<<< HEAD
from tkinter import *
root=Tk()
root.geometry("600x500")

def task():
    root=Tk()
    root.geometry=(f"{width_window}x{height_window}")

l1=Label(root,text="width")
l2=Label(root,text="height")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)

thickness=StringVar
length=StringVar

width_window=Entry(root,textvariable=thickness)
height_window=Entry(root,textvariable=length)
width_window.grid(row=0,column=1)
height_window.grid(row=1,column=1)

b1=Button(root,text="submit it",command=task)
b1.grid(row=2,column=2)

=======
from tkinter import *
root=Tk()
root.geometry("600x500")

def task():
    root=Tk()
    root.geometry=(f"{width_window}x{height_window}")

l1=Label(root,text="width")
l2=Label(root,text="height")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)

thickness=StringVar
length=StringVar

width_window=Entry(root,textvariable=thickness)
height_window=Entry(root,textvariable=length)
width_window.grid(row=0,column=1)
height_window.grid(row=1,column=1)

b1=Button(root,text="submit it",command=task)
b1.grid(row=2,column=2)

>>>>>>> c9620fbf3a4515d86fcebd2f69f58b69fe37309f
root.mainloop()