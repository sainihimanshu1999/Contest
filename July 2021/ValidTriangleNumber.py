'''A triangle is valid if sum of its either two sides are greater than third side'''


def validTriangle(nums):
    count = 0
    nums.sort()

    for i in range(len(nums)-1,1,-1):
        low = 0
        high = i-1

        while low<high:
            if nums[low]+nums[high]>nums[i]:
                count += low-high
                high -=1
            else:
                low +=1


    return count