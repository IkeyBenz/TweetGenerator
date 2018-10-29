import random

def getWordsFrom(filePath="/usr/share/dict/words"):
    return open(filePath, 'r').read().split('\n')

def pickRandomWords(amount, words):
    selectedWords = []
    for _ in range(amount):
        randIndex = random.randint(0, len(words)-1)
        selectedWords.append(words.pop(randIndex))
    return selectedWords

def makeSentenceWith(words):
    return ' '.join(words) + '.'

if __name__ == '__main__':
    words = getWordsFrom()
    selectedWords = pickRandomWords(8, words)
    print(makeSentenceWith(selectedWords))
