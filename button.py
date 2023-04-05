<<<<<<< HEAD
from tkinter import *
root=Tk()
root.geometry("333x575")
def name():
    print("what is your name")
f1=Frame(root,bg="blue",borderwidth=4,relief=RAISED)
f1.pack(side=LEFT,anchor="nw")
b1=Button(f1,text="click here",fg="blue",command=name)
b1.pack(side=LEFT,padx=23)
b2=Button(f1,text="click here",fg="blue",command=name)
b2.pack(side=LEFT,padx=23)
b3=Button(f1,text="click here",fg="blue",command=name)
b3.pack(side=LEFT,padx=23)
=======
from tkinter import *
root=Tk()
root.geometry("333x575")
def name():
    print("what is your name")
f1=Frame(root,bg="blue",borderwidth=4,relief=RAISED)
f1.pack(side=LEFT,anchor="nw")
b1=Button(f1,text="click here",fg="blue",command=name)
b1.pack(side=LEFT,padx=23)
b2=Button(f1,text="click here",fg="blue",command=name)
b2.pack(side=LEFT,padx=23)
b3=Button(f1,text="click here",fg="blue",command=name)
b3.pack(side=LEFT,padx=23)
>>>>>>> c9620fbf3a4515d86fcebd2f69f58b69fe37309f
root.mainloop()