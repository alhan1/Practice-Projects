#this is a project to present a dice to print a random number
import random

Numbers = [i for i in range(1,7)]
check = input('Do you want to roll a dice? \n > ')
while check == 'yes':
		print('\n Dice rolls', Numbers[random.randint(0,5)])
		check = input("\n Do you want to roll again? \n > ")

print ("Goodbye")


