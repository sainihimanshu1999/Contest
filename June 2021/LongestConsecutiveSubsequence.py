'''
This question can be solved by using two methods, one is basic iteration and other in recursion(i think in recursion)
the time complexity is slightly less tha iterative one
'''

def lcs1(nums):
    nums = set(nums)
    length = 0

    for x in nums:
        if x-1 not in nums:
            y = x+1
            while y in nums:
                y = y+1
            length = max(length,y-x)

    return length


def lcs2(nums):

    def func(x):
        if x-1 in nums:
            return func(x-1)+1
        return 1


    nums =set(nums)
    ans = 0
    for i in nums:
        ans = max(ans,func(i))

    return ans

nums = [30,80,11,12,98,13,14,67]

print(lcs2(nums))

