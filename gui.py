## GUI FOR HANGMAN

from tkinter import *
#from tkinter import ttk
import tkinter.font as font
import webbrowser

gamepageurl = "https://github.com/gnicoleh/hangman_python" # make repo "public" so it works for everyone
def openweb():
    webbrowser.open(gamepageurl,1)


def openNewWindow():
    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(mainWindow)

    # sets the title of the Toplevel widget
    newWindow.title("Crypto Hangman: Guess the Cryptocurrency!")

    # set the geometry of toplevel
    width = newWindow.winfo_screenwidth()
    height = newWindow.winfo_screenheight()
    newWindow.geometry("%dx%d" % (width, height))

    # a Label widget to show in toplevel
    Label(newWindow, text="This is the game window").pack()


# Tk object which will be treated as a new window
mainWindow = Tk()
# sets the title of the window widget
mainWindow.title("Crypto Hangman")
# set upper-left icon using mainWindow.iconbitmap() || use .ico for windows os and .xbm for linux os
# set the geometry of the window
width = mainWindow.winfo_screenwidth()
height = mainWindow.winfo_screenheight()
mainWindow.geometry("%dx%d" % (width, height))
mainWindow.configure(bg="black")

# define font
myFont = font.Font(family="Segoe UI", size=30, weight="bold")

titlebar = Label(mainWindow, bg="black", fg="green", text="CRYPTO \nHANGMAN", font=(myFont, 62, "bold")).place(relx=0.5, rely=0.2, anchor=CENTER)
humorbar = Label(mainWindow, bg="black", fg="green", font=(myFont, 12, "italic"), text="An exercise in infuriating coding brought to you by Nicole and Zach").place(relx=0.5, rely=0.3, anchor=CENTER)

# add widgets here
button1 = Button(mainWindow, bg="green", fg="white", font=myFont, command=openNewWindow, text="Play").place(relx=0.5, rely=0.5, anchor=CENTER)
button2 = Button(mainWindow, bg="green", fg="white", font=myFont, text="Settings").place(relx=0.5, rely=0.6, anchor=CENTER)
button3 = Button(mainWindow, bg="green", fg="white", font=myFont, command= openweb, text="Github Code").place(relx=0.5, rely=0.7, anchor=CENTER)
button4 = Button(mainWindow, bg="green", fg="white", font=myFont, command= mainWindow.destroy, text="Quit").place(relx=0.5, rely=0.8, anchor=CENTER)

mainWindow.mainloop()
