'''We find longest increasing subsequence using additonal aray'''


def longestInceasingSubsequence(nums):
    result = [1]*len(nums)

    for i in range(len(nums)):
        for j in range(i):
            
            if nums[i]>nums[j]:
                if result[i] == result[j]:
                    result[i] +=1


    return max(result)