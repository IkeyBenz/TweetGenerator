from random import randint

quotes = (
    "It's just a flesh wound.",
    "He's not the Messiah. He's a very naughty boy!",
    "THIS IS AN EX-PARROT!!"
)

def randomQuote():
    return quotes[randint(0, len(quotes))]

if __name__ == '__main__':
    print(randomQuote())