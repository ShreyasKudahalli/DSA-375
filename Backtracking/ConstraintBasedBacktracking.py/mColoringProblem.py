# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        
        adj = [[] for _ in range(v)]
        for u, w in edges:
            adj[u].append(w)
            adj[w].append(u)

        color = [0] * v

        def possible(node, col):
            for nei in adj[node]:
                if color[nei] == col:
                    return False
            return True
            
        
        def backtrack(node):
            if node == v:
                return True
            
            for i in range(1,m+1):
                if possible(node,i):
                    color[node]=i
                    if backtrack(node+1):
                        return True
                    color[node]=0
            return False
        return backtrack(0)
        
                    