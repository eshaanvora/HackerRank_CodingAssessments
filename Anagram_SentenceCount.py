
words = ["bats","tabs","in","cat","act","the"]
sentences = ["cat the bats", "in the act", "act tabs in"]

def solution(words, sentences):

    anagrams = {}
    for i in words:
        #Convert to tuple as list type is not hashable
        i = tuple(sorted(i))
        if i in anagrams:
            anagrams[i] += 1
        else:
            anagrams[i] = 1

    numSentences = []
    for i in sentences:
        tmpCount = 1
        for k in i.split():
            match = tuple(sorted(k))
            if match in anagrams:
                tmpCount *= anagrams[match]

        numSentences.append(tmpCount)

    return numSentences

print(solution(words, sentences))
