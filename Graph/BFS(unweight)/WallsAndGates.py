from os import *
from sys import *
from collections import *
from math import *

def wallsAndGates(a, n, m): 
    # Write your Code here.

    q = deque()

    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                q.append((i,j,0))

    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    while q:
        r,c,length = q.popleft()
        
        for dr,dc in dirs:
            nr,nc = r+dr,c+dc
            if 0 <= nr < n and 0 <= nc < m and a[nr][nc]>0:
                if a[nr][nc] > length+1:
                    a[nr][nc] = length+1
                    q.append((nr,nc,length+1))
    return a