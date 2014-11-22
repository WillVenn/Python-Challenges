#!/usr/bin/env python3.4
import sys
from tkinter import *
import os

def callback():
	print (entry.get())
	label_name = Label(root, textvariable=var).pack()
	##new = Tk()
	##new.title(entry.get())
	##label_name = Label(textvariable=entry.get())
	##label_name.pack()



root = Tk()
root.title("Challenge 1!")
root.geometry("600x300+250+160")

label_intro = Label(text="Welcome to Challenge 1! please enter your name and age in the box below").pack()

#------------------------------------------
entry = Entry(root)
entry.pack()
entry.focus_set()

button = Button(root, text="Display", width=10, command=callback)
button.pack()

text = (entry.get())

var = StringVar(entry.get())


root.mainloop()

