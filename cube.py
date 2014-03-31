import random

class face(object):
    struc = []
    name = None
    value = None

    def __init__(self, name, value, faces):
        self.struc = []
        self.name = name
        self.value = value
        self.FRONT, self.BACK, self.LEFT, self.RIGHT, self.UP, self.DOWN = faces
        for x in xrange(3):
            self.struc.append([])
            for y in xrange(3):
                self.struc[x].append(value)
        
    def getName(self):
        return self.name

    def num2coord(self, num):
        return (num / 3, num % 3)

    def coord2num(self, coord):
        row,col = coord
        return row*3+col

    def getColumns(self, _2dlist=None):
        if _2dlist == None:
            _2dlist = self.struc
        ret = []
        for i in xrange(len(_2dlist[0])):
            ret.append([])
            for j in xrange(len(_2dlist)):
                ret[i].append(_2dlist[j][i])
        return ret

    def getUpFacePos(self, frontFace, row, col):
        if frontFace == self.FRONT or face == self.UP or frontFace == self.DOWN:
            return (row, col)
        elif frontFace == self.BACK:
            return self.num2coord(8 - self.coord2num((row,col)))
        elif frontFace == self.LEFT:
            cmap = [2,5,8,1,4,7,0,3,6]
            return self.num2coord(cmap[self.coord2num((row,col))])
        elif frontFace == self.RIGHT:
            cmap = [6,3,0,7,4,1,8,5,2]
            return self.num2coord(cmap[self.coord2num((row,col))])
        
    def getDownFacePos(self, frontFace, row, col):
        if frontFace == self.FRONT or frontFace == self.UP or frontFace == self.DOWN:
            return (row, col)
        elif frontFace == self.BACK:
            return self.num2coord(8 - self.coord2num((row,col)))
        elif frontFace == self.LEFT:
            cmap = [6,3,0,7,4,1,8,5,2]
            return self.num2coord(cmap[self.coord2num((row,col))])
        elif frontFace == self.RIGHT:
            cmap = [2,5,8,1,4,7,0,3,6]
            return self.num2coord(cmap[self.coord2num((row,col))])

    def getPosFromUp(self, row, col):
        if self.name == self.FRONT or self.name == self.UP or self.name == self.DOWN:
            return (row, col)
        elif self.name == self.BACK:
            return self.num2coord(8 - self.coord2num((row,col)))
        elif self.name == self.LEFT:
            cmap = [6,3,0,7,4,1,8,5,2]
            return self.num2coord(cmap[self.coord2num((row,col))])
        elif self.name == self.RIGHT:
            cmap = [2,5,8,1,4,7,0,3,6]
            return self.num2coord(cmap[self.coord2num((row,col))])

    def getPosFromDown(self, row, col):
        if self.name == self.FRONT or self.name == self.UP or self.name == self.DOWN:
            return (row, col)
        elif self.name == self.BACK:
            return self.num2coord(8 - self.coord2num((row,col)))
        elif self.name == self.LEFT:
            cmap = [2,5,8,1,4,7,0,3,6]
            return self.num2coord(cmap[self.coord2num((row,col))])
        elif self.name == self.RIGHT:
            cmap = [6,3,0,7,4,1,8,5,2]
            return self.num2coord(cmap[self.coord2num((row,col))])

    def getCoords(self, key):
        x, y = -1, -1
        if len(key) == 2:
            x,y = self.num2coord(key[1])
            key = key[0], x, y
        if key[0] == self.UP:
            x,y = self.getPosFromUp(key[1], key[2])
        elif key[0] == self.DOWN:
            x,y = self.getPosFromDown(key[1], key[2])
        elif self.name == self.UP:
            x,y = self.getUpFacePos(*key)
        elif self.name == self.DOWN:
            x,y = self.getDownFacePos(*key)
        else:
            x,y = key[1], key[2]
        return (x,y)

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        else:
            return self.name == other.name

    def __getitem__(self, key):
        x,y=self.getCoords(key)
        return self.struc[x][y]
    
    def __setitem__(self, key, value):
        x,y=self.getCoords(key)
        self.struc[x][y] = value

    def __len__(self):
        return 3

    def __str__(self):
        return str(self.struc)

    def __repr__(self):
        return str(self)

    def isSolved(self):
        c = self.struc[0][0]
        for x in self.struc:
            for y in x:
                if c != y: return False
        return True

    def listRep(self, frontFace):
        r = []
        for i in xrange(9):
            r.append(self[frontFace, i])
        return r

    def reOrder(self, frontFace, newOrder):
        oldDat = self.listRep(frontFace)
        for i in xrange(9):
            self[frontFace, i] = oldDat[newOrder[i]]

    def copy(self):
        r = face(self.name, self.value, (self.FRONT, self.BACK, self.LEFT, self.RIGHT, self.UP, self.DOWN))
        r.struc = []
        for x in xrange(3):
            r.struc.append([])
            for y in xrange(3):
                r.struc[x].append(self.struc[x][y])

        return r
        
class cube(object):
    W, R, B, O, G, Y = 0, 1, 2, 3, 4, 5
    colors = [W, Y, R, O, G, B] # F, B, L, R, U, D
    colLet = {W:"W", R:"R", B:"B", O:"O", G:"G", Y:"Y"}
    FRONT = "F"
    BACK = "B"
    LEFT = "L"
    RIGHT = "R"
    UP = "U"
    DOWN = "D"

    cube = {}
    moveList = []

    lastFace = -1
    recording = False
    
    def __init__(self, colors):
        self.cube = {}
        self.moveList = []
        self.colors = colors
        self.createCube()

    def copy(self):
        r = cube()
        faces = [self.FRONT, self.BACK, self.LEFT, self.RIGHT, self.UP, self.DOWN]
        for i in xrange(len(self.colors)):
            r.cube[faces[i]] = self.cube[faces[i]].copy()
        return r

    def createCube(self):
        faces = [self.FRONT, self.BACK, self.LEFT, self.RIGHT, self.UP, self.DOWN]
        for i in xrange(len(self.colors)):
            self.cube[faces[i]] = face(faces[i], self.colors[i], faces)          
                    
    def getColumns(self, frontFace, face):
        ret = []
        for i in xrange(len(face)):
            ret.append([])
            for j in xrange(len(face)):
                ret[i].append(face[(frontFace,j,i)])
        return ret
    
    def getFaces(self, frontFace):
        if frontFace == self.BACK:
            return self.BACK, self.FRONT, self.RIGHT, self.LEFT, self.UP, self.DOWN
        elif frontFace == self.LEFT:
            return self.LEFT, self.RIGHT, self.BACK, self.FRONT, self.UP, self.DOWN
        elif frontFace == self.RIGHT:
            return self.RIGHT, self.LEFT, self.FRONT, self.BACK, self.UP, self.DOWN
        elif frontFace == self.UP:
            return self.UP, self.DOWN, self.LEFT, self.RIGHT, self.BACK, self.FRONT
        elif frontFace == self.DOWN:
            return self.DOWN, self.UP, self.LEFT, self.RIGHT, self.FRONT, self.BACK
        else:
            return self.FRONT, self.BACK, self.LEFT, self.RIGHT, self.UP, self.DOWN

    def inverseMove(self, move):
        return move[0] if len(move)==2 else (move+"'")
        
    def turn(self, face, clockwise=True):
        FRONT, BACK, LEFT, RIGHT, UP, DOWN = self.getFaces(face)
        if self.recording:
            g = "%s%s" % (face, "" if clockwise else "'")
            self.moveList.append(g)
            f = True
            while f:
                f = False
                if len(self.moveList) > 1:
                    if self.moveList[-1] == self.inverseMove(self.moveList[-2]):
                        self.moveList.pop(); self.moveList.pop()
                        f = True
                if len(self.moveList) > 2:
                    if self.moveList[-1] == self.moveList[-2] == self.moveList[-3]:
                        self.moveList.pop(); self.moveList.pop()
                        self.moveList[-1] = self.inverseMove(self.moveList[-1])
                        f = True
        if clockwise:
            lRep = self.cube[LEFT].listRep(FRONT)
            rRep = self.cube[RIGHT].listRep(FRONT)
            uRep = self.cube[UP].listRep(FRONT)
            dRep = self.cube[DOWN].listRep(FRONT)

            #FRONT
            self.cube[FRONT].reOrder(FRONT, [6,3,0,7,4,1,8,5,2])
            #LEFT
            self.cube[LEFT][FRONT, 2] = dRep[0]
            self.cube[LEFT][FRONT, 5] = dRep[1]
            self.cube[LEFT][FRONT, 8] = dRep[2]
            #DOWN
            self.cube[DOWN][FRONT, 0] = rRep[6]
            self.cube[DOWN][FRONT, 1] = rRep[3]
            self.cube[DOWN][FRONT, 2] = rRep[0]
            #RIGHT
            self.cube[RIGHT][FRONT, 0] = uRep[6]
            self.cube[RIGHT][FRONT, 3] = uRep[7]
            self.cube[RIGHT][FRONT, 6] = uRep[8]
            #UP
            self.cube[UP][FRONT, 6] = lRep[8]
            self.cube[UP][FRONT, 7] = lRep[5]
            self.cube[UP][FRONT, 8] = lRep[2]
        else:
            lRep = self.cube[LEFT].listRep(FRONT)
            rRep = self.cube[RIGHT].listRep(FRONT)
            uRep = self.cube[UP].listRep(FRONT)
            dRep = self.cube[DOWN].listRep(FRONT)

            #FRONT
            self.cube[FRONT].reOrder(FRONT, [2,5,8,1,4,7,0,3,6])
            #LEFT
            self.cube[LEFT][FRONT, 2] = uRep[8]
            self.cube[LEFT][FRONT, 5] = uRep[7]
            self.cube[LEFT][FRONT, 8] = uRep[6]
            #DOWN
            self.cube[DOWN][FRONT, 0] = lRep[2]
            self.cube[DOWN][FRONT, 1] = lRep[5]
            self.cube[DOWN][FRONT, 2] = lRep[8]
            #RIGHT
            self.cube[RIGHT][FRONT, 0] = dRep[2]
            self.cube[RIGHT][FRONT, 3] = dRep[1]
            self.cube[RIGHT][FRONT, 6] = dRep[0]
            #UP
            self.cube[UP][FRONT, 6] = rRep[0]
            self.cube[UP][FRONT, 7] = rRep[3]
            self.cube[UP][FRONT, 8] = rRep[6]
    
    def __str__(self):
        x = ""
        for l in self.cube:
            x += l+" : "+str(self.cube[l])+"\n"
        return x[:-1]
        #return self.formatStr()

    def strSide(self, face, replCol=True):
        x = """%i %i %i
%i %i %i
%i %i %i""" % (self.cube[face][0][0],self.cube[face][0][1],self.cube[face][0][2],
               self.cube[face][1][0],self.cube[face][1][1],self.cube[face][1][2],
               self.cube[face][2][0],self.cube[face][2][1],self.cube[face][2][2])
        if replCol:
            for col in self.colLet: x = x.replace(str(col), self.colLet[col])
        return x
        
    def strCube(self,face=-1,replCol=True):
        faces = self.getFaces(face)
        o = "FBLRUD"
        
        x = """
        U0 U1 U2
        U3 U4 U5   
        U6 U7 U8    
 L0 L1 L2  F0 F1 F2  R0 R1 R2  B0 B1 B2
 L3 L4 L5  F3 F4 F5  R3 R4 R5  B3 B4 B5
 L6 L7 L8  F6 F7 F8  R6 R7 R8  B6 B7 B8
        D0 D1 D2
        D3 D4 D5
        D6 D7 D8
"""
        j = 0
        for face in faces:
            for i in xrange(9):
                s = "%s%d" % (o[j], i)
                x = x.replace(s, str(self.cube[face][faces[0], i]))
            j+=1

        if replCol:
            for col in self.colLet: x = x.replace(str(col), self.colLet[col])

        return x

