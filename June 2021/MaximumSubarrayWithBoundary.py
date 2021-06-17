'''
In this question we are using two pointers
'''

def subarrayBoundary(nums,L,R):
    leftIndex,rightIndex=-1,-1
    result = 0

    for i,num in enumerate(nums):
        if num>=L:
            rightIndex = i

        if num>R:
            leftIndex = i

        result += rightIndex-leftIndex

    return result


nums = [2,1,4,3]
print(subarrayBoundary(nums,2,3))