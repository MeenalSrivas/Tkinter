<<<<<<< HEAD
from tkinter import *
root=Tk()
root.geometry("500x600")

#for binding into an event you have to give def() funx one argument in it otherwise it will give an error

def task(event):
    print(f"event is being executed successfully in line{event.x} and {event.y}")
    

button=Button(root,text="click here")
button.pack()

#button.bind("<Button 1>",task)
#button.bind("<Motion>",task)
#button.bind("<B1 Motion>",task)
button.bind("<Double Button - 2>",quit)
root.mainloop()
=======
from tkinter import *
root=Tk()
root.geometry("500x600")

#for binding into an event you have to give def() funx one argument in it otherwise it will give an error

def task(event):
    print(f"event is being executed successfully in line{event.x} and {event.y}")
    

button=Button(root,text="click here")
button.pack()

#button.bind("<Button 1>",task)
#button.bind("<Motion>",task)
#button.bind("<B1 Motion>",task)
button.bind("<Double Button - 2>",quit)
root.mainloop()
>>>>>>> c9620fbf3a4515d86fcebd2f69f58b69fe37309f
