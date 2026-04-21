#User function Template for python3
from typing import List

class disjointset:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        
        if px == py:
            return False
        
        # union by rank
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        return True
        

class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        # code here
        edges.sort(key=lambda x: x[2])
        
        res = 0
        ds = disjointset(V)
        
        
        for u,v,w in edges:
            if ds.union(u,v):
                res += w
        return res