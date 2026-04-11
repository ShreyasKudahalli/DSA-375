class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        result = []

        def dfs(path,val):
            if val == n-1:
                result.append(path[:])
                return
            
            for nei in graph[val]:
                path.append(nei)
                dfs(path,nei)
                path.pop()
        dfs([0],0)
        return result