import random

def read_quotes_from_file(file):
    qf = open(file)
    quotes = qf.readlines()
    qf.close()
    return quotes

def get_random_quote():
    quotes = read_quotes_from_file('quotes.txt')
    rnd = random.randint(0, len(quotes))
    return quotes[rnd]

if __name__== "__main__":
    main()