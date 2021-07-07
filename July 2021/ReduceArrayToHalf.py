'''In this question we use dictionary and count the frequeny of the elements and add the maximum frequence elements
in the set till the number of the elements in the array does not become half'''

from collections import Counter

def reduceArray(arr):
    n = len(arr)//2
    count = Counter(arr)
    count = sorted(count.items, key = lambda x:-x[1])

    result = 0

    for k,v in count:
        if n>0:
            n -= v
            result+=1
        else:
            break
    return result