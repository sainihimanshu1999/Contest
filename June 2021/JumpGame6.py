'''
In this question we have used sliding window variation algorithm with dp, this question is pretty clever
'''

from collections import deque

def jump(nums,k):
    dp = [0]*(len(nums))
    dp[0] = nums [0]
    queue = deque([(nums[0],0)])

    for i in range(1,len(nums)):
        dp[i] = nums[i]+queue[0][0]

        while queue and queue[-1][0]<dp[i]:
            queue.pop()
        queue.append((dp[i],i))

        if  i-k == queue[0][1]:
            queue.popleft()
    return dp[-1]


nums = [1,-1,-2,4,-7,3]
k = 2
print(jump(nums,k))
    
