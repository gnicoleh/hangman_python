## GUI FOR HANGMAN

from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.font as font
import webbrowser, os, platform, random
from pygame import mixer


#----------------MAIN MENU SECTION----------------
def DrawMainWindow():
    for widgets in mainWindow.winfo_children():
        widgets.destroy()

    titlebar = Label(mainWindow, bg="black", fg="green", text="CRYPTO \nHANGMAN", font=(myFont, 62, "bold")).place(relx=0.5, rely=0.2, anchor=CENTER)
    humorbar = Label(mainWindow, bg="black", fg="green", font=(myFont, 12, "italic"), text="An exercise in infuriating Python coding brought to you by Nicole and Zach").place(relx=0.5, rely=0.3, anchor=CENTER)

    # add widgets here
    play = Button(mainWindow, bg="green", fg="white", font=myFont, text="Play", command=PlayGame).place(relx=0.5, rely=0.5, anchor=CENTER)
    settings = Button(mainWindow, bg="green", fg="white", font=myFont, text="Settings", command=OpenSettings).place(relx=0.5, rely=0.6, anchor=CENTER)
    githubCode = Button(mainWindow, bg="green", fg="white", font=myFont, text="Github Code", command=OpenWeb).place(relx=0.5, rely=0.7, anchor=CENTER)
    quitGame = Button(mainWindow, bg="green", fg="white", font=myFont, text="Quit", command=mainWindow.destroy).place(relx=0.5, rely=0.8, anchor=CENTER)

    global soundButton
    soundButton = Button(mainWindow, image= volumeOnImage, height=50, width=50, command=switch)
    soundButton.place(relx=0.9, rely=0.9, anchor=CENTER)

    mainWindow.mainloop()

#----------------GITHUB BUTTON SECTION----------------
gamepageurl = "https://github.com/gnicoleh/hangman_python" # make repo "public" so it works for everyone
def OpenWeb():
    webbrowser.open(gamepageurl,1)


#----------------ACTUAL GAMEPLAY SECTION-----------------

word_bank = ['choco late', 'Horus Heresy', 'her etic', 'The God Emperor', 'Terr aria', 'Sie ge', 'Bea ulo', 'Dark Souls', 'cotton candy', 'crypto currency', 'spark point', 'PayMoney Wubby', 'Sweet Anita']

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
    def display_warning(message):
        # Displays a warning message to the user, takes a string as an argument
        warning = Label(mainWindow, bg="red", fg="white", text=message, font=(myFont, 18, "bold"))
        warning.place(relx=0.5, rely=0.7, anchor=CENTER)
        warning.after(2500, lambda: warning.destroy())
        

    for widgets in mainWindow.winfo_children():
        widgets.destroy()
    
    global soundButton
    soundButton = Button(mainWindow, image= volumeOnImage, height=50, width=50, command=switch)
    soundButton.place(relx=0.9, rely=0.9, anchor=CENTER)
    back = Button(mainWindow, bg="green", fg="white", font=(myFont, 24, "bold"), text="Main Menu", command=DrawMainWindow).place(relx=0.9, rely=0.1, anchor=CENTER)
    
    #the body of the code to build the play space and perform game logic
    word = choose_word(word_bank)
    word = word.lower()
    blanks = word_to_guess(word)
    attempts = 6

    wordDisplay = Label(mainWindow, bg="black", fg="green", text=" ".join(blanks), font=(myFont, 42, "bold"))
    wordDisplay.place(relx=0.5, rely=0.4, anchor=CENTER) # using .place in its own line prevents object "wordDisplay" becoming type None
    while True:
        if "_" in blanks:
            #given_letter = input("Please enter a character that you think is in the word(s)\n")
            #given_letter = given_letter.lower() # sanitize all inputs to also be lowercase so everything matches
            # safety check to ensure only 1 character entered at a time

            label = Label(mainWindow, bg="black", fg="white", text="Please enter the letter that you think is in the word(s):", font=(myFont, 36, "bold"))
            label.place(relx=0.5, rely=0.6, anchor=CENTER)
            entry = Entry(mainWindow, font=(myFont, 36, "bold"), width=3, justify="center")
            entry.place(relx=0.5, rely=0.8, anchor=CENTER)

            def func(event=None):
                #global string
                string = entry.get().lower()
                if string == "a":
                    print(string)
                    entry.delete(0, END)
                else:
                    print("I am not 'a'!")
                    entry.delete(0, END)
            
            #-------------------------------------------------------------------------------------------#    
            #### THE PROBLEM IS THE WHILE LOOP ION LINE 81!!! MAKES ENTRY AND LABEL WEIRD ####
            #### LINES 184 - 200 WORK JUST FINE CAUSE THEY DON'T HAVE WHILE LOOP. CODE IS THE SAME ####
            #-------------------------------------------------------------------------------------------#

            
            #mainWindow.bind("<Return>", func)
            checkButton = Button(text="Enter", command=func).place(relx=0.5, rely=0.9, anchor=CENTER)
            mainWindow.mainloop()   # DO NOT REMOVE, defines 'string', 'button', 'label', and 'message'
            #print(string)

            #if len(string) > 1:
            #    display_warning("Please enter only one character at a time!")
            #    entry.delete(0, END)
            #    continue
            ## safety check to ensure only letters are accepted. This way, numbers and symbols cannot deduct user attempts at the word
            #if string.isalpha() != True:
            #    display_warning("Please only enter a letter of the alphabet!")
            #    entry.delete(0, END)
            #    continue
            #if string in word:
            #    i = 0 # needed to set the 'start' of the find() method
            #    for char in word:
            #        if char == string:
            #            position_of_letter = word.find(string, i) # looks if letter appears more than once in the word
            #            i = position_of_letter + 1 # starts find() on the next index of the last appearance
            #            blanks[position_of_letter] = string
            #    wordDisplay.config(text=" ".join(blanks))
            #elif attempts > 2:
            #    attempts -= 1
            #    display_warning("Oops! Looks like that character is not in the word(s). Try again! You have " + str(attempts) + " attempts remaining.")
            #    entry.delete(0, END)
            #    continue
            #elif attempts == 2:
            #    attempts -= 1
            #    display_warning("Oops! Looks like that character is not in the word(s). Try again! This is your final attempt!")
            #    entry.delete(0, END)
            #    continue
            #else:
            #    attempts -= 1
            #    label.destroy()
            #    entry.destroy()
            #    message = Label(mainWindow, bg="green", fg="white", text="Oops! Looks like that character is not in the word(s). You have ran out of attempts, better luck next time!", font=(myFont, 18, "bold"))
            #    message.place(relx=0.5, rely=0.5, anchor=CENTER)
            #    message.after(3700, lambda: message.destroy())
            #    again = Label(mainWindow, bg="grey", fg="white", text="Would you like to play again?", font=(myFont, 18, "bold"))
            #    again.place(relx=0.5, rely=0.6, anchor=CENTER)
            #    yes = Button(mainWindow, bg="green", fg="white", font=(myFont, 18, "bold"), text="Yes", command=PlayGame)
            #    yes.place(relx=0.47, rely=0.7, anchor=CENTER)
            #    no = Button(mainWindow, bg="red", fg="white", font=(myFont, 18, "bold"), text="No", command=DrawMainWindow)
            #    no.place(relx=0.53, rely=0.7, anchor=CENTER)
            #    break
        #else:
        #    # blanks at this point is a list of characters, so to prevent it being printed as an ugly list, which cannot be concatenated, we iterate through the list,
        #    # concatenating each element together individually into a word called merger which is then printed
        #    merger = ""
        #    for char in blanks:
        #        merger += char
        #    message = Label(mainWindow, bg="green", fg="white", text="Huzzah! You guessed '" + merger + "' right! Thank you for playing, see you next time!", font=(myFont, 18, "bold"))
        #    message.place(relx=0.5, rely=0.5, anchor=CENTER)
        #    message.after(3700, lambda: message.destroy())
        #    again = Label(mainWindow, bg="grey", fg="white", text="Would you like to play again?", font=(myFont, 18, "bold"))
        #    again.place(relx=0.5, rely=0.6, anchor=CENTER)
        #    yes = Button(mainWindow, bg="green", fg="white", font=(myFont, 18, "bold"), text="Yes", command=PlayGame)
        #    yes.place(relx=0.47, rely=0.7, anchor=CENTER)
        #    no = Button(mainWindow, bg="red", fg="white", font=(myFont, 18, "bold"), text="No", command=mainWindow.destroy)
        #    no.place(relx=0.53, rely=0.7, anchor=CENTER)
        #    break
                

#----------------SETTINGS SECTION----------------
def OpenSettings():
    for widgets in mainWindow.winfo_children():
        widgets.destroy()
    
    titlebar = Label(mainWindow, bg="black", fg="green", text="SETTINGS", font=(myFont, 62, "bold")).place(relx=0.5, rely=0.2, anchor=CENTER)
    back = Button(mainWindow, bg="green", fg="white", font=myFont, text="Back", command=DrawMainWindow).place(relx=0.5, rely=0.5, anchor=CENTER)
    
    global soundButton
    soundButton = Button(mainWindow, image= volumeOnImage, height=50, width=50, command=switch)
    soundButton.place(relx=0.9, rely=0.9, anchor=CENTER)

    label = Label(mainWindow, bg="black", fg="white", text="Please enter the letter that you think is in the word(s):", font=(myFont, 36, "bold"))
    label.place(relx=0.5, rely=0.7, anchor=CENTER)
    entry = Entry(mainWindow, font=(myFont, 36, "bold"), width=3, justify="center")
    entry.place(relx=0.5, rely=0.8, anchor=CENTER)
    #entry.focus_set()

    def func(event=None):
        string = entry.get().lower()
        if string == "a":
                    print(string)
                    entry.delete(0, END)
        else:
            print("I am not 'a'!")
            entry.delete(0, END)

    mainWindow.bind('<Return>', func)
    checkButton = Button(text="Enter", command=func).place(relx=0.5, rely=0.9, anchor=CENTER)


#----------------MAIN WINDOW SECTION----------------
# Tk object which will be treated as a new window
mainWindow = Tk()
mainWindow.title("Crypto Hangman") # sets the title of the window widget
width = mainWindow.winfo_screenwidth()
height = mainWindow.winfo_screenheight() 
mainWindow.geometry("%dx%d" % (width, height)) # set the geometry of the window
mainWindow.configure(bg="black")
# set upper-left icon using mainWindow.iconbitmap() || use .ico for windows os and .xbm for linux os

myFont = font.Font(family="Segoe UI", size=30, weight="bold") # define font

#----------------SOUND SECTION----------------
##plays the soundtrack
#soundfile_path = os.path.dirname(os.path.abspath(__file__)) + '\zeldas_lullaby_piano.wav'
#soundfile = soundfile_path.replace("\\","/")
#winsound.PlaySound(soundfile, winsound.SND_ASYNC + winsound.SND_LOOP) #SND_ASYNC allows other process to run cocurrently once the sound file starts. SND_LOOP will loop the song until the program is closed

# test soundtrack for any os, if it works on Windows, please remove code commented right above
#What is this DOESNT work on Windows?
mixer.init()
mixer.music.load("zeldas_lullaby_piano.wav")
mixer.music.play(-1)

#----------------VOLUME BUTTON SECTION----------------
# used as a boolean for the volume button
is_on = True

def switch():
    global is_on

    if is_on:
        soundButton.config(image = volumeOffImage)
        soundButton.place(relx=0.9, rely=0.9, anchor=CENTER)
        is_on =  False
    else:
        soundButton.config(image = volumeOnImage)
        is_on = True


folderpath = os.path.dirname(os.path.abspath(__file__))
tempVolumeOnPath = folderpath + '\\volumeon.gif'
tempVolumeOffPath = folderpath + '\\volumeoff.gif'
volumeOnPath = tempVolumeOnPath.replace("\\","/")
volumeOffPath = tempVolumeOffPath.replace("\\","/")
volumeOnImage = PhotoImage(file= volumeOnPath)
volumeOffImage = PhotoImage(file= volumeOffPath)

while TRUE:
    DrawMainWindow()
