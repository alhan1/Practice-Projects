#Things to fix:
	#Need to allow all cases of letters
	#Need to introduce a timer

import random
import os, csv
from time import time

def letterGenerator(word):
	word = word.lower()
	box = []
	for i in range(0, len(word)):
		box.append(word[i])
	return box

def vowels(word):
	vowel = ["a", "e", "i", "o", "u"]
	box = word
	letter = []
	for box in box:
		if box in vowel:
			letter.append(box)
		else: 
			letter.append('_')

	return letter

def find(lst, word):
	indices = [i for i, x in enumerate(lst) if x == word]
	return indices

def Hangman():
	hangman = ['''
	  4.   +---+
	  5.   |   |
	  6.       |
	  7.       |
	  8.       |
	  9.       |
	 10. =========''', '''
	 11.
	 12.   +---+
	 13.   |   |
	 14.   O   |
	 15.       |
	 16.       |
	 17.       |
	 18. =========''', '''
	 19.
	 20.   +---+
	 21.   |   |
	 22.   O   |
	 23.   |   |
	 24.       |
	 25.       |
	 26. =========''', '''
	 27.
	 28.   +---+
	 29.   |   |
	 30.   O   |
	 31.  /|   |
	 32.       |
	 33.       |
	 34. =========''', '''
	 35.
	 36.   +---+
	 37.   |   |
	 38.   O   |
	 39.  /|\  |
	 40.       |
	 41.       |
	 42. =========''', '''
	 43.
	 44.   +---+
	 45.   |   |
	 46.   O   |
	 47.  /|\  |
	 48.  /    |
	 49.       |
	 50. =========''', '''
	 51.
	 52.   +---+
	 53.   |   |
	 54.   O   |
	 55.  /|\  |
	 56.  / \  |
	 57.       |
	 58. =========''']

	return hangman

def doubleEntry(xinput, game):
	userInput = xinput
	if userInput in game:
		print ("Sorry, you already entered the letter, try again\n")	

def main():
	list = open("test.txt", "r")
	if list.mode == "r":
		contents = list.readlines()
	word = contents[random.randint(0, len(contents))]
	check = letterGenerator(word)
	game = vowels(check)
	print(game)
	hangman = 0
	pic = Hangman()
	while (hangman is not len(pic)):
		user = input('Enter a letter \n>')
		user = user.lower()
		doubleEntry(user, game)
		if (user in check):
			indices = find(check, user)
			for i in range(0, len(indices)):
				del game[indices[i]]
				game.insert(indices[i], user)
		else:
			print(pic[hangman])
			hangman = hangman + 1
		print (game)
		if (game == check):
			break
	if hangman < 4:
		print ("Congrats, you won")
	else:
		print ("You lost, the word was %s" % ", ".join(map(str, check)))

def OverallGameplay():
	userInput = input("Do you want to play a game of hangman?\n>(YES OR NO)\t>")
	while userInput == "YES":
		main()
		userInput = input("Do you want to play again?\n(YES OR NO)\t>")
	print("Good Bye")

OverallGameplay()



















