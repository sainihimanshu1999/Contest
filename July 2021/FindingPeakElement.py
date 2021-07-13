'''It's easy question '''

def peak(nums):
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            return i-1

    return len(nums-1)