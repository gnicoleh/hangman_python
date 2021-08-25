## GUI FOR HANGMAN

from tkinter import *
import tkinter as tk
import tkinter.font as font
import webbrowser, os, platform, random
from pygame import mixer



def SoundButtonOff(button):
    button.image = volumeOffImage

def SoundButtonOn():
    pass


def DrawMainWindow():
    for widgets in mainWindow.winfo_children():
        widgets.destroy()

    titlebar = Label(mainWindow, bg="black", fg="green", text="CRYPTO \nHANGMAN", font=(myFont, 62, "bold")).place(relx=0.5, rely=0.2, anchor=CENTER)
    humorbar = Label(mainWindow, bg="black", fg="green", font=(myFont, 12, "italic"), text="An exercise in infuriating Python coding brought to you by Nicole and Zach").place(relx=0.5, rely=0.3, anchor=CENTER)

    # add widgets here
    button1 = Button(mainWindow, bg="green", fg="white", font=myFont, text="Play", command=PlayGame).place(relx=0.5, rely=0.5, anchor=CENTER)
    button2 = Button(mainWindow, bg="green", fg="white", font=myFont, text="Settings", command=OpenSettings).place(relx=0.5, rely=0.6, anchor=CENTER)
    button3 = Button(mainWindow, bg="green", fg="white", font=myFont, text="Github Code", command=OpenWeb).place(relx=0.5, rely=0.7, anchor=CENTER)
    button4 = Button(mainWindow, bg="green", fg="white", font=myFont, text="Quit", command=mainWindow.destroy).place(relx=0.5, rely=0.8, anchor=CENTER)

    soundbutton = Button(mainWindow, image= volumeOnImage, height=50, width=50).place(relx=0.9, rely=0.9, anchor=CENTER)

    mainWindow.mainloop()

#GITHUB BUTTON SECTION
gamepageurl = "https://github.com/gnicoleh/hangman_python" # make repo "public" so it works for everyone
def OpenWeb():
    webbrowser.open(gamepageurl,1)



#ACTUAL GAMEPLAY SECTION

word_bank = ['chocolate', 'Horus Heresy', 'heretic', 'The God Emperor', 'Terraria', 'Siege', 'Beaulo', 'Dark Souls', 'cottoncandy', 'cryptocurrency', 'sparkpoint', 'PayMoneyWubby', 'SweetAnita']

# Choosing a random word from a list
def choose_word(word_bank):
    return str(random.choice(word_bank)) #needed to ensure all outputs are strings for comparison

# Creating blank spaces for each character in the chosen word
def word_to_guess(word):
    blank_spaces = []
    for char in word:
        if char != " ":
            blank_spaces.append("_")
        else:
            blank_spaces.append(" ")
    return blank_spaces

def PlayGame():
    for widgets in mainWindow.winfo_children():
        widgets.destroy()
    
    #the body of the code to build the play space and perform game logic
    word = choose_word(word_bank)
    word = word.lower()
    blanks = word_to_guess(word)
    attempts = 6

    wordDisplay = Label(mainWindow, bg="black", fg="green", text=blanks, font=(myFont, 42, "bold")).place(relx=0.5, rely=0.5, anchor=CENTER)
    #mainWindow.wordDisplay = Label(mainWindow, bg="black", fg="green", text= blanks, font=(myFont, 42, "bold")).place(relx=0.5, rely=0.5, anchor=CENTER)
    while True:
        if "_" in blanks:
            given_letter = input("Please enter a character that you think is in the word(s)\n")
            given_letter = given_letter.lower() # sanitize all inputs to also be lowercase so everything matches
            # safety check to ensure only 1 character entered at a time
            if len(given_letter) > 1:
                print("Please enter only one character at a time.")
                continue
            # safety check to ensure only letters are accepted. This way, numbers and symbols cannot deduct user attempts at the word
            if given_letter.isalpha() != True:
                print("Please only enter a letter of the alphabet.")
                continue
            if given_letter in word:
                i = 0 # needed to set the 'start' of the find() method
                for char in word:
                    if char == given_letter:
                        position_of_letter = word.find(given_letter, i) # looks if letter appears more than once in the word
                        i = position_of_letter + 1 # starts find() on the next index of the last appearance
                        blanks[position_of_letter] = given_letter
                #wordDisplay = Label(mainWindow, bg="black", fg="green", text= blanks, font=(myFont, 42, "bold")).place(relx=0.5, rely=0.5, anchor=CENTER)
                #text = tk.StringVar()
                #text.set(blanks)
                #wordDisplay = tk.Label(mainWindow, bg="black", fg="green", textvariable=text, font=(myFont, 42, "bold")).place(relx=0.5, rely=0.5, anchor=CENTER)
                wordDisplay['text'] = str(blanks)
                ##FIX THIS PART
                




#SETTINGS SECTION
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

##plays the soundtrack
#soundfile_path = os.path.dirname(os.path.abspath(__file__)) + '\zeldas_lullaby_piano.wav'
#soundfile = soundfile_path.replace("\\","/")
#winsound.PlaySound(soundfile, winsound.SND_ASYNC + winsound.SND_LOOP) #SND_ASYNC allows other process to run cocurrently once the sound file starts. SND_LOOP will loop the song until the program is closed

# test soundtrack for any os, if it works on Windows, please remove code commented right above
#What is this DOESNT work on Windows?
# mixer.init()
# mixer.music.load("zeldas_lullaby_piano.wav")
# mixer.music.play(-1)

folderpath = os.path.dirname(os.path.abspath(__file__))
tempVolumeOnPath = folderpath + '\\volumeon.gif'
tempVolumeOffPath = folderpath + '\\volumeoff.gif'
volumeOnPath = tempVolumeOnPath.replace("\\","/")
volumeOffPath = tempVolumeOffPath.replace("\\","/")
volumeOnImage = PhotoImage(file= volumeOnPath)
volumeOffImage = PhotoImage(file= volumeOffPath)

while TRUE:
    DrawMainWindow()
    