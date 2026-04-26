#User function Template for python3

class Solution:
    def transitiveClosure(self, N, graph):
        # code here
        
        reach = [[0]*N for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1:
                    reach[i][j] = 1
            reach[i][i] = 1  
        
        for via in range(N):
            for i in range(N):
                for j in range(N):
                    reach[i][j] = reach[i][j] or (reach[i][via] and reach[via][j])
        
        return reach