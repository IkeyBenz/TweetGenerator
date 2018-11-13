import random
import sys

def randomWord(lst):
    return lst[random.randint(0, len(lst)-1)]



if __name__ == '__main__':
    print(randomWord(sys.argv[1:]))