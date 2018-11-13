# Making a histogram with a dictionary data type

def histogram(words):
    frequencies = {}
    for word in words:
        if not frequencies[word]:
            frequencies[word] = 0
        frequencies[word] += 1
    return frequencies