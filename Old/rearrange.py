import sys
from random import randint

def rearrage(words):
    ''' Takes in a list of words and returns a scrambled version '''
    scrambled = []
    for _ in range(len(words)):
        randIndex = randint(0, len(words)-1)
        scrambled.append(words.pop(randIndex))
    return scrambled

if __name__ == '__main__':
    newWords = rearrage(sys.argv[1:])
    print(' '.join(newWords))