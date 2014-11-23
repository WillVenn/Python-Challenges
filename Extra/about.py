#!/usr/bin/env python3.4
from tkinter import *

#--------------------------------------
#Window shizzle

root = Tk() #Creates the root window
root.title("About Python Challenges") #Names the root window 
created above
root.geometry("600x450+250+450") #Sets the size and location of 
said created window
##root.iconbitmap("logo.png")
img = PhotoImage(file='Images/logo.png') #sets the application 
icon
root.tk.call('wm', 'iconphoto', root._w, img) #Still setting the 
icon
#---------------------------------------

#Labels
label_Intro = Label(text="This is a collection of Python 
programmes showing of the capabilities of python").pack() 
#Standard tkinter label again nothing to interesting believe me!
label_Author = Label(text="This was created by Will Venn using 
Python3.X and tkinter as the GUI modules", font=("Helvetica", 
12)).pack()
#---------------------------------------

#Buttons

button_Quit = Button(text="Quit", bd=2, command=root.quit).pack() 
#A standard packed button that quits the app with a border width 
of 2
#---------------------------------------

#Images

photo1 = PhotoImage(file="Images/aboutlogo.gif") #Sets an image on 
the window
w = Label(root, image=photo1)
w.photo = photo1
w.pack()

photo2 = PhotoImage(file="Images/tk.png") #Sets another image on 
the window
w = Label(root, image=photo2)
w.photo = photo2
w.pack()
#---------------------------------------
root.mainloop() #tells the root window to keep running after 
completed everything or until told to shutdown sing the buttons or 
force closed
