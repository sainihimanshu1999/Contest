'''In this question we have to find 4 distinct numbers whose sum is equal to target'''


def fourSum(nums,target):
    dic = {}

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sumi = nums[i]+nums[j]

            if sumi in dic:
                dic[sumi].append((i,j))

            else:
                dic[sumi] = [(i,j)]


    result = set()
    for k in dic:
        value = target-k
        if value in dic:
            l1 = dic[k]
            l2 = dic[value]

            for i,j in l1:
                for k,l in l2:
                    if i!=k and i!=l and j!=k and j!=l:
                        ans = [nums[i],nums[j],nums[k],nums[l]]
                        ans.sort()
                        result.add(tuple(ans))

    return list(result)


nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums,target))
