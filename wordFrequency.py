import dictionaryWords
import random

def histogram(text):
    frequencies = {}
    words = text.split(' ') if type(text) == str else text
    for word in words:
        try:
            frequencies[word] += 1
        except:
            frequencies[word] = 1
    return frequencies

def uniqueWords(text):
    accounted = []
    count = 0
    words = text.split(' ') if type(text) == str else text
    for word in words:
        if word not in accounted:
            count += 1
            accounted.append(word)
    return word

def frequency(word, histogram):
    return histogram[word]

# Probably terrible run time and aweful memory usage
def chooseWordBasedOn(histogram):
    words = []
    for word, frequency in histogram.items():
        for _ in range(frequency):
            words.append(word)
    return words[random.randint(0, len(words)-1)]

# Test for the above function's accuracy
def test():
    text = open('oneFish.txt', 'r').read()
    frequencies = histogram(text)
    word = chooseWordBasedOn(frequencies)
    return word

if __name__ == '__main__':
    print(test())