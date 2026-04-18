class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        rgraph = defaultdict(list)
        indegree = [0] * V

        for u in range(V):
            for v in graph[u]:
                rgraph[v].append(u)
            indegree[u] = len(graph[u])
        
        q = deque()
        safenode = []

        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        while q:
            node = q.popleft()
            safenode.append(node)

            for x in rgraph[node]:
                indegree[x] -= 1
                if not indegree[x]:
                    q.append(x)
        safenode.sort()
        return safenode