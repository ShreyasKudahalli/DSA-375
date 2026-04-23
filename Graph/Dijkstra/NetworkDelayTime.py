class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_heap = [(0,k)]
        edges = defaultdict(list)
        t = 0
        visited = set()

        for u,v,w in times:
            edges[u].append((v,w))

        while min_heap:
            w1,node = heapq.heappop(min_heap)

            if node in visited:
                continue
            t = max(t,w1)

            visited.add(node)

            for n1,w2 in edges[node]:
                heapq.heappush(min_heap,(w2+w1,n1)) 
        return t if len(visited)==n else -1