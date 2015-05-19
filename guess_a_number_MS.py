from random import randint
correct = randint(0,100)  #Zufallszahl finden und als correct speichern
counter = 0               #Zaehler fuer die Anzahl der benoetigen Versuche
solved = False            #Loesung gefunden oder nicht

print "Hello, let's play a game!"

while solved == False :
	while True:
		try:
			eingabe = int(raw_input("Please insert an integer between 0 and 100:"))
			break
		except:
			print('Oops, this was not a number!')
	if eingabe > 100:
		print ('Your number is bigger than 100!')
	elif eingabe < 0:
		print ('Your number is smaller than 0')
	else:
		counter = counter + 1
		if (eingabe == correct):
			print 'Yippie, you won! You tried {} times'.format(counter)
			eing2= str(raw_input("Do you want to play again? Please enter y or n:"))
			if (eing2 == 'y'):
				counter = 0
				correct = randint(0,100)
			else:
				solved = True
		elif (eingabe < correct):
			print ('Sorry, your number was too low')
		else:
			print ('Sorry, your number was too high')



