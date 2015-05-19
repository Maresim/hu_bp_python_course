
from random import randint
correct = randint(0,100)  #Zufallszahl finden und als correct speichern
counter = 0               #Zaehler fuer die Anzahl der benoetigen Versuche
solved = False            #Loesung gefunden oder nicht
validanswer = False       #vernuenftige Antwort auf nochmal spielen

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
			while validanswer == False:
				eing2= str(raw_input("Do you want to play again? Please enter y or n:"))
				if (eing2 == 'y'):
					counter = 0
					correct = randint(0,100)
					validanswer = True
				elif (eing2 == 'n'):
					solved = True
					validanswer = True
					print('Goodbye')
				else:
					print ('This was not a valid answer.')
		elif (eingabe < correct):
			print ('Sorry, your number was too low')
		else:
			print ('Sorry, your number was too high')



