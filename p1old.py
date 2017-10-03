

class node:
    def __init__(self, source, dest, next = 0):
        self.source = source
        self.dest = dest
        self.next = next

class head:
    def __init__(self, head=None):
        self.head = head

class Graph:
    def __init__(self,v):
        self.v = v
        self.nodeList = []
        for i in range(v):
            self.nodeList.append(head())
            
    def addEdge(self, source, dest):
        #One edge
        newNode = node(source, dest)
        newNode.next = self.nodeList[source].head
        self.nodeList[source].head = newNode

def read(Graph):
    pass

def write(Graph):
    pass

def main():
    pass

        
        
