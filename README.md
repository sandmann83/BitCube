BitCube.py
=========

**Usage**
```
Usage: bitcube.py
```

F: Front, L: Left, R: Right, U: Up, D: Down (bottom)

Each letter corresponds with a clockwise turn if you were facing that side.
A move with a tick (') after it means a counterclockwise turn if you were facing that side.


Thanks to an open source Python Rubik's Cube implementation that I slimmed down. No author to give credit to, so here it is: http://pastebin.com/KwGMujyB.

**Example Output**
```
$ ./bitcube.py
```
```
****************************************************
BE SURE TO WRITE THIS DOWN INCASE YOU LOSE YOUR CUBE
****************************************************

Color (Facing): Green
Color (Right): White
Generated Moves: F U D U R' R' U F F' F' R U' R F' L L R L' U F R' F L U' R R U' U L' U L U' U F U' R U' F' D

        O G B
        O O B
        R G Y
 G Y W  G W R  G Y W  R R Y
 O Y O  G G W  B W R  B B B
 R W G  O G O  B Y O  Y W Y
        W Y W
        R R R
        B O B

Passphrase: OGBOOBRGYGYWOYORWGGWRGGWOGOGYWBWRBYORRYBBBYWYWYWRRRBOB
Secret Exp: b7b1f65cbbd682de37735cb9df932007752641532c4ad8ef510c1eadc85a6106
Passphrase: 342332145450353104401440343450201253115222505050111232
Secret Exp: e87fa90c573e0ab615fff08fbad14d1099d233066bb927fd489018a7e5e6fe05
```
