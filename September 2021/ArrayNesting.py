'''This question can be done by two menthods, one by simple while loop and one by using dfs'''

'''While loop method'''

def arrayNesting(nums):
    result = 0
    length = 0

    visited = [False]*(len(nums))

    for i in range(len(nums)):
        while i not in visited:
            visited[i] = True
            i = nums[i]
            length +=1


        result = max(result,length)

        length = 0


    return result




'''DFS method'''


def arrayNesting2(nums):
    result = 0
    visited = set()

    def dfs(index,length):
        nonlocal result
        nonlocal visited

        if nums[index] in visited:
            result = max(result,length)


        visited.add(nums[index])

        dfs(nums[index],length+1)

    for i in range(len(nums)):
        dfs(i,0)

    return result