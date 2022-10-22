class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def addNext(self, next):
        self.next = next

class Graph:
    def __init__(self, n):
        self.size = n
        self.nodes = []
        for i in range(n):
            self.nodes.append(Node(i))
    
    def addConn(self, outN, inN):
        self.nodes[outN].addNext(inN)
        
    def findCy(self):
        visited = [-1 for _ in range(self.size)]
        for idx in range(self.size):
            if visited[idx] == -1:
                stack = []
                stack.append(idx)
                visited[idx] = 0
                self.dfs(stack, visited)
    
    def dfs(self, stack, visited):
        for idx, node1 in enumerate(self.nodes):
            b = False
            for node2 in self.nodes:
                if node2.data == node1.next.data or node1.data == node2.next.data:
                    b = True
                    break
            if b:
                if visited[idx] == 0:
                    return 1
                elif visited[idx] == -1:
                    stack.append(idx)
                    visited[idx] = 0
                    self.dfs(stack, visited)
            visited[stack[-1]] = 1
            stack.pop()
        return 0

a, b = map(int, input().split())
g = Graph(a)
for _ in range(b):
    c, d = map(int, input().split())
    g.addConn(c, d)
    if g.findCy():
        print("NO")
    else:
        print("YES")

