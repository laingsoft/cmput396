import sys
'''
Student: Charles Laing ID: 1388069

Greated an adjacency list to store a graph data struct
http://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
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

    def connected(self):
        visited =[]
        [visited.append(False) for i in range(self.v)]
        for i in range(self.v):
            if (visited[i] == false):
                DFSutl(i, visited)
    def DFSutil(i, visited):
        visited[i] = True
        print(i)
        
        
    def __str__(self):
        # build the output here for ease of calling later
        output = ''
        output += str(self.v)
        for i in range(len(self.nodeList)):
            output+=str(len(self.nodeList[i].head))
            output+=''.join(map(str,self.nodeList[i].head))
        return output

def read():
    # Python doesn't have cin like he wants, but I guess this should work. 
    line = map(int, raw_input().split())
    graph = Graph(line.pop(0))
    for i in range(graph.v):
        edgenum = line.pop(0)
        #print("vertex:"+str(i))
        for y in range(edgenum):
         #   print(y, str(line))
            temp = line.pop(0)
            graph.addEdge(i,temp)
          #  print("edge:"+str(temp))
    return graph
        
def write(graph):
    print(graph)

def main():
    #Main function to call
    g = read()
    write(g)

if __name__ == "__main__":
    #If it is being called from the python interpreter, start main
    main()

        
        

    
