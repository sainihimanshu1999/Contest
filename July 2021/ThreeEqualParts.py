'''In this question first step should be to check the number of ones cane be divided into 3 parts and then we check
how the remaining zeroes are distributed among the 3 parts'''

def threeEqual(nums):
    n = len(nums)
    indexs  = [i for i in range(n) if nums[i]==1]
    m = len(indexs)

    if m == 0:
        return [0,2]

    if m%3:
        return [-1,-1]

    p1,p2 = indexs[0],indexs[m//3-1]
    p3,p4 = indexs[m//3],indexs[2*m//3-1]
    p5,p6 = indexs[2*m//3],indexs[-1]

    part1,part2,part3 = nums[p1,p2+1],nums[p3:p4+1],nums[p5:p6+1]

    if part1!=part2 or part2 != part3:
        return [-1,-1]

    l1 = p3-p2-1
    l2 = p5-p4 -1
    l3 =n-p6-1

    if l3>l2 or l3>l1:
        return [-1,-1]

    return [p2+l3,p4+l3+1]