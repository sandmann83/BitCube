import uuid, hashlib, sys, random, argparse

colors = ['Orange',
	  'Green',
	  'Red',
	  'Blue',
	  'White',
	  'Yellow']
dictionary = {'O': 1,
	      'G': 2,
	      'R': 3,
	      'B': 4,
	      'W': 5,
	      'Y': 6}

def sumPrevious(generated):
	copy = generated
	for digit in generated:
		if generated.index(digit) == 0:
			previous = 0
		else:
			previous = generated[generated.index(digit) - 1]

		copy[generated.index(digit)] = int(digit) + int(previous)
	return copy

def sumNumber(number):
	return sum(map(int, str(number)))

def allLessThanOrEqual(generated, ceiling):
	good = True
	for num in generated:
		if num > ceiling:
			good = False
	return good

def validColor(color):
	return color in dictionary.keys()

def generateMoves():
	possible_moves = ['F', 'L', 'R', 'U', 'D', 'F\'', 'L\'', 'R\'', 'U\'', 'D\''] 
	generated = uuid.uuid4().int
	while len(str(generated)) != 39:
		generated = uuid.uuid4().int
	generated = list(str(generated))
	generated_sum = sumPrevious(sumPrevious(generated))
	while not allLessThanOrEqual(generated_sum, 10):
		generated_sum = [sumNumber(num) for num in generated_sum]
	return ' '.join([possible_moves[move-1] for move in generated_sum])

def generateFaces():
	front_face = random.choice(colors)
	right_face = random.choice(colors)

	if front_face == "Orange":
		while right_face == "Red" or front_face == right_face:
			right_face = random.choice(colors)
	elif front_face == "Red":
		while right_face == "Orange" or front_face == right_face:
			right_face = random.choice(colors)
	elif front_face == "Green":
		while right_face == "Blue" or front_face == right_face:
			right_face = random.choice(colors)
	elif front_face == "Blue":
		while right_face == "Green" or front_face == right_face:
			right_face = random.choice(colors)
	elif front_face == "Yellow":
		while right_face == "White" or front_face == right_face:
			right_face = random.choice(colors)
	elif front_face == "White":
		while right_face == "Yellow" or front_face == right_face:
			right_face = random.choice(colors)
	return [front_face.upper(), right_face.upper()]

def colorToNumbers(output):
	return ''.join([str(dictionary[str(number[0])]) for number in list(output)])

def sha256(numbers, mode="numbers"):
	if mode == "numbers":
		return hashlib.sha256(b''.join([str(num) for num in colorToNumbers(numbers)])).hexdigest()
	else:
		return hashlib.sha256(b''.join([str(num) for num in numbers])).hexdigest()

def displayInformation():
	print "*" * 52
	print "F: Front, L: Left, R: Right, U: Up, D: Down (bottom)"
	print "\n"
	print "Follow the generated moves exactly. Each letter corresponds with a clockwise turn if you were facing that side."
	print "A move with a tick (') after it means a counterclockwise turn if you were facing that side."
	print "\n"
	print "Once you finish moving the cube, hold the cube in the beginning orientation. Start with the top left color and write down the first letter of that color."
	print "Go across that row (so 3 colors), and then down one row, and then across it. Do this for all 3 rows. Turn the cube to the right, so you are now on your right face."
	print "Continue writing the 9 colors down for each side. Once you get back to your beginning face, flip the cube to the top side. Write those 9 down, then go to the opposite face."
	print "\n"
	print "Example if your starting face is ORANGE and your right face is GREEN:"
	print "ORANGE -> GREEN -> RED -> BLUE -> WHITE -> YELLOW"
	print "*" * 52

def displayHelp():
	print "Usage: bitcube.py [-g] [-h] [-c COLORS]"
	print "-g 		Generates 36 moves"
	print "-h 		Displays information about moves"
	print "-c COLORS	Uses the COLORS string (54 characters long) to generate the Secret Exponent"

args = sys.argv

if len(args) == 1:
	displayHelp()
	sys.exit(1)

if "-g" in args:
	moves = generateMoves()
	faces = generateFaces()
	print "*" * 52
	print "BE SURE TO WRITE THIS DOWN INCASE YOU LOSE YOUR CUBE"
	print "*" * 52, "\n"
	print "Color (Facing): %s" % faces[0]
	print "Color (Right): %s" % faces[1]
	print "Generated Moves: %s" % moves

if "-h" in args:
	displayInformation()

if "-c" in args:
	colors = args[2]
	if len(colors) is not 54:
		print "The length of COLORS must be 54 long (one for each color on the cube)."
		sys.exit(1)
	if False in [validColor(color) for color in list(colors)]:
		print "The only possible colors are O G R B W Y."
		sys.exit(1)
	print "Passphrase: %s" % colors
	print "Secret Exp: %s" % sha256(colors, mode="colors")
	print "Passphrase: %s" % colorToNumbers(colors)
	print "Secret Exp: %s" % sha256(colors, mode="numbers")
