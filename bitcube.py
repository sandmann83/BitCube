import uuid, hashlib, sys, random, pprint
from cube import cube

colors = ['White', 'Red', 'Blue', 'Orange', 'Green', 'Yellow']

ids = {'W': 0, 'R': 1, 'B': 2, 'O': 3, 'G': 4, 'Y': 5}

opposites = {'W': 'Y', 'Y': 'W', 'G': 'B', 'B': 'G', 'R': 'O', 'O': 'R'}

tops = {'WG': 'R',
	'GY': 'R',
	'YB': 'R',
	'BW': 'R',
	'WO': 'G',
	'OY': 'G',
	'YR': 'G',
	'RW': 'G',
	'OG': 'W',
	'GR': 'W',
	'RB': 'W',
	'BO': 'W'}

for t in list(tops):
	tops[t[::-1]] = opposites[tops[t]]

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
	return color in ids.keys()

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
	return [front_face, right_face]

def colorToNumbers(output):
	return ''.join([str(ids[str(number[0])]) for number in list(output)])

def sha256(numbers, mode="numbers", salt=""):
	if mode == "numbers":
		return hashlib.sha256(b''.join([str(num) for num in colorToNumbers(numbers)]) + salt).hexdigest()
	else:
		return hashlib.sha256(b''.join([str(num) for num in numbers]) + salt).hexdigest()

'''Deprecated'''
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

'''Deprecated'''
def displayHelp():
	print "Usage: bitcube.py [-g] [-h] [-c COLORS]"
	print "-g 		Generates 36 moves"
	print "-h 		Displays information about moves"
	print "-c COLORS	Uses the COLORS string (54 characters long) to generate the Secret Exponent"

def doMoves(cube, moves):
	moves = moves.split()
	for move in moves:
	    if "F" in move:
	        cube.turn(c.FRONT, "'" not in move)
	    if "L" in move:
	        cube.turn(c.LEFT, "'" not in move)
	    if "R" in move:
	        cube.turn(c.RIGHT, "'" not in move)
	    if "U" in move:
	        cube.turn(c.UP, "'" not in move)
	    if "D" in move:
	        cube.turn(c.DOWN, "'" not in move)
	return cube

def cubeToString(cube):
	order = "ULFRBD"
	colors_string = ""
	for face in list(order):
		for i in xrange(0, 3):
			colors_string += ''.join([list(ids.keys())[list(ids.values()).index(x)] for x in c.cube[face].struc[i]])
	return colors_string

moves = generateMoves()
faces = generateFaces()
print "*" * 52
print "BE SURE TO WRITE THIS DOWN INCASE YOU LOSE YOUR CUBE"
print "*" * 52, "\n"
print "Color (Facing): %s" % faces[0]
print "Color (Right): %s" % faces[1]
print "Generated Moves: %s" % moves

colors = [faces[0][0], opposites[faces[0][0]],
		  opposites[faces[1][0]], faces[1][0],
		  tops[faces[0][0] + faces[1][0]], opposites[tops[faces[0][0] + faces[1][0]]]]
colors = [ids[color] for color in colors]

c = cube(colors)
c = doMoves(c, moves)

print c.strCube()

import getpass
password = getpass.getpass("  Password: ")

colors_string = cubeToString(c)
print "    Colors: %s" % colors_string
print " Encrypted: %s" % colorToNumbers(colors_string)
print "Secret Exp: %s" % sha256(colors_string, mode="numbers", salt=password)
