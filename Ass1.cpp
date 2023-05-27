#include <iostream>
#include <vector>

using namespace std;

void dfs(vector<vector<int>>& graph, int node, vector<bool>& visited) {
    visited[node] = true;
    cout << node << " ";

    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(graph, neighbor, visited);
        }
    }
}

void bfs(vector<vector<int>>& graph, int start_node, vector<bool>& visited) {
    vector<int> q;
    q.push_back(start_node);

    while (!q.empty()) {
        int node = q.front();
        q.erase(q.begin());

        if (!visited[node]) {
            visited[node] = true;
            cout << node << " ";

            for (int neighbor : graph[node]) {
                if (!visited[neighbor]) {
                    q.push_back(neighbor);
                }
            }
        }
    }
}

int main() {
    int n, m, start_node;
    cout << "Enter the number of nodes and edges: ";
    cin >> n >> m;

    cout << "Enter the edges:\n";
    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    cout << "Enter the starting node: ";
    cin >> start_node;

    cout << "DFS traversal: ";
    vector<bool> visited(n, false);
    dfs(graph, start_node, visited);

    cout << "\nBFS traversal: ";
    visited.assign(n, false);
    bfs(graph, start_node, visited);

    return 0;
}


Output:
Enter the number of nodes and edges: 5 4
Enter the edges:
0 1
0 2
1 3
1 4
Enter the starting node: 0
DFS traversal: 0 1 3 4 2 
BFS traversal: 0 1 2 3 4 

