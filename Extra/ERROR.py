#!/usr/bin/env python3.4
from tkinter import *
#---------------------------------------

#Functions

#---------------------------------------

root = Tk()
root.geometry("450x450")
root.title("How the hell did you get here?!")
img = PhotoImage(file='Images/logo.png')
root.tk.call('wm', 'iconphoto', root._w, img)


error_label = Label(text="How the hell did you get here?! you must 
have the leet haxor skills!").pack()
error_label2 = Label(text="You must have this t-shirt!").pack()

photo = PhotoImage(file="Images/haxor.png") 
w = Label(root, image=photo)
w.photo = photo
w.pack()


root.mainloop()

#Yes I know that this should be commented but to be honest as the 
end user should never get to this screen I thought to hell with 
it! :D
