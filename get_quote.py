import random
import sys

def read_quotes_from_file(file):
    qf = open(file, 'r')
    quotes = qf.readlines()
    qf.close()
    return quotes

def get_random_quote():
    quotes = read_quotes_from_file('quotes.txt')
    rnd = random.randint(0, len(quotes)-1)
    return quotes[rnd]

def get_runs_qty():
    try:
        number_of_quotes = sys.argv[1]
        if number_of_quotes > 0:
            return number_of_quotes
        else:
            return 1
    except:
        return 1

def main():
    for i in range(0, get_runs_qty()):
        print(get_random_quote())

if __name__== "__main__":
    main()
