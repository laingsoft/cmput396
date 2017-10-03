#include <iostream>
#include <vector>
#include <array>

using namespace std;


class head{
public:
  std::vector<int> head;
};

class Graph{
  int v;
  std::vector<head> nodeList;
public:
  Graph(int v);
  void addEdge(int source, int dest);
  
};

Graph :: Graph(int v){
  this.v = v;
}

int main(){
  return 0;
}
