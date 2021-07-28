'''we will find 3sum closest by using simple formula of abs(sumi-target) < abs(result-target) where result would be
sum(sorted(nums[:3]))'''


def closes3sum(nums,target):
    nums.sort()

    result = sum(nums[:3])

    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue

        j,k =i+1,len(nums)-1
        sumi = nums[i]+nums[j]+nums[k]

        while j<k:
            
            if sumi == target:
                return sumi

            if abs(sumi-target)<abs(result-target):
                result = sumi

            if sumi< target:
                j+=1

            elif sumi>target:
                k-=1

    return result



nums = [-1,1,2,-4]
target = 1

print(closes3sum(nums,target))
            