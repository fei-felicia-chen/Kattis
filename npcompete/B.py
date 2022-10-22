class Node:
    def __init__(self):
        self.data = []
        self.upp = None
        self.mid = None
        self.low = None
        
    def add(self, n):
        if n not in self.data:
            self.data.append(n)
    
    def createChilds(self, n):
        self.upp = Node()
        self.mid = Node()
        self.low = Node()
        if n > 1:
            self.upp.createChilds(n - 1)
            self.mid.createChilds(n - 1)
            self.low.createChilds(n - 1)

class Tree:
    def __init__(self, n):
        pass
        

tc = int(input())
nc = int(input())
for _ in range(tc):
    d = dict()
    m = -1
    for _ in range(nc):
        c, r, _ = input().split()
        levels = r.split("-")
        levels.reverse()
        nl = []
        for l in levels:
            if l == "upper":
                nl.append(1)
            elif l == "middle":
                nl.append(0)
            else:
                nl.append(-1)
        if len(levels) > m:
            m = len(levels)
        d[c[:len(c) - 1]] = nl
    for k, v in d.items():
        cm = len(v)
        if cm < m:
           for _ in range(m - cm):
               v.append(0)
    ans = []
    while d:
        comp = dict()
        for k, v in d.items():
            comp[k] = v[0]
        h = -1
        for v in comp.values():
            if v > h:
                h = v
        bests = []
        for k, v in 
        
        
    
    
    