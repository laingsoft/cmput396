#include <iostream>
#include <vector>
#include <array>

using namespace std;


class head{
public:
  std::vector<int> head;
};

class Graph{
public:
  int v;
  std::vector<std::vector<int> > nodeList;
  Graph(int v);
  void addEdge(int source, int dest);
  std::vector<std::vector<int> > getCopy(){
    return nodeList;
  }
  
};

void Graph::addEdge(int source, int dest){
  nodeList[source].push_back(dest);
  nodeList[dest].push_back(source);
}

Graph :: Graph(int val){
  v = val;
  for(int i=0; i<v;i++){
    nodeList.push_back(vector<int>());
  }
}


void write(const Graph &g){
  while (!g.nodeList.empty()){
    while(!g.nodeList.back().empty()){
      cout<<g.nodeList.back().back();
      g.nodeList.back().pop_back();
    }
    g.nodeList.pop_back();
  }

}
int main(){
  Graph g(4);
  cout<<"test";
  g.addEdge(1,2);
  g.addEdge(1,3);
  write(g);
  return 0;
}
