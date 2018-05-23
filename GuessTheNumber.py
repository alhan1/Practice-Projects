import random 	

def main():
	number = random.randint(0,100)
	enter = int(input('Enter a number between 0 and 100\n> '))
	check = 'yes'
	while (enter is not number):
		if(enter > number):
			print ("You're high")
		elif(enter < number):
			print ("You're low")
		check = input("Do you want to guess again?\n> ")
		if (check == 'yes'):
			enter = int(input('Enter a number between 0 and 100\n> '))
		else:
			print("Good Bye")
			exit(0)
	print("Congratulations, you guessed correctly!")

check = input('Do you want to play a game?\n> ')
while check == 'yes':
	main()
	check = input('Do you want to play again?\n> ')
	if (check == 'yes'):
		main()
	else:
		print("Good Bye")
		exit(0)

print("Good Bye")



