#include<iostream>
#include<list>
#include<vector>
#define pb push_back
using namespace std;

class Graph{
     public:
     int V;
     list<int> *adj;

    Graph(int v){
         V=v;
         adj = new list<int>[V];
    }
     void addEdge(int u,int v,bool isUndirected=true){
          adj[u].pb(v);
          if(isUndirected==false){
               adj[v].pb(u);
          }
     }
    void dfsHelper(int node,vector<bool>&visited){
         visited[node]=true;
         cout<<node<<" ";
         for(auto nbr:adj[node]){
              if(!visited[nbr]){
                   dfsHelper(nbr,visited);
              }
         }
     return;
    }
     void dfs(int src){
          vector<bool>visited(V,false);
          dfsHelper(src,visited);
     }

     
   

};

int main(){
Graph g(7);
g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
 
    cout << "Following is Depth First Traversal "
         << "(starting from vertex 2) \n";
    g.dfs(2);
 
    return 0;
}
