class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])

        def mark(i,j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'T'
                mark(i+1,j)
                mark(i-1,j)
                mark(i,j+1)
                mark(i,j-1)
        
        for i in range(m):
            for j in range(n):
                if i==0 or j== 0 or i==m-1 or j==n-1 and board[i][j] == 'O':
                    mark(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'


        