'''
We use basic memoization in this question
'''

def boundary(startrow,startcol,maxMove,m,n):
    def dfs(moves,i,j,memo):
        if (moves,i,j) in memo:
            return memo[(moves,i,j)]
        
        if moves == 0:
            return 0
        
        result = 0
        
        for x,y in[(0,1),(0,-1),(1,0),(-1,0)]:
            newx = i+x
            newy = j+y
            if 0<=newx<m and 0<=newy<n:
                result += dfs(moves-1,newx,newy,memo)
            else:
                result +=1
        memo[(moves,i,j)] = result
        return result
    return dfs(maxMove,startrow,startcol,{})

m = 1
n = 3
maxMove = 3
startRow = 0
startCol = 1

print(boundary(startRow,startCol,maxMove,m,n))