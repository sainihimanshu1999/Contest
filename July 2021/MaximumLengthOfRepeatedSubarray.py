'''This question is similar to length of the longest substring'''


def repeatedSubarray(A,B):
    m = len(A)
    n = len(B)

    if m==0 or n==0:
        return 0


    if m==1 and n==1:
        if A[0] == B[0]:
            return 1
        else:
            return 0


    dp = [[0]*(n+1) for _ in range(m+1)]
    result = 0


    for i in range(1,m+1):
        for j in range(1,n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j]=0
            
            result = max(result,dp[i][j])
    
    return result


nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,5,6]

print(repeatedSubarray(nums1,nums2))