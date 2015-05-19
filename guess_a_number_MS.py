from random import randint
correct = randint(0,100)  #Zufallszahl finden und als correct speichern
counter = 0               #Zaehler fuer die Anzahl der benoetigen Versuche
solved = False            #Loesung gefunden oder nicht

print "Hello, let's play a game!"

while solved == False :
	eingabe = int(raw_input("please insert an integer between 0 and 100:"))
	counter = counter + 1
	if (eingabe == correct):
		print ('Yippie, you won! You tried ',counter,' times')
		solved = True
	elif (eingabe < correct):
		print ('Sorry, your number was too low')
	else:
		print ('Sorry, your number was too high')



