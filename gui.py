## GUI FOR HANGMAN

from tkinter import *
from tkinter import ttk
import tkinter.font as font
import webbrowser

gamepageurl = "https://github.com/gnicoleh/hangman_python"
def openweb():
    webbrowser.open(gamepageurl,1)

mainWindow = Tk()
mainWindow.title("Crypto Hangman")
width = mainWindow.winfo_screenwidth()
height = mainWindow.winfo_screenheight()
mainWindow.geometry("%dx%d" % (width, height))
mainWindow.configure(bg="black")

# define font
myFont = font.Font(family="Segoe UI", size=30, weight="bold")

titlebar = Label(mainWindow, bg="black", fg="green", text="HANGMAN", font=(myFont, 62)).place(relx=0.5, rely=0.2, anchor=CENTER)
humorbar = Label(mainWindow, bg="black", fg="green", text="An exercise in infuriating coding brought to you by Nicole and Zach").place(relx=0.5, rely=0.25, anchor=CENTER)

# add widgets here
button1 = Button(mainWindow, text="Play", bg="green", fg="white", font=myFont).place(relx=0.5, rely=0.5, anchor=CENTER)
button2 = Button(mainWindow, text="Settings", bg="green", fg="white", font=myFont).place(relx=0.5, rely=0.6, anchor=CENTER)
button3 = Button(mainWindow, text="Github Code", bg="green", fg="white", font=myFont, command= openweb).place(relx=0.5, rely=0.7, anchor=CENTER)
button4 = Button(mainWindow, text="Quit", bg="green", fg="white", font=myFont, command= mainWindow.destroy).place(relx=0.5, rely=0.8, anchor=CENTER)

mainWindow.mainloop()
