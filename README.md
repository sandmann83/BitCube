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

Color (Facing): Red
Color (Right): White
Generated Moves: R R' U' L' R' D R' L' F D U' U U R' D' L' L' F D' R F' L' F' R'
 D D' D L R R R L' R U U' F' U U' D

        Y B B
        R G B
        G B B
 B Y O  Y W W  R R O  W Y O
 O Y G  R R O  Y W O  W O G
 B Y G  W B W  G R R  Y W R
        R O O
        G B W
        Y G G

Birth Year: 1989
    Colors: YBBRGBGBBBYOOYGBYGYWWRROWBWRROYWOGRRWYOWOGYWRROOGBWYGG
 Encrypted: 522142422253354254500113020113503411053034501133420544
Secret Exp: 7ba4c9f3c26b89051a8a7ebcc1b30083643f3c5a0394eb24dd8aa5745c1035a1
```
