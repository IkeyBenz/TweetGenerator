# Making a histogram with a two dimentional list

def histogram(words):
    frequencies = []
    for word in words:
        findAndIncriment(frequencies, word)
    return frequencies

def findAndIncriment(lsts, word):
    incrimented = False
    for lst in lsts:
        if lst[0] == word:
            lst[1] += 1
            incrimented = True
    if not incrimented:
        lsts.append([word, 1])