from itertools import product
class Puzzle:
    def __init__(self):
        # create the data that we want to store.
        self.puzzleName = ''
        self.puzzleState = [] #List of a bunch of lists. So accessing the data will be puzzleState[i][j]
                              #where i is the row, and j is the column
        self.blocks = {}
        
    def read(self):
        #First line containes the Puzzle Name, Width, Height, ID of marked, Offset
        #eg puzzle1 4 5 X 1
        #Exit width is the width of the marked block
        line = raw_input().split()
        self.puzzleName = line[0]
        self.dims = (int(line[1]), int(line[2]))
        self.marked = line[3]
        self.offset = int(line[4])
        
        #Next is a series of lines that represent other blocks in the puzzle [a-z]
        #eg a X X b
        #eg a X X b
        #eg c d d e
        #eg c f g e
        #eg h - - i
        for i in range(self.dims[1]):
            inlist = list(raw_input())
            for i in range(len(inlist)):
                self.blocks[inlist[i]] = []
            self.puzzleState.append(inlist)
            #self.puzzleState.append(map(str, list(raw_input())))
        
        #Empty cells are marked with '-'
    def write(self):
        print(self.puzzleName + ' '+ str(self.dims[0]) +' '+ str(self.dims[1]) +' '+ self.marked +' '+ str(self.offset))
        for i in range(self.dims[1]):
            print(''.join(self.puzzleState[i]))
        
        #output to stdout the current state of the puzzle in the above format

    def findOpen(self):                    
        return self.blocks['-']
    
    def writeGoals(self):
        #goal is to look for available moves
        #blocks can move either u d l r

        #first, find all of the open spots
        openlist = self.findOpen()
        for i in range(self.dims[1]):
            for j in range(self.dims[0]):
                self.blocks[self.puzzleState[i][j]].append((i,j))
        empty = len(self.blocks.pop('-',None)) #Remove the empty spaces, and get the number of slots. this is the maximum number of moves possible
        avail = [] # We need a flat list of all block positions to make comparisons easier
        openm = [] # we need an empty list of moves
        #flatten the coords of the blocks
        for block in self.blocks:
            if self.blocks[block] not in avail:
                avail.extend(self.blocks[block])

        blockcopy = self.blocks #We make a copy in order to stops blocks being able to phase through eachother
        for val in range(1,empty+1):
            blockmoves = [(-val, 0),(val, 0), (0, -val), (0, val)]
           # print(self.blocks)
            for block in blockcopy: #Go through each block
                for move in blockmoves: # for u d l r
                    add = True
                    blocktest = []
                    for i in self.blocks[block]: #apply udlr to all of the tuples in the block
                        blocktest.append(tuple(map(lambda a,b: a+b, i, move)))
                        
                    #print(block, blocktest)

                    #Here we check to see if the potential position for the block is either taken, or out of bounds.
                    #we basically apply the transformation to all of the points of each block, if any of them overlap
                    #another block, we can ignore that move, because it's invalid
                    for i in blocktest:
                        #print(block, ((0 <= i[0] <= self.dims[0]) and (0<=i[1]<=self.dims[1])), i)
                        if ((i in avail) or not((0 <= i[0] < self.dims[1]) and (0 <= i[1] < self.dims[0]))):
                            if( i not in self.blocks[block]): #Make sure it isn't colliding with itself
                                add = False
                            #print("bad block, not adding")
                    if(add):
                        #print('adding', block, move)
                        openm.append((block, move))

            #We need to make sure that blocks can't jump over eachother
            blockcopy = {}
            for i in openm:
                blockcopy[i[0]] = self.blocks[i[0]]
                            
            
        '''
        for block in self.blocks:
            for y,x in self.blocks[block]:
                if (((y, x+2) in empty) and (0 <= x+2 <= self.dims[0])):
                    print(empty)
                    #print((tuple(map(lambda a, b: a+b,(x,y),move))))
                    print(block)
                    openm.append((block,(y, x+2)))
        '''
       #print(avail)
        print(openm)
                
def main():
    puzzle = Puzzle()
    puzzle.read()
    puzzle.writeGoals()



if __name__ == '__main__':
    main()
    
