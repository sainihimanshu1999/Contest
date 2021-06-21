'''
Printing pascal triangle values till an given number
'''
def pascal(num):
    if num==1:
        return [[1]]

    dp = [[1]*(i+1) for i in range(num)]

    for i in range(1,num):
        for j in range(1,i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp


print(pascal(5))

