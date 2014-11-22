#!/usr/bin/env python3.4
import sys
from tkinter import *
import os
import subprocess
#----------------------------------------------

#Functions below
def chosendropdown(self): #Functions for selecting the challenge

	selected = set_variable.get()

	if selected == "Challenge_1":
		print("ENTERED IF STATEMENT")
		##subprocess.Popen(["chll1.py"])
		##os.popen("python.exe")
		subprocess.call(['python', 'Challenges/chll1.py'])
		print ("Launched Challenge 1")

	else:
		##print (Dropdown)
		subprocess.call(['python', 'ERROR.py'])
		##subprocess.call(["python3", "chll1.py"])
		##print ("Should have launched...")


def about(): #Function for opening my About app
	print ("About was clicked")
	print ("Launching about app")
	subprocess.call(['python', 'about.py'])






#----------------------------------------------

#Window creation/settings
root = Tk() #Creating the root window
root.geometry("850x600+250+450") #Setting the size and location of 
the window
root.title("Python Challenges v1.0") #Setting the window title
img = PhotoImage(file='logo.png') #Setting the application icon
root.tk.call('wm', 'iconphoto', root._w, img) #setting icon 
still...
#----------------------------------------------

#Labels
label_Welcome = Label(text="Welcome To Will's Python Challenge 
Menu", fg="purple", font=("Helvetica", 16)).pack() #Standard label 
just changed font and size
label_Choose = Label(text="Please Choose a Challenge From The 
Dropdown List Below", font=("Helvetica", 14)).pack()

label_Drop = Label(text="Which Challenge Would you Like? ").pack()
set_variable = StringVar(root) #Creates a string variable for sets 
it to 'select a challenge for my dropdown box
set_variable.set("Select a Challenge!")
#----------------------------------------------

#Dropdown
Dropdown = OptionMenu(root, set_variable, "Challenge_1", 
"Challenge_2", "Challenge 3", "Challenge 4", "Challenge 5", 
"Challenge 6", "Challenge 7", "Challenge 8", "Challenge 9", 
"Challenge 10", "And more will come", command=chosendropdown)
Dropdown.pack()
#----------------------------------------------

testvar = "Challenge_1" #Random test variables
print (testvar)
#----------------------------------------------



#----------------------------------------------

#Images
photo = PhotoImage(file="Images/pythonlogo.png") #Is the python 
logo in the middle/boottom of the window
w = Label(root, image=photo)
w.photo = photo
w.pack()

#----------------------------------------------

#Menubar
menubar = Menu(root) #Creates the (NON-CASCADING) menubar
menubar.add_command(label="About", command=about) #Adds an about 
button that launches my about app
menubar.add_command(label="Quit", command=root.quit) #Adds a quit 
button that closes the whole window/running processes

root.config(menu=menubar) #Configures the window to appear on the 
menu
#----------------------------------------------
#loops
root.mainloop() #tells the root window to keep running after 
completed everything or until told to shutdown sing the buttons or 
force closed
