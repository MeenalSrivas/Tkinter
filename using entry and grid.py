<<<<<<< HEAD
from tkinter import *
root=Tk()
root.geometry=("555x444")
def goodname():
    print(username.get())
    print(age.get())
name=Label(text="username")
age=Label(text="user age")
name.grid()
age.grid(row=2)
uservar=StringVar
agevar=StringVar
username=Entry(root,textvariable=uservar)
age=Entry(root,textvariable=agevar)
username.grid(row=0,column=1)
age.grid(row=2,column=1)
b1=Button(text="submit",bg="blue",fg="white",command=goodname)
b1.grid(row=3,column=1)
if username is "":
    print("it cannot be empty")
=======
from tkinter import *
root=Tk()
root.geometry=("555x444")
def goodname():
    print(username.get())
    print(age.get())
name=Label(text="username")
age=Label(text="user age")
name.grid()
age.grid(row=2)
uservar=StringVar
agevar=StringVar
username=Entry(root,textvariable=uservar)
age=Entry(root,textvariable=agevar)
username.grid(row=0,column=1)
age.grid(row=2,column=1)
b1=Button(text="submit",bg="blue",fg="white",command=goodname)
b1.grid(row=3,column=1)
if username is "":
    print("it cannot be empty")
>>>>>>> c9620fbf3a4515d86fcebd2f69f58b69fe37309f
root.mainloop()