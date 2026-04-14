class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        group = [-1] * n

        def dfs(i,g):
            group[i] = g

            for x in graph[i]:
                if group[x] == -1:
                    if dfs(x,1-g) == False:
                        return False
                if group[x]==g:
                    return False
            return True

        for i in range(n):
            if group[i] == -1:
                if dfs(i,0) == False:
                    return False
        return True