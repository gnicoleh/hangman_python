## GUI FOR HANGMAN

from tkinter import *
from tkinter import ttk
import tkinter.font as font

mainWindow = Tk()
mainWindow.title("Crypto Hangman")
width = mainWindow.winfo_screenwidth()
height = mainWindow.winfo_screenheight()
mainWindow.geometry("%dx%d" % (width, height))
mainWindow.configure(bg="black")

# define font
myFont = font.Font(family="Segoe UI", size=30, weight="bold")

# add widgets here
button1 = Button(mainWindow, text="Play", bg="green", fg="white", font=myFont).place(relx=0.5, rely=0.5, anchor=CENTER)
button2 = Button(mainWindow, text="Settings", bg="green", fg="white", font=myFont).place(relx=0.5, rely=0.6, anchor=CENTER)
button3 = Button(mainWindow, text="Github Code", bg="green", fg="white", font=myFont).place(relx=0.5, rely=0.7, anchor=CENTER)
button4 = Button(mainWindow, text="Quit", bg="green", fg="white", font=myFont).place(relx=0.5, rely=0.8, anchor=CENTER)

mainWindow.mainloop()
