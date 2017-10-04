import sys
'''
Student: Charles Laing ID: 1388069

creates an adjacency list to store a graph data struct
outputs the connected components of the graph in the format 

[num components]
[num elements][element list]
..

'''

class head:
    #Serves as the structure of each node
    def __init__(self, head=None):
        self.head = []

class Graph:
    #Actual graph structure is a list of nodes
    def __init__(self,v):
        #Constructor
        self.v = v
        self.nodeList = [] #nodelist is a list of edges, where the index is the vertex, and the second accessor is the edge
        for i in range(v):
            self.nodeList.append(head()) #head represents an edge on the graph
            
    def addEdge(self, source, dest):
        # helper function to add an edge
        self.nodeList[source].head.append(dest) #add the edge to the adjacency list
        #self.nodeList[dest].head.append(source)

    def connected(self):
        visited =[] #Create an open list to contain all unvisited nodes
        [visited.append(False) for i in range(self.v)] #All of them are false, so fill it with a list comp
        components = [] # place to put the strings
        for i in range(self.v): #for each node in the list
            if (visited[i] == False): #check if we haven't seen it yet
                tempvar = self.DFSutl(i, visited) #Call the util to iterate through the second structure
                if (len(tempvar)): #Only bother adding to the output if there are connected componenets present
                    components.append(str(len(tempvar)) +' '+  ' '.join([str(y) for y in tempvar]))
        print(str(len(components))+'\n'+ '\n'.join(components)) #formatting the output
        
    def minDistance(self, start):
        distance = 0
        distv = []
        visited = []
        for i in range(self.v):
            distv.append('-')
            visited.append(False)
            
        for i in range(len(self.nodeList[start].head)):
            if(visited[i] ==False):
                self.recurseDist(start,visited, distv, 0)
        distv[start] = 0;
        print(str(self.v) +' '+ ' '.join(map(str, distv)))
            
    def recurseDist(self, start, visited, distv, dist=0):
        distance = 0
        visited[start] = True
        for i in self.nodeList[start].head:
            #print(self.nodeList[start].head)
            if( not visited[i]):
                dist+=1
                self.recurseDist(i, visited,distv, dist)
                distv[i] = dist
        return distance +1
                
            
        
                
    def DFSutl(self,i, visited):
        visited[i] = True #We visit the node and color it
        val = [] #for returning
        val.append(i)
        for it in self.nodeList[i].head: #iterate through the secondary structure
            if (not visited[it]): #If we haven't seen it before, recurse
               val.extend(self.DFSutl(it, visited))
        return val

def read():
    # Python doesn't have cin like he wants, but I guess this should work. 
    line = map(int, raw_input().split())
    graph = Graph(line.pop(0))
    for i in range(graph.v):
        edgenum = line.pop(0)
        for y in range(edgenum):
            temp = line.pop(0)
            graph.addEdge(i,temp)
    
    return graph, int(raw_input()) #Return the starting vertex

def main():
    #Main function to call
    g, start = read()
    g.minDistance(start)

if __name__ == "__main__":
    #If it is being called from the python interpreter, start main
    main()

        
        

    
