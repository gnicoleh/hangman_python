## GUI FOR HANGMAN

from tkinter import *
#from tkinter import ttk
import tkinter.font as font
import webbrowser, winsound, os

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
    newWindow.configure(bg="black")

    # a Label widget to show in toplevel
    Label(newWindow, text="This is the game window").pack()


def SoundButtonOff(button):
    button.image = volumeOffImage

def SoundButtonOn():
    pass


def DrawMainWindow():
    for widgets in mainWindow.winfo_children():
        widgets.destroy()

    titlebar = Label(mainWindow, bg="black", fg="green", text="CRYPTO \nHANGMAN", font=(myFont, 62, "bold")).place(relx=0.5, rely=0.2, anchor=CENTER)
    humorbar = Label(mainWindow, bg="black", fg="green", font=(myFont, 12, "italic"), text="An exercise in infuriating coding brought to you by Nicole and Zach").place(relx=0.5, rely=0.3, anchor=CENTER)

    # add widgets here
    button1 = Button(mainWindow, bg="green", fg="white", font=myFont, text="Play", command=PlayGame).place(relx=0.5, rely=0.5, anchor=CENTER)
    button2 = Button(mainWindow, bg="green", fg="white", font=myFont, text="Settings", command=OpenSettings).place(relx=0.5, rely=0.6, anchor=CENTER)
    button3 = Button(mainWindow, bg="green", fg="white", font=myFont, text="Github Code", command= openweb).place(relx=0.5, rely=0.7, anchor=CENTER)
    button4 = Button(mainWindow, bg="green", fg="white", font=myFont, text="Quit", command= mainWindow.destroy).place(relx=0.5, rely=0.8, anchor=CENTER)

    soundbutton = Button(mainWindow, image= volumeOnImage, height=50, width=50).place(relx=0.9, rely=0.9, anchor=CENTER)

    mainWindow.mainloop()

    

def PlayGame():
    for widgets in mainWindow.winfo_children():
        widgets.destroy()

    soundbutton = Button(mainWindow, image= volumeOnImage, height=50, width=50).place(relx=0.9, rely=0.9, anchor=CENTER)

def OpenSettings():
    for widgets in mainWindow.winfo_children():
        widgets.destroy()
    
    titlebar = Label(mainWindow, bg="black", fg="green", text="SETTINGS", font=(myFont, 62, "bold")).place(relx=0.5, rely=0.2, anchor=CENTER)
    button1 = Button(mainWindow, bg="green", fg="white", font=myFont, text="Back", command=DrawMainWindow).place(relx=0.5, rely=0.5, anchor=CENTER)
    soundbutton = Button(mainWindow, image= volumeOnImage, height=50, width=50).place(relx=0.9, rely=0.9, anchor=CENTER)



# Tk object which will be treated as a new window
mainWindow = Tk()
mainWindow.title("Crypto Hangman") # sets the title of the window widget
width = mainWindow.winfo_screenwidth()
height = mainWindow.winfo_screenheight() 
mainWindow.geometry("%dx%d" % (width, height)) # set the geometry of the window
mainWindow.configure(bg="black")
# set upper-left icon using mainWindow.iconbitmap() || use .ico for windows os and .xbm for linux os

myFont = font.Font(family="Segoe UI", size=30, weight="bold") # define font

#plays the soundtrack
soundfile_path = os.path.dirname(os.path.abspath(__file__)) + '\zeldas_lullaby_piano.wav'
soundfile = soundfile_path.replace("\\","/")
winsound.PlaySound(soundfile, winsound.SND_ASYNC + winsound.SND_LOOP) #SND_ASYNC allows other process to run cocurrently once the sound file starts. SND_LOOP will loop the song until the program is closed

folderpath = os.path.dirname(os.path.abspath(__file__))
tempvolumeOnPath = folderpath + '\\volumeon.gif'
tempvolumeOffPath = folderpath + '\\volumeoff.gif'
volumeOnPath = tempvolumeOnPath.replace("\\","/")
volumeOffPath = tempvolumeOffPath.replace("\\","/")
volumeOnImage = PhotoImage(file= volumeOnPath)
volumeOffImage = PhotoImage(file= volumeOffPath)

while TRUE:
    DrawMainWindow()
