'''
making matchsticks into square
'''

def makeSquare(matchsticks):

    if not matchsticks:
        return False

    l = len(matchsticks)

    perimeter = sum(matchsticks)

    possible_side =  perimeter//4

    if possible_side*4 != perimeter:
        return False

    matchsticks.sort(reverse = True)

    sums = [0 for _ in range(4)]


    def dfs(index):

        if index == l:
            return sums[0] == sums[1] == sums[2] == possible_side

        for i in range(4):
            sums[i] += matchsticks[index]
            if dfs(index+1):
                return True
            
            sums[i] -= matchsticks[index]

        return False
    return dfs(0)

matchsticks = [1,1,2,2,2]
print(makeSquare(matchsticks))