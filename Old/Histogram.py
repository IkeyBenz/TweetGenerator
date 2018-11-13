import random
class Histogram:
    def __init__(self, wordsLst):
        self.frequencies = self.generate(wordsLst)

    def generate(self, words):
        freqs = {}
        for word in words:
            if word not in freqs:
                freqs[word] = 0
            freqs[word] += 1 
        return freqs

    def chooseWeightedlyRandomWord(self):
        words = [word for word in self.frequencies.keys()]
        frequencies = self.frequencies.values()
        accumulator = 0
        accumulated = []
        for frequency in frequencies:
            accumulator += frequency
            accumulated.append(accumulator)
        rand = random.randint(0, accumulator)
        for number in accumulated:
            if rand <= number:
                index = accumulated.index(number)
                return words[index]
    
    def generateProbableSenetence(self, length):
        chosenWords = [self.chooseWeightedlyRandomWord() for _ in range(length)]
        return ' '.join(chosenWords) + '.'
        

# testWordsList = ['hello', 'there', 'hello', 'my', 'hello', 'name', 'my','ikey', 'is', 'is', 'my']
# h = Histogram(testWordsList)
# print(h.generateProbableSenetence(11))
