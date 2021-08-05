## Hangman

import random

word_bank = ['chocolate', 'Horus Heresy', 'heretic', 'The God Emperor', 'Terraria', 'Siege', 'Beaulo', 'Dark Souls', 'cottoncandy', 'cryptocurrency', 'sparkpoint', 'PayMoneyWubby', 'SweetAnita']

## Choosing a random word from a list
def choose_word(word_bank):
    return str(random.choice(word_bank)) #need to ensure all outputs are strings for comparison

#For testing purposes, word chosen is currently printed out, will be removed in the future
word = choose_word(word_bank)
display_word = word
print(display_word)

#we save the word as all lowercase so that it does not matter if player inputs capitals or not
word = word.lower()

## Creating blank spaces for each character in the chosen word
def word_to_guess(word):
    blank_spaces = []
    for char in word:
        if char != " ":
            blank_spaces.append("_")
        else:
            blank_spaces.append(" ")
    return blank_spaces

## '*' is a pointer. The following line means: print the elements in blanks[] that are separated by ''
blanks = word_to_guess(word)
print(*blanks, sep='')
print(" ")

#main functionality of the game
def start_game (word, blanks):
	attempts = 6
	while True:
		if "_" in blanks:
			given_letter = input("Please enter a character that you think is in the word(s)\n")
			given_letter = given_letter.lower() #sanitize all inputs to also be lowercase so everything matches
			#safety check to ensure only 1 character entered at a time
			if len(given_letter) > 1:
				print("Please enter only one character at a time.")
				continue
			if given_letter in word:
				for char in word:
					if char == given_letter:
						position_of_letter = word.index(given_letter)
						blanks[position_of_letter] = given_letter
						print(blanks)
			elif attempts > 2:
				attempts -= 1
				print("Oops! Looks like that character is not in the word(s). Try again! You have " + str(attempts) + " attempts remaining.")
				continue
			elif attempts == 2:
				attempts -= 1
				print("Oops! Looks like that character is not in the word(s). Try again! This is your final attempt!")
				continue
			else:
				attempts -= 1
				print("Oops! Looks like that character is not in the word(s). You have ran out of attempts, better luck next time!")
				break
		else:
			print("Huzzah! You guessed ' " + blanks + "' right! Thank you for playing, see you next time!")
			break
	return None

#function to repeat the game if the player wants to
def play_again():
	while True:
		again = input("Would you like to play again? Y/N: ")
		again = again.upper() #pull input into uppercase to match if-else statement below
		if again == "Y":
			break #breaks from the loop, allowing function to return true, allowing gameplay loop to continue, right back to startgame
		elif again == "N":
			print("Ok, see you next time!") #later nerd
			raise SystemExit		## Does the same thing 'Sys.exit()' does, but doesn't import the sys package
		else:
			print("Please choose either 'Y' or 'N'")
			continue
	return True

#main gameplay loop
while True:
	start_game(word, blanks)
	if play_again() == True:
		continue
