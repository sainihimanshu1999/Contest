'''In this question we have to find unique palindormic subsequnce od length #3 only'''

from collections import Counter
import collections

def palindromicSubsequence(s):
    result = set()
    left = set()
    right = Counter(s)

    for i in range(len(s)):
        if s[i] in right:
            right[s[i]] -=1

        if not right[s[i]]:
            right.pop(s[i])

        for j in range(26):
            char =chr(ord('a')+j)
            if char in left and char in right:
                result.add((s[i],char))

        left.add(s[i])

    return len(result)


s = 'aabca'
print(palindromicSubsequence(s))