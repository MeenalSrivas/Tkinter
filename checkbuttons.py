<<<<<<< HEAD
from tkinter import *
root=Tk()
root.geometry("665x774")
Label(root,text="WELCOME TO THE DANCE BATTLE",font="comicsansms 10 bold").grid(row=0,column=3,pady=15)
name=Label(root,text="Name")
contact=Label(root,text="contact")
gender=Label(root,text="gender")
dancestyle =Label(root,text="dancestyle")

name.grid(row=1,column=1)
contact.grid(row=2,column=1)
gender.grid(row=3,column=1)
dancestyle.grid(row=4,column=1)

name_value=StringVar
contact_value=StringVar
gender_value=StringVar
dance_style_value=StringVar
customised_costume=StringVar

NAME=Entry(root,textvariable=name)
CONTACT=Entry(root,textvariable=contact)
GENDER=Entry(root,textvariable=gender)
DANCE_STYLE=Entry(root,textvariable=dancestyle)

NAME.grid(row=1,column=2)
CONTACT.grid(row=2,column=2)
GENDER.grid(row=3,column=2)
DANCE_STYLE.grid(row=4,column=2)

#check_button
costume=Checkbutton(root,text="whether costume is required")
costume.grid(row=6,column=3)

=======
from tkinter import *
root=Tk()
root.geometry("665x774")
Label(root,text="WELCOME TO THE DANCE BATTLE",font="comicsansms 10 bold").grid(row=0,column=3,pady=15)
name=Label(root,text="Name")
contact=Label(root,text="contact")
gender=Label(root,text="gender")
dancestyle =Label(root,text="dancestyle")

name.grid(row=1,column=1)
contact.grid(row=2,column=1)
gender.grid(row=3,column=1)
dancestyle.grid(row=4,column=1)

name_value=StringVar
contact_value=StringVar
gender_value=StringVar
dance_style_value=StringVar
customised_costume=StringVar

NAME=Entry(root,textvariable=name)
CONTACT=Entry(root,textvariable=contact)
GENDER=Entry(root,textvariable=gender)
DANCE_STYLE=Entry(root,textvariable=dancestyle)

NAME.grid(row=1,column=2)
CONTACT.grid(row=2,column=2)
GENDER.grid(row=3,column=2)
DANCE_STYLE.grid(row=4,column=2)

#check_button
costume=Checkbutton(root,text="whether costume is required")
costume.grid(row=6,column=3)

>>>>>>> c9620fbf3a4515d86fcebd2f69f58b69fe37309f
root.mainloop()