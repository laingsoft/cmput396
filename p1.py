


class head:
    def __init__(self, head=None):
        self.head = []

class Graph:
    def __init__(self,v):
        self.v = v
        self.nodeList = []
        for i in range(v):
            self.nodeList.append(head())
            
    def addEdge(self, source, dest):
        self.nodeList[source].head.append(dest)
        self.nodeList[dest].head.append(source)
        
    def __str__(self):
        output = ''
        output += str(self.v)
        for i in range(len(self.nodeList)):
            output+=str(len(self.nodeList[i].head))
            output+=''.join(map(str,self.nodeList[i].head))
        return output

def read(Graph):
    pass

def write(Graph):
    print(Graph)

def main():
    pass

        
        
