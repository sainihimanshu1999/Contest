'''
In this question we are sorting the efficeincy in descending order and zipping speed according to it
'''

from heapq import *

def maxPerfomance(efficiency,speed,k):
    sumi,ans,heap = 0,0,[]

    for eff,speed in sorted(zip(efficiency,speed),reverse=True):
        if len(heap)>k-1:
            sumi -= heappop(heap)

        heappush(heap,speed)

        sumi += speed

        ans = max(ans,eff*sumi)

    return ans



speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2

print(maxPerfomance(efficiency,speed,k))