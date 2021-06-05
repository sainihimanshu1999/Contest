'''
It was little tricky, but we used the BFS to get out result
'''
from collections import deque

def lock(deadends,target):

    deadset =  set(deadends)
    q = deque([('0000',0)])

    visited = set('0000')

    while q:
        string,steps= q.popleft()

        if string == target:
            return steps

        elif string in deadset:
            continue

        for i in range(4):
            digit = int(string[i])
            for move in [-1,1]:
                new_digit = (digit+move)%10
                new_string = string[:i]+str(new_digit)+string[i+1:]
                if new_string not in visited:
                    visited.add(new_string)
                    q.append((new_string,steps+1))
    return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(lock(deadends,target))