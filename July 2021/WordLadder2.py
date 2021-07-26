'''In this question we have to provide shortest path to convert on word to another with only one allowed change in a word'''

from collections import defaultdict

def wordLadder2(beginWord,endWord,WordList):
    if endWord not in WordList:
        return []

    wordset = set(WordList)

    layer = {}

    layer[beginWord] = [[beginWord]]


    while layer:
        newlayer = defaultdict(list)

        for word in layer:
            if word == endWord:
                return layer[word]

            for i in range(len(word)):
                for c in  'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i]+c+word[i+1:]

                    if new_word in wordset:
                        newlayer[new_word] += [j+[new_word] for j in layer[word]]

        wordset -= set(newlayer.keys())
        layer = newlayer

    return []


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


print(wordLadder2(beginWord,endWord,wordList))
