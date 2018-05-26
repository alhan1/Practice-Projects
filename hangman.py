import random
import os, csv
import time

def letterGenerator(word):
	word = word
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



def main():
	list = open("test.txt", "r")
	if list.mode == "r":
		contents = list.readlines()
	word = contents[random.randint(0, len(contents))]
	check = letterGenerator(word)
	game = vowels(check)
	print(game)
	hangman = 0
	while (hangman < 4):
		user = input('Enter a letter \n>')
		if (user in check):
			indices = find(check, user)
			for i in range(0, len(indices)):
				del game[indices[i]]
				game.insert(indices[i], user)
		else:
			hangman = hangman + 1
			print(hangman)
		print (game)
		if (game == check):
			break
	if hangman < 4:
		print ("Congrats, you won")
	else:
		print ("You lost")

def OverallGameplay():
	userInput = input("Do you want to play a game of hangman?\n>(YES OR NO)\t>")
	while userInput == "YES":
		main()
		userInput = input("Do you want to play again?\n(YES OR NO)\t>")
	print("Good Bye")

OverallGameplay()



















