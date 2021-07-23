'''We have to partition array into disjoint interval one thing we have to keep in mind that minright of interval should be 
greater than or equal to maximum of left interval'''


#O(n) space

def partition(nums):
    n = len(nums)

    minRight = [0]*n
    minRight[n-1] = nums[n-1]

    for i in range(n-2,-1,-1):
        minRight[i] = min(nums[i],minRight[i+1])

    maxLeft = nums[0]

    for i in range(1,n):
        if maxLeft<=minRight[i]:
            return i
        maxLeft = max(maxLeft,nums[i])


#O(1) space

def partition2(nums):
    leftMax = Gmax = nums[0]
    partition = 0

    for i in range(1,len(nums)):
        Gmax = max(Gmax,nums[i])
        if nums[i]<leftMax:
            partition = i
            leftMax = Gmax
    return partition +1
            


nums = [5,0,3,8,6]
print(partition2(nums))