'''
We use basic dijsktra algorithm to find the distance between two points, and dijsktra algo is used by implementing min
heap
'''
from heapq import *

def swinRain(grid):
    n = len(grid)
    heap = [(grid[0][0],0,0)]
    visited = set([(0,0)])
    res = 0

    moves = [(1,0),(-1,0),(0,-1),(0,1)]

    for i in range(n*n):
        val,x,y = heappop(heap)
        res = max(val,res)
        if x==n-1 and y==n-1:
            return res

        for dx,dy in moves:
            newx,newy = dx+x,dy+y

            if (newx,newy) not in visited and 0<=newx<n and 0<=newy<n:
                heappush(heap,(grid[newx][newy],newx,newy))
                visited.add((newx,newy))


grid  =[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(swinRain(grid))