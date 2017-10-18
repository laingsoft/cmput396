import sys
'''
Student: Charles Laing ID: 1388069

Greated an adjacency list to store a graph data struct
outputs the connected structure of the graph. 

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
        self.nodeList[dest].head.append(source)

    def connected(self):
        visited =[] #created the visited list. we can keep track of the visited nodes here
        [visited.append(False) for i in range(self.v)] #list comp to fill the visited with false
        components = [] #for building the output at the end
        for i in range(self.v):
            if (visited[i] == False): #only look if we haven't seen it before
                tempvar = self.DFSutl(i, visited)
                if (len(tempvar)):                    
                    components.append(str(len(tempvar)) +' '+  ' '.join([str(y) for y in tempvar])) # string building
        print(str(len(components))+'\n'+ '\n'.join(components))
        
    
    def DFSutl(self,i, visited):
        #performs the dfs
        visited[i] = True
        val = []
        val.append(i)
        for it in self.nodeList[i].head:
            if (not visited[it]):
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
    return graph

def main():
    #Main function to call
    g = read()
    g.connected()

if __name__ == "__main__":
    #If it is being called from the python interpreter, start main
    main()

        
        

    
