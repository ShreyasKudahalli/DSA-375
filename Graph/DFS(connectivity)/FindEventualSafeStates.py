class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n
        
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            
            state[node] = 1
            
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            state[node] = 2 
            return True
        
        result = []
        
        for i in range(n):
            if dfs(i):
                result.append(i)
        
        return result