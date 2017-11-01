
import heapq
import copy

def uniformCostSearch(node):
    openlist = [(0,node,[])] #queue of the nodes to explore
    closed = {} # map of nodes to states explored
    test = []
    while openlist:
        cost, testnode, path = heapq.heappop(openlist) #Grab the node from the top of the queue
        #print(testnode)

        #if closed.has_key(testnode):
        #    continue
        cont = True
        for i in closed:
            if (i.blocks == testnode.blocks):
                cont = False

        if(cont):
            test.append(path)

            if (testnode.goaltest()):
                return path

            cost += 1
            expand = expandNode(testnode)
            for k in expand:
                #print(expand[k])
                add = True
                for i in closed:
                    if (i.blocks == k.blocks):
                        add = False
                        #print((expand[k], path))
                if(add):heapq.heappush(openlist, (cost, k, (path,expand[k])))

            closed[testnode] = cost
    return [-1]
    


def expandNode(node):
    moves = node.writeGoals()
    nodelist = {}
    for move in moves: #go through all possible moves
        #inside each block, there are multiple points, we need to transform all of them
        moveblock = []
        blockcopy = copy.copy(node.blocks)

        for point in blockcopy[move[0]]:
            pointcopy = copy.copy(point)
            #print(node.blocks[move[0]], move[1], move[0])
            #print(pointcopy, 'before')
            moveblock.append(tuple(map(lambda a,b: a+b, move[1], pointcopy)))
            #print(pointcopy, 'after')
           # print(move[0],node.blocks[move[0]],moveblock, move[1]) #this is the list of the new positions of each block
            
        newnode = copy.deepcopy(node)
        empty = newnode.blocks[move[0]]

        #If there is an overlap when we moved the blocks, we don't want it to be listed as empty
        for i in moveblock:
            if i in empty:
                empty.remove(i)
        #print(empty)
        newnode.blocks[move[0]] = moveblock
        newnode.blocks['-'] = empty
        nodelist[newnode] = (move[1], move[0])
    return nodelist    

class Puzzle:
    def __init__(self):
        # create the data that we want to store.
        self.puzzleName = ''
        self.puzzleState = [] #List of a bunch of lists. So accessing the data will be puzzleState[i][j]
                              #where i is the row, and j is the column
        self.blocks = {}
    
    def goaltest(self):
        #print(self.dims[1], self.offset, self.blocks[self.marked])
        return ((self.dims[1], self.offset) in self.blocks[self.marked])
            
        
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

        for i in range(self.dims[1]):
            for j in range(self.dims[0]):
                self.blocks[self.puzzleState[i][j]].append((i,j))
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

        #print(self.blocks)
        bcopy = copy.copy(self.blocks)
        empty = len(bcopy.pop('-',None)) #Remove the empty spaces, and get the number of slots. this is the maximum number of moves possible
        avail = [] # We need a flat list of all block positions to make comparisons easier
        openm = [] # we need an empty list of moves
        #flatten the coords of the blocks
        for block in bcopy:
            if bcopy[block] not in avail:
                avail.extend(bcopy[block])

        blockcopy = bcopy #We make a copy in order to stops blocks being able to phase through eachother
        for val in range(1,empty+2):
            blockmoves = {'u':(-val, 0),'d':(val, 0), 'l':(0, -val), 'r':(0, val)}
           # print(self.blocks)
            for block in blockcopy: #Go through each block
                for move in blockmoves: # for u d l r
                    add = True
                    blocktest = []
                    for i in bcopy[block]: #apply udlr to all of the tuples in the block
                        blocktest.append(tuple(map(lambda a,b: a+b, i, blockmoves[move])))
                        
                    #print(block, blocktest)

                    #Here we check to see if the potential position for the block is either taken, or out of bounds.
                    #we basically apply the transformation to all of the points of each block, if any of them overlap
                    #another block, we can ignore that move, because it's invalid
                    for i in blocktest:
                        #print(block, ((0 <= i[0] <= self.dims[0]) and (0<=i[1]<=self.dims[1])), i)
                        if ((i in avail) or not((0 <= i[0] < self.dims[1]) and (0 <= i[1] < self.dims[0]))):
                            if( i not in bcopy[block]): #Make sure it isn't colliding with itself
                                add = False
                            #print("bad block, not adding")
                        if((i not in avail) and (block == self.marked) and (0<=i[0]<=self.dims[1]) and (self.offset <= i[1] < self.dims[0])):
                            add = True
                    if(add):
                        #print('adding', block, move)
                        openm.append((block, blockmoves[move], val))

            #We need to make sure that blocks can't jump over eachother
            blockcopy = {}
            for i in openm:
                blockcopy[i[0]] = bcopy[i[0]]
                            
            
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
        output = str(len(openm)) + ' '
        openm.sort()
        for i in openm:
            output += ''.join(map(str, i)) + ' '
        #print(output)
        return openm   

def flatten(iterable):
    # http://rightfootin.blogspot.ca/2006/09/more-on-python-flatten.html
    it = iter(iterable)
    for e in it:
        if isinstance(e, (list, tuple)):
            for f in flatten(e):
                yield f
        else:
            yield e
            
def main():
    puzzle = Puzzle()
    puzzle.read()
    #puzzle.writeGoals()
    val = uniformCostSearch(puzzle)
    move = [x for x in flatten(val)]
    new = []
    output = str(len(move)/3)+' '
    for x in range(len(move)/3): #split everything into 3
        y,x,v = move.pop(0), move.pop(0), move.pop(0)
        output+=v
        if(y>0 and y!=0): output+='d'+str(abs(y))+' '
        if(y<0 and y!=0): output+='u'+str(abs(y))+' '
        if(x<0 and x!=0): output+='l'+str(abs(x))+' '
        if(x>0 and x!=0): output+='r'+str(abs(x))+' '
    print(output)



if __name__ == '__main__':
    main()
    
