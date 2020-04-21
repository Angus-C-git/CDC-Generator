characters = {
	"A": 23,
	"B": 47,
	"I": 397,
	"L": 507,
	"O": 581,
	"P": 635,
	"R": 687,
	"U": 763,
	"Y": 901,
	"0": 405,
	"1": 73
}

def getMsg():
	msg = list(input("Enter Message: "))
	genCDC(msg)

def genCDC(msg):

	cdc = 0

	for letter in msg:
		try:
			charVal = characters.get(letter)
			cdc = (((((cdc + charVal)*521)%10000)+450)%967)
		except TypeError:
			print("One or more of the characters in the msessage are not supported, exiting...")
			cdc = None
			break
	print("MESSAGE CDC:", cdc)

getMsg()