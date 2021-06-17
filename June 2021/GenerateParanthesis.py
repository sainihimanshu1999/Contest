'''
This question can be done by two methods one is dfs and other is dp method
'''

#dfs

def paran(n):
    if not n:
        return []

    result = []
    left,right=n,n
    dfs(left,right,result,'')
    return result

def dfs(left,right,result,path):
    if right<left or left<0 or right<0:
        return 
    
    if not left and not right:
        result.append(path)

    if left:
        dfs(left-1,right,result,path+'(')
    if right:
        dfs(left,right-1,result,path+')')

    
#dp solution

def paran2(n):
    dp = [[] for _ in range(n+1)]

    dp[0].append('')

    for i in range(n+1):
        for j in range(i):
            dp[i]+= ['('+x+')'+y for x in dp[j] for y in dp[i-j-1]]

    return dp[n]


print(paran2(18))