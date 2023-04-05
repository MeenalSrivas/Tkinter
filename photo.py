<<<<<<< HEAD
from tkinter import *
from PIL import Image, ImageTk
photu_root=Tk()
photu_root.geometry("770x600")

#photo= PhotoImage(file="meenu.jpg")

#FOR Jpg images

photo=Image.open("meenu.png")
image_meenu=ImageTk.PhotoImage(photo)
photo_label=Label(image=image_meenu,text="my photo",bg="blue",borderwidth=10,relief=SUNKEN)
photo_label.pack(side=LEFT,padx=2,pady=77)
photu_root.mainloop()
=======
from tkinter import *
from PIL import Image, ImageTk
photu_root=Tk()
photu_root.geometry("770x600")

#photo= PhotoImage(file="meenu.jpg")

#FOR Jpg images

photo=Image.open("meenu.png")
image_meenu=ImageTk.PhotoImage(photo)
photo_label=Label(image=image_meenu,text="my photo",bg="blue",borderwidth=10,relief=SUNKEN)
photo_label.pack(side=LEFT,padx=2,pady=77)
photu_root.mainloop()
>>>>>>> c9620fbf3a4515d86fcebd2f69f58b69fe37309f
