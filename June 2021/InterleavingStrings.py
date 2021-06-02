'''
This question is done by basic memoization
'''

#recursive apprroach

def interLeave(s1,s2,s3):
    if not s1 and not s2 and not s3:
        return True

    if len(s1)+len(s2) != len(s3):
        return False

    ans = (len(s1)>0 and len(s3)>0 and s1[0]==s3[0] and interLeave(s1[1:],s2,s3[1:])) or (len(s2)>0 and len(s3)>0 and s2[0]==s3[0] and interLeave(s1,s2[1:],s3[1:]))

    return ans



#memoized approach

def interLeave2(s1,s2,s3):
    def func(s1,s2,s3,memo):
        if (s1,s2,s3) in memo:
            return memo[(s1,s2,s3)]
        if not s1 and not s2 and not s3:
            memo[(s1,s2,s3)] = True
            return True

        if len(s1)+len(s2) != len(s3):
            memo[(s1,s2,s3)] = False
            return False

        ans = (len(s1)>0 and len(s3)>0 and s1[0]==s3[0] and func(s1[1:],s2,s3[1:],memo)) or (len(s2)>0 and len(s3)>0 and s2[0]==s3[0] and func(s1,s2[1:],s3[1:],memo))

        memo[(s1,s2,s3)] = ans
        return memo[(s1,s2,s3)]
    return func(s1,s2,s3,{})



s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"

print(interLeave2(s1,s2,s3))