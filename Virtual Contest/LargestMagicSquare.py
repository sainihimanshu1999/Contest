'''In the magic square every row and col and diagonals have equal sum, we find this by using simple recursion'''

def largestMagicSqaure(grid):

    def magicSquare(i,j,l):
        s = set()
            
        for x in range(l):
            sumi = 0
            for y in range(l):
                sumi += grid[i+x][j+y]
            s.add(sumi)
            if len(s)>1:
                return False
            
        
        for y in range(l):
            sumi=0
            for x in range(l):
                sumi += grid[i+x][j+y]
                
            s.add(sumi)
            if len(s)>1:
                return False
            
        sumi = 0
        for x in range(l):
            sumi += grid[i+x][j+x]
            
        s.add(sumi)
        if len(s)>1:
            return False
        
        sumi = 0
        for x in range(l):
            sumi += grid[i+x][j+l-1-x]
        s.add(sumi)
        if len(s)>1:
            return False
        
        
        return True

    

    m = len(grid)
    n = len(grid[0])
    
    l = min(m,n)
    
    for k in range(l,1,-1):
        for i in range(m-k+1):
            for j in range(n-k+1):
                if magicSquare(i,j,k):
                    return k
                
    
    return 1



grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]

print(largestMagicSqaure(grid))