'''
We use prefix and suffix in that, if prefix is palindrome we check if suffix[::-1] is present in list and if we find one
we prepend to out prefix and return if suffix is palindrome whe check for prefix[::-1] adn if there we append it
'''

def pals(words):
    dic = {w:i for i,w in enumerate(words)}
    result = []

    for i,w in enumerate(words):
        for j in range(len(w)+1):

            prefix,suffix = w[:j],w[j:]

            if prefix == prefix[::-1] and suffix[::-1]!=w and suffix[::-1] in dic:
                result.append([dic[suffix[::-1]],i])

            if j!=len(w) and suffix==suffix[::-1] and prefix[::-1]!=w and prefix[::-1] in dic:
                result.append([i,dic[prefix[::-1]]])

    return result



words = ["abcd","dcba","lls","s","sssll"]
print(pals(words))