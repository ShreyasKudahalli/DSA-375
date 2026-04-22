class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        import heapq
        from collections import defaultdict
        
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w)) 
            
        
        dist = [float('inf')]*V
        dist[src] = 0
        
        
        min_heap = [(0,src)]
        
        while min_heap:
            wt,node = heapq.heappop(min_heap)
            
            if wt > dist[node]:
                continue
            
            for neigh, wt in graph[node]:
                if dist[node] + wt < dist[neigh]:
                    dist[neigh] = dist[node] + wt
                    heapq.heappush(min_heap, (dist[neigh], neigh))
        return dist
            