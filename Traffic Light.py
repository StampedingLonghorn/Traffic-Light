#Library imports
from gpiozero import LEDBoard
from time import sleep

#Declarations
red = LEDBoard(2, 17, 10, 5)
yellow = LEDBoard(3, 27, 9, 6)
permissiveYellow = LEDBoard(4)
rightYellow = LEDBoard(19)
green = LEDBoard(22, 11, 13)
protectedGreen = LEDBoard(14)
rightGreen = LEDBoard(26)

while True:
	#Setup
	red.off()
	yellow.off()
	permissiveYellow.off()
	rightYellow.off()
	green.on()
	protectedGreen.on()
	rightGreen.off()

	#Protected to permissive left
	sleep(5) #Number of seconds protected green light is on.
	protectedGreen.off()
	permissiveYellow.blink(1,1,10,False) #This blinks every second for 10 blinks.

	#Permissive left and green to yellow
	green.off()
	yellow.on()

	#Yellow to red
	sleep(2) #Number of seconds yellow light is on.
	yellow.off()
	red.on()
	sleep(15) #Number of seconds red light is on.

	#Protected right turn
	rightGreen.on() #Turns on protected right turn.
	sleep(5) #Number of seconds right green is on.
	rightGreen.off()
	rightYellow.on()
	sleep(2) #Number of seconds yellow right turn is on.
	rightYellow.off()
	sleep(1)
