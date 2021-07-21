'''reduction operation are done greedily'''


def reductionQperation(nums):
    ans=val=0

    for i in range(1,len(nums)):
        if nums[i-1]<nums[i]:
            val +=1
        ans +=val
    return ans