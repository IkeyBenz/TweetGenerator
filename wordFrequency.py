import dictionaryWords

def histogram(text):
    words = {}
    for word in text:
        try:
            words[word] += 1
        except:
            words[word] = 1
    return words

def uniqueWords(text):
    accounted = []
    count = 0
    for word in text:
        if word not in accounted:
            count += 1
            accounted.append(word)
    return word

def frequency(word, histogram):
    return histogram[word]