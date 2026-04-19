class Solution:
    def spanningTree(self, V, edges):
        from collections import defaultdict
        import heapq
        
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        min_heap = [(0, 0)] 
        visited = [False] * V
        
        mst_weight = 0
        
        while min_heap:
            wt, node = heapq.heappop(min_heap)
            
            if visited[node]:
                continue
            
            visited[node] = True
            mst_weight += wt
            
            for neigh, edge_wt in graph[node]:
                if not visited[neigh]:
                    heapq.heappush(min_heap, (edge_wt, neigh))
        
        
        return mst_weight