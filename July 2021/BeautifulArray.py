'''This beautiful array question can be done using divide and conquer alogrithm
try to identify is there is any odd even criteris in the array'''


def beautifulArray(n):

    if n == 1:
        return [1]


    left = beautifulArray(n//2)
    right = beautifulArray(n-n//2)

    return [2*x for x in left]+[2*x-1 for x in right]