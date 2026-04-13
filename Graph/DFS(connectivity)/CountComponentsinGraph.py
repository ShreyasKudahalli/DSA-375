class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        
        def dfs(node):
            stack = [node]
            nodes = 0
            edge_count = 0
            
            while stack:
                curr = stack.pop()
                if visited[curr]:
                    continue
                
                visited[curr] = True
                nodes += 1
                edge_count += len(adj[curr])
                
                for nei in adj[curr]:
                    if not visited[nei]:
                        stack.append(nei)
            
            return nodes, edge_count // 2 
        
        complete = 0
        
        for i in range(n):
            if not visited[i]:
                nodes, edges_count = dfs(i)
                
                if edges_count == nodes * (nodes - 1) // 2:
                    complete += 1
        
        return complete