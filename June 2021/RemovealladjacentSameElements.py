'''This is pretty easy and it can be done using two approaches, one is recurrsion and other in stack method
'''


#DFS(very time consuming but original)

def adjacentElements(s):
    def dfs(string):
        if not string: return ''

        for i in range(len(string)-1):
            if string[i]==string[i+1]:
                newstr = string[:i]+string[i+2:]
                return dfs(newstr)

        return string

    return dfs(s)


#Stack(great time complexity O(n))

def adjancentElements2(s):
    stack = []
    for c in s:
        if stack and stack[-1]==c:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)


s = "abbaca"
print(adjancentElements2(s))