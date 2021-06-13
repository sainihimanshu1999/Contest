'''
This question was pretty fun, it is more like knapsack problem(in general knapsack problem we would have used dynamic programming)
but in this question we are using heaps(max heaps)
'''

from heapq import *

def refuelingStops(s,fuel,target):
    s = [(0,0)]+s+[(target,0)]
    n = len(s)
    result = 0
    heap = []

    for i in range(1,n):
        fuel -= s[i][0]-s[i-1][0]
        while heap and fuel<0:
            fuel -= heappop(heap)
            result +=1
        if fuel<0: return -1
        heappush(heap,-s[i][1])

    return result

target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]

print(refuelingStops(stations,startFuel,target))
