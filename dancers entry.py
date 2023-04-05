<<<<<<< HEAD
from tkinter import *
root=Tk()
root.geometry("665x774")
Label(root,text="WELCOME TO THE DANCE BATTLE",font="comicsansms 10 bold").grid(row=0,column=3,pady=15)
def getvalue():
    print("submitting form")
    print(f"{name_value.get(),contact_value.get(),gender_value.get(),dance_style_value.get(),customised_costume.get()}\n")
    
    with open("dancers.txt","a") as f:
        f.write(f"{name_value.get(),contact_value.get(),gender_value.get(),dance_style_value.get(),customised_costume.get()}\n")
    
name=Label(root,text="Name")
contact=Label(root,text="contact")
gender=Label(root,text="gender")
dancestyle =Label(root,text="dancestyle")

name.grid(row=1,column=1)
contact.grid(row=2,column=1)
gender.grid(row=3,column=1)
dancestyle.grid(row=4,column=1)

name_value=StringVar()
contact_value=StringVar()
gender_value=StringVar()
dance_style_value=StringVar()
customised_costume=StringVar()

NAME=Entry(root,textvariable=name_value)
CONTACT=Entry(root,textvariable=contact_value)
GENDER=Entry(root,textvariable=gender_value)
DANCE_STYLE=Entry(root,textvariable=dance_style_value)

NAME.grid(row=1,column=2)
CONTACT.grid(row=2,column=2)
GENDER.grid(row=3,column=2)
DANCE_STYLE.grid(row=4,column=2)

#check_button
costume=Checkbutton(root,text="whether costume is required",variable=customised_costume)
costume.grid(row=6,column=3)

b1=Button(root,text="submit it",command=getvalue)
b1.grid(row=6,column=2)

=======
from tkinter import *
root=Tk()
root.geometry("665x774")
Label(root,text="WELCOME TO THE DANCE BATTLE",font="comicsansms 10 bold").grid(row=0,column=3,pady=15)
def getvalue():
    print("submitting form")
    print(f"{name_value.get(),contact_value.get(),gender_value.get(),dance_style_value.get(),customised_costume.get()}\n")
    
    with open("dancers.txt","a") as f:
        f.write(f"{name_value.get(),contact_value.get(),gender_value.get(),dance_style_value.get(),customised_costume.get()}\n")
    
name=Label(root,text="Name")
contact=Label(root,text="contact")
gender=Label(root,text="gender")
dancestyle =Label(root,text="dancestyle")

name.grid(row=1,column=1)
contact.grid(row=2,column=1)
gender.grid(row=3,column=1)
dancestyle.grid(row=4,column=1)

name_value=StringVar()
contact_value=StringVar()
gender_value=StringVar()
dance_style_value=StringVar()
customised_costume=StringVar()

NAME=Entry(root,textvariable=name_value)
CONTACT=Entry(root,textvariable=contact_value)
GENDER=Entry(root,textvariable=gender_value)
DANCE_STYLE=Entry(root,textvariable=dance_style_value)

NAME.grid(row=1,column=2)
CONTACT.grid(row=2,column=2)
GENDER.grid(row=3,column=2)
DANCE_STYLE.grid(row=4,column=2)

#check_button
costume=Checkbutton(root,text="whether costume is required",variable=customised_costume)
costume.grid(row=6,column=3)

b1=Button(root,text="submit it",command=getvalue)
b1.grid(row=6,column=2)

>>>>>>> c9620fbf3a4515d86fcebd2f69f58b69fe37309f
root.mainloop()