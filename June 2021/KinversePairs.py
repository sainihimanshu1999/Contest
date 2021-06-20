'''
calculating the number of k inverse in numbers till range n by using dp
'''

def Kinverse(n,k):
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1


    for i in range(1,n+1):
        for j in range(0,k+1):
            if(j==0):
                dp[i][j]=1
                
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
                if i<=j:
                    dp[i][j] -= dp[i-1][j-i]
                    
            dp[i][j] = dp[i][j]%(10**9+7)
    
    return dp[n][k]


print(Kinverse(3,1))