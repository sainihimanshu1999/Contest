'''Custom sort is done using basic dictionary'''

def customSort(order,s):

    if not order:
        return s

    if not s:
        return None

    dic = {}
    result = ''
    for char in s:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1


    for char in order:
        if char in s:
            result += char*dic[char]
            dic.pop(char)

        else:
            continue

    for k,v in dic.items():
        result += k*v

    return result


o = 'cba'
s = 'abcccd'

print(customSort(o,s))
