#Import the required library
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry
win.geometry("750x280")

#Create a canvas object
canvas= Canvas(win, width= 1000, height= 750, bg="SpringGreen2")

#Add a text in Canvas
canvas.create_text(300, 50, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))
canvas.pack()

win.mainloop()