#CMPUT 396 Webbels
import sys
import random, math, time

STRINGS = ["--","oo","xx","$$","##","++","@@"]

#Colors:
#0 - Black
#1 - red
#2 - green
#3 - orange
#4 - blue
#5 - purple
#6 - turquoise
#7 - grey
COLORS = {
    0:'',
    1:"\x1b[1;37;41m",
    2:"\x1b[1;37;42m",
    3:"\x1b[1;37;43m",
    4:"\x1b[1;37;44m",
    5:"\x1b[1;37;45m",
    6:"\x1b[1;37;46m",
    7:"\x1b[1;37;47m"
            }
COLOR_TERM = '\x1b[0m'

def color(string, color):
    return(str(COLORS[color] + string + COLOR_TERM))


class webbels:
    def __init__(self, k, seed):
        self.dim = k
        self.board = []
        self.move_rng = random.Random()
        self.world_rng = random.Random()
        self.score = 0
        if seed != 0: #If the seed is 0, we don't want to set it
            self.move_rng.seed(seed)
            self.world_rng.seed(seed)

            
        for i in range(self.dim):
            self.board.append([])
            [self.board[i].append('') for y in range(self.dim)]
        self.fillRandom()
        blocklist = []
        #self.recursiveSearch(0,3,blocklist)
        #print(self.RandomMove(), "randomMove")
        carlo = self.RandomMove()
        while carlo:
            time.sleep(.5)
            print(self)
            print(carlo)
            self.doMove(carlo)
            carlo = self.RandomMove()
            #print(carlo)
            
            
        #self.doMove(blocklist)

    def RandomMove(self):
        if self.findMoves():
            x,y = self.move_rng.randint(0, self.dim-1), self.move_rng.randint(0,self.dim-1)
            blocklist = []
            self.recursiveSearch(x,y,blocklist)
            while len(blocklist) < 2:
                x,y = self.move_rng.randint(0, self.dim-1), self.move_rng.randint(0,self.dim-1)
                blocklist = []
                self.recursiveSearch(x,y,blocklist)
                #print(blocklist)
            return blocklist
        else:
            return 0
                
                
            
        
        

    def __str__(self):
        print("\x1b[2J")
        print("\x1b[H")
        output = ''
        for i in range(self.dim):
            for y in range(self.dim):
                output+= color(self.board[i][y], STRINGS.index(self.board[i][y]) )
            output += '\n'
        output += str(self.score)
        return output

    def fillRandom(self):
        for x in range(self.dim):
            for y in range(self.dim):
                self.board[x][y] = STRINGS[self.world_rng.randint(1,len(STRINGS)-1)]

    def addLeft(self):
        for y in range(self.dim):
            self.board[y][0] = STRINGS[self.world_rng.randint(1,len(STRINGS)-1)]

    def doMove(self, blocklist):
        for coord in blocklist:
            self.board[coord[0]][coord[1]] = '--'

        self.score = self.score + len(blocklist)**2
            
            
        gravity =  self.findGravity()
        while len(gravity):
            self.shiftDown(gravity)
            gravity = self.findGravity()
            
        pullr = self.pullRight()
        while pullr:
            print(pullr)
            col = pullr.pop()
            print(col)
            if col == 0:
                self.addLeft()
            else:
                self.shiftRight(col)
                pullr = self.pullRight()
                
    def shiftRight(self, col):
        for i in range(self.dim):
            old = self.board[i][col-1]
            self.board[i][col-1] = '--'
            self.board[i][col] = old
        

    def pullRight(self):
        retval = []
        for x in range(self.dim):
            col = []
            for i in range(self.dim):
                col.append(self.board[i][x])
            if len(set(col)) == 1: retval.append(x)
        return retval
            
    def findGravity(self):
        retval = []
        for x in range(self.dim):
            for y in range(self.dim):
                if self.board[y][x] != '--' and y < self.dim-1:
                    if self.board[y+1][x] == '--':
                        retval.append((x,y))
        return(retval)

    def shiftDown(self, shiftblocks):
        for coord in shiftblocks:
            old = self.board[coord[1]][coord[0]]
            self.board[coord[1]][coord[0]] = '--'
            self.board[coord[1]+1][coord[0]] = old
            
            

    def recursiveSearch(self,x,y,blocklist):
        #Look up, down, left, right
        if (x,y) in blocklist or x<0 or y<0:
            return
        blocklist.append((x,y))
        #If the block is empty, ignore
        this_block = self.board[x][y]
        if this_block != '--' and 0 <= x < self.dim-1 and 0 <= y < self.dim-1:
            if self.board[x+1][y] == this_block: self.recursiveSearch(x+1, y, blocklist)
            if self.board[x-1][y] == this_block: self.recursiveSearch(x-1, y, blocklist)
            if self.board[x][y+1] == this_block: self.recursiveSearch(x, y+1, blocklist)
            if self.board[x][y-1] == this_block: self.recursiveSearch(x, y-1, blocklist)
    
        #if the block is the same, call recursive search on it,
    def findMoves(self):
        moveset = []
        closedcoords = []
        for x in range(self.dim):
            for y in range(self.dim):
                blocklist = []
                self.recursiveSearch(y,x,blocklist)
                closedcoords.append(blocklist)
       # print(self.board[1][2], self.board[2][2], self.board[3][2])
        for i in closedcoords:
            if len(i) > 2:
                moveset.append(i)
        return moveset
            

def main(out, seed, n, size, colors, minballs, MC_runs):
    game = webbels(8, 50)
    print(game)
    #print(game.score)



if __name__ == '__main__':
    args = sys.argv
    if len(args) < 8:
        print("Incorrect Usage")
    else:
        argv = []
        [argv.append(int(i)) for i in args[1:]]
        main(argv[0],argv[1],argv[2],argv[3],argv[4],argv[5],argv[6])
