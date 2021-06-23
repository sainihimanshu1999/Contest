'''
In thsi we can easily check subsequnce by employing two loops, but it will get TLE, so we use dictionary to solve this
problem
'''
from collections import defaultdict

def subsequence(s,words):
    dic = defaultdict(list)
    count = 0

    for word in words:
        dic[word[0]].append(word)


    for char in s:
        dic_value = dic[char]
        dic[char] = []
        for word in dic_value:
            if len(word)==1:
                count +=1
            else:
                dic[word[1]].append(word[1:])

    return count


s = "abcde"
words = ["a","bb","acd","ace"]
print(subsequence(s,words))