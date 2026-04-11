class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m,n = len(image),len(image[0])
        start = image[sr][sc]

        if start == color:
            return image

        def mark(r,c):
            if 0 <= r < m and 0 <= c < n and image[r][c] == start:
                image[r][c] = color
                mark(r+1,c)
                mark(r-1,c)
                mark(r,c+1)
                mark(r,c-1)
        
        mark(sr,sc)

        return image