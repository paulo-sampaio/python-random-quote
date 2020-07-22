import random

def primary():

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    rnd = random.randint(0, len(quotes))
    print(quotes[rnd])

if __name__== "__main__":
    primary()
