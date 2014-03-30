BitCube.py
=========



**Usage**
```
Usage: bitcube.py [-g] [-h] [-c COLORS]
-g              Generates 36 moves
-h              Displays information about moves
-c COLORS       Uses the COLORS string (54 characters long) to generate the Secret Exponent
```


F: Front, L: Left, R: Right, U: Up, D: Down (bottom)


Follow the generated moves exactly. Each letter corresponds with a clockwise turn if you were facing that side.
A move with a tick (') after it means a counterclockwise turn if you were facing that side.


Once you finish moving the cube, hold the cube in the beginning orientation. Start with the top left color and write down the first letter of that color.
Go across that row (so 3 colors), and then down one row, and then across it. Do this for all 3 rows. Turn the cube to the right, so you are now on your right face.
Continue writing the 9 colors down for each side. Once you get back to your beginning face, flip the cube to the top side. Write those 9 down, then go to the opposite face.


**Example Output**
```
$ ./bitcube.py -g
```
```
****************************************************
BE SURE TO WRITE THIS DOWN INCASE YOU LOSE YOUR CUBE
****************************************************

Color (Facing): ORANGE
Color (Right): GREEN
Generated Moves: F L' U' R' L U U R' F' L' U' R U' D' F R D' U U' D' R L' L F' R' D D F' U R D R L U' D F' R U L
```

**Example Input**
```
$ ./bitcube.py -c GROYOBRROWWORGOGOBBGOYRGYGRGYYYBBGRBWYYOWBRWBWYYGYBROR
```
```
Passphrase: GROYOBRROWWORGOGOBBGOYRGYGRGYYYBBGRBWYYOWBRWBWYYGYBROR
Private Key: feafd12f849dbb8b2b700ee4ad623d75e13d01815f111c40469d7cdc2e569b22
Passphrase: 231614331551321214421632623266644234566154354566264313
Private Key: db926f40b54995b19cf986019f42107eafda82fe55535ef191ca878b34bfcafe
```

**Example Rotation**

```
Color (Facing): ORANGE
Color (Right): GREEN

ORANGE -> GREEN -> RED -> BLUE -> WHITE -> YELLOW
```
