'''
This question is similar to the question of counting the number of islands
'''

def maxArea(grid):
    m = len(grid)
    n = len(grid[0])

    areas = []

    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                areas.append(dfs(i,j))
    return max(areas) if areas else 0

def dfs(i,j,grid):
    m = len(grid)
    n = len(grid[0])

    if 0<=i<m and 0<=j<n and grid[i][j]:
        grid[i][j] = 0
        return 1+dfs(i+1,j,grid)+dfs(i-1,j,grid)+dfs(i,j+1,grid)+dfs(i,j-1,grid)
    return 0

