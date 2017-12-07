#CMPUT 396 Webbels
import sys
import random, math, time, copy

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

def color(string, color, mode):
    if mode:
        return(str(COLORS[color] + string + COLOR_TERM))
    else:
        return string
class MonteTree:
    #Represents the MonteCarlo tree. Copies the object and makes child nodes
    def __init__(self, webbels):
        self.node = copy.deepcopy(webbels)

    def findChildScores(self, monteVal):
        moveset = {}
        movesAtNode = self.node.findMoves()
        #[print(i) for i in movesAtNode]
        for move in movesAtNode:
            #print("trying",move)
            depth = monteVal
            child = copy.deepcopy(self.node)
            carlo = move #child.RandomMove()
            child.move = 0
            child.mscore = 0
            child.avg = 0
            while carlo and depth:
                depth -= 1
                child.move += 1
                child.mscore = len(carlo) ** 2
                child.avg += child.mscore
                child.doMove(carlo)
                
               
                #print(carlo)
                carlo = child.RandomMove()
                #print(carlo)
            child.avg = child.avg / child.move
            #print("score", child.score)
            moveset[child.score] = move
        #print ("best move",moveset[max(moveset)])
        return moveset[max(moveset)]
            
            
        

class webbels:
    def __init__(self,colormode, size, seed,colors, minballs, printmode,timer, MC_Depth):
        self.dim = size
        self.MC_Depth = MC_Depth
        self.move = 0
        self.avg = 0
        self.mscore = 0
        self.printmode = printmode
        self.colormode = colormode
        self.timer = timer
        self.colors = colors
        self.minballs = minballs
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
            
        
        blocklist = []
        #self.play()
        #self.recursiveSearch(0,3,blocklist)
        #print(self.RandomMove(), "randomMove")

    def play(self):
        #self.fillRandom()
        if self.MC_Depth == 0:
            carlo = self.RandomMove()
            self.move = 0
            self.mscore = 0
            self.avg = 0
            while carlo:
            
                self.move += 1
                time.sleep(self.timer / 1000)
                #print(self)
                #print(carlo)
                self.mscore = len(carlo) ** 2
                
                
                self.avg += self.mscore
                self.doMove(carlo)
                
                if self.printmode:
                    print(self)
                    #print(carlo)
                carlo = self.RandomMove()
                #print(carlo)
            self.avg = self.avg / self.move
        else:
            #if the depth is >0, do the monte carlo search
            self.move = 0
            self.mscore = 0
            self.avg = 0
            while self.findMoves():
                tree = MonteTree(self)
                time.sleep(self.timer / 1000)
                self.move += 1
                best = tree.findChildScores(self.MC_Depth)
                self.mscore = len(best) **2
                self.avg += self.mscore
                self.doMove(best)

                if self.printmode:
                    print(self)
            self.avg = self.avg / self.move
            
            
            
            
            
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
            output+= str(i)+" |"
            for y in range(self.dim):
                output+= color(self.board[i][y], STRINGS.index(self.board[i][y]), self.colormode)
            output += '| \n'
        bottom = '  '
        for i in range(self.dim):
            bottom += " "+str(i)
        bottom += '\n'
        output += bottom
        output += "moves: {0} score: {1} move-score: {2}\n ".format(self.move, self.score, self.mscore)
        return output

    def fillRandom(self):
        self.score = 0
        for x in range(self.dim):
            for y in range(self.dim):
                self.board[x][y] = STRINGS[self.world_rng.randint(1,self.colors)]

    def addLeft(self):
        numballs =  self.world_rng.randint(self.minballs, self.dim)
        padding = self.dim - numballs
        newcol = []
        [newcol.append(STRINGS[0]) for i in range(padding)]
        [newcol.append(STRINGS[self.world_rng.randint(1,self.colors)]) for i in range(numballs)]
        
        for y in range(self.dim):
            self.board[y][0] = newcol[y]

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
            col = pullr.pop(0)
            #print(col)
            if col == 0:
                self.addLeft()
            else:
                self.shiftRight(col)
                pullr = self.pullRight()
                
    def shiftRight(self, col):
        #print(self)
        #time.sleep(0.2)
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
        if (y,x) in blocklist or x<0 or y<0:
            return

        blocklist.append((y,x))
        #If the block is empty, ignore
        this_block = self.board[y][x]
        if this_block != '--':
            if 0 <= x <self.dim-1:
                if self.board[y][x+1] == this_block: self.recursiveSearch(x+1, y, blocklist)
                if self.board[y][x-1] == this_block: self.recursiveSearch(x-1, y, blocklist)
            if 0 <= y < self.dim-1:
                if self.board[y+1][x] == this_block: self.recursiveSearch(x, y+1, blocklist)
                if self.board[y-1][x] == this_block: self.recursiveSearch(x, y-1, blocklist)
            

            
            
            

        
    
        #if the block is the same, call recursive search on it,
    def findMoves(self):
        moveset = []
        closedcoords = []
        for y in range(self.dim):
            for x in range(self.dim):
                blocklist = []
                
                self.recursiveSearch(x,y,blocklist)
                #print(blocklist)
                closedcoords.append(blocklist)
       # print(self.board[1][2], self.board[2][2], self.board[3][2])
        for i in closedcoords:
            if len(i) >= 2:
                moveset.append(i)
        return moveset
            

def main(out, seed, n, size, colors, minballs, MC_runs):
    #(self,colormode, size, seed,colors, minballs, printmode,timer)
    if out == 0 :
        scores = []
        game = webbels(0,size, seed, colors, minballs,0,0)
        for i in range(n):
            game.fillRandom()
            game.play()
            scores.append(game.score)
            print("game {0} moves {1}".format(i, game.move))
        print(scores)
        #print(game)
    if out == -1:
        scores = []
        game = webbels(0,size, seed, colors, minballs,1,0)
        for i in range(n):
            game.fillRandom()
            game.play()
            scores.append(game.score)
            print("game {0} moves {1}".format(i, game.move))
        print(scores)
        #print(game)
    elif out > 0:
        scores = []
        game = webbels(1, size, seed, colors, minballs, 1, out, MC_runs)
        for i in range(n):
            game.fillRandom()
            game.play()
            #tree = MonteTree(game)
            #tree.findChildScores(2)
            
            #scores.append(game.score)
            print("game {0} moves {1} avg {2}".format(i, game.move, game.avg))
        print(scores)
    #for i in range(10):
        #
     #   game = webbels(8,i)
        #print(game)
    #print(game)



if __name__ == '__main__':
    args = sys.argv
    if len(args) < 8:
        print("Incorrect Usage")
    else:
        argv = []
        [argv.append(int(i)) for i in args[1:]]
        main(argv[0],argv[1],argv[2],argv[3],argv[4],argv[5],argv[6])


 
