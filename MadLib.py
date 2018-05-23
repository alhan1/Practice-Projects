def userInput():
	Noun = input("Enter a noun\n>")
	Adjective = input("Enter an adjective\n>")
	diction = {'Noun':Noun, 
				'Adjective':Adjective,
				}
	return diction

def madLibs(diction):
	Madlib1 = "If you are going to challenge a couple to a chicken fight during spring break, make sure they are more %s than you!" % diction['Adjective'] 
	Madlib2 = "On Summer Friday's, I wear my polka dotted %s to work under my business attire" % diction['Noun']
	dicti = {'Madlib1': Madlib1,
			'Madlib2': Madlib2,
			}
	return dicti

def main():
	user = userInput()
	madLib = madLibs(user)
	print(madLib['Madlib1'])
	inp = input('Do you want another Madlib?\n> ')
	if(inp == 'yes'):
		print(madLib['Madlib2'])

main()
