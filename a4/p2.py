import heapq

class NxNGrid:
	def __init__(self):
		self.grid = []	#[y][x] map of coords
		self.obs = [] #List of Tuples representing each block.
		self.dim = 0 #N
		
	def read(self):
            # read in the map
		self.dim = int(raw_input())
		
		for i in range(self.dim):
			insertion = list(raw_input().strip())
			for y in range(len(insertion)):
				if (insertion[y] == "*"):
					self.obs.append((y,i))
			self.grid.append(insertion)
                
	
	def write(self):
		for i in self.grid:
			print(''.join(i))
		

class Node:
    def __init__(self, state, parent, goal, position):
        self.state = state #NxN object
        self.parent = parent #Node Object
        self.goal = goal #Goal Position
        self.position = position #Where the node is
        self.prevmov = None

    def Getmoves(self): #Computes the available moves for each node
        udlr = [(-1,0), (1,0), (0,-1), (0,1)]
        valid = {}
        for i in udlr:
            testval = tuple(map(lambda a, b: a+b, i, self.position))
            dim = self.state.dim
            if ((testval not in self.state.obs) and ((0 <= testval[0] < dim ) and (0 <= testval[1] < dim))):
                valid[i] = testval

        #print(valid)
        return valid
            
            
                        
def nocost(start, goal, cost):
    return cost

def manhattan(start, goal, cost):
    #do the manhattan distance
    return cost + abs(start[0] - goal[0]) + abs(start[1] - goal[1])

H_LIBRARY = {"M":manhattan, "0":nocost} # for ease of swapping functions


def Astar(node, costfunc): #Add the path cost method here
    maxOpen, maxClosed = 0,0
    openlist = [(0, node)]
    closed = {}
    while openlist:
        if len(openlist) > maxOpen: maxOpen = len(openlist)
        if len(closed) > maxClosed: maxClosed = len(closed)

        #print("openlist" + str(openlist) + "closed" + str(closed))
        cost, testnode = heapq.heappop(openlist)
        cost+=1
        #print(cost)

        if testnode.position in closed:
            continue

        #add (nodestate -> node) in closed
        closed[testnode.position] = testnode
        
        #if goal, return solution
        if testnode.position == testnode.goal:
            return testnode, maxOpen, maxClosed
        #expand node, add successor nodes to open if not in closed
        moves = testnode.Getmoves()

        for k,v in moves.items():
            newNode = Node(testnode.state, testnode, testnode.goal, v)
            if newNode.position not in closed:
                newNode.prevmov = k
                #openlist.append((H_LIBRARY[costfunc](newNode.position, newNode.goal),newNode)) #RIP
                heapq.heappush(openlist, (H_LIBRARY[costfunc](newNode.position, newNode.goal, cost),newNode))
        
    return -1, maxOpen, maxClosed


def readPoints():
    positions = [] #list of tuples of tuples. ie. [((s.x,s.y), (g.x,g.y))]
    for i in range(int(raw_input())):
        v = map(int, raw_input().split())
        positions.append(((v[0], v[1]), (v[2], v[3])))
    return positions
        
        
    
	
def main():
	p = NxNGrid()
	p.read()
        positions = readPoints()
	#p.write()
        #print(positions)
       # print("Starting Astar")
        #print(p.obs)
        for i in positions:
            for v in ['0','M']:
                initialNode = Node(p, None, i[1], i[0])
                nn, maxopen, maxclosed = Astar(initialNode, v)
                movelist = []
                udlr = {(-1,0): 'L', (1,0):'R', (0,-1):'U', (0,1):'D', None:''}
                while nn != None and  nn != -1:
                    #print(nn.position, udlr[nn.prevmov])
                    #movelist.append(udlr[nn.prevmov])
                    movelist.insert(0,udlr[nn.prevmov])
                    nn = nn.parent
                if (nn == -1): path_size = -1
                else: path_size = len(''.join(movelist))
                print("h={0} {1} {2} {3} {4} {5} {6} {7} {8}".format(v,path_size,maxopen,maxclosed,initialNode.position[0], initialNode.position[1],
                                                                         initialNode.goal[0], initialNode.goal[1],  ''.join(movelist)))
                # print("Finished List")
            

	
	
if __name__ == "__main__":
	main()
