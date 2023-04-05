from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("689x555")
photu=Image.open("shahrukhkhan-283 passport.jpg")
photu1=Image.open("preity-zinta-k4fb.jpeg")
photo=ImageTk.PhotoImage(photu)
photo1=ImageTk.PhotoImage(photu1)
l1=Label(text="bollywood stuff",padx=70,pady=10)
l=Label(image=photo)
l2=Label(image=photo1)
l.grid(row=0,column=0)
l2.grid(row=1,column=4)
l1.grid(row=0,column=6)
root.mainloop()

