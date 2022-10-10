from collections import defaultdict


class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
 
    def addEdge(self, u, v):
        self.graph[u - 1].append(v - 1)
 
    # Recursively find the parent of the subset
    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        if parent[i] != i:
            return self.find_parent(parent, parent[i])
 
    # A unite of two subsets
    def union(self, parent, x, y):
        parent[x] = y
 
    # Check if the graph is cyclic by checking if they have same parents
    def is_cyclic(self):
        parent = [0]*(self.V)
        for i in range(self.V):
            parent[i] = i
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)
        return False
                
num_houses, num_cables = map(int, input().split())
g = Graph(num_houses)
for _ in range(num_cables):
    a, b = map(int, input().split())
    g.addEdge(a, b)

if (g.is_cyclic() and 0 in g.graph) or (num_cables==1 and ([0] in g.graph.values() or 0 in g.graph)):
    print("Connected")
    
elif g.is_cyclic():
    for k in sorted(g.graph):
        print(k+1)                      # i did -1 on line 11 so it doesn't give index out of range
else:
    for k, _ in sorted(g.graph):
        pass