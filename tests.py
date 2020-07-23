import io
import sys
import random
import unittest
import get_quote
from unittest.mock import patch

class TestGetQuotes(unittest.TestCase):

    def test_read_quotes_from_file_returns_list(self):
        rq = get_quote.read_quotes_from_file('quotes.txt')
        self.assertIsInstance(rq, list)
    
    def test_read_quotes_from_file_returns_the_same_number_of_itens_as_lines(self):
        rq = get_quote.read_quotes_from_file('quotes.txt')
        qf = open('quotes.txt', 'r')
        lines = len(qf.readlines())
        qf.close()
        self.assertEqual(len(rq), lines)
    
    def test_get_random_quote_returns_string(self):
        rq = get_quote.get_random_quote()
        self.assertIsInstance(rq, str)
    
    def test_trims_quote_returns_trimmed_string(self):
        rq = get_quote.get_random_quote()
        tq = get_quote.get_trimmed_quote(rq)
        self.assertNotEqual('\n', tq[-1])
    
    def test_get_random_quote_returns_string_present_in_file(self):
        rq = get_quote.get_random_quote()
        qf = open('quotes.txt', 'r')
        quotes = qf.readlines()
        qf.close()
        self.assertIn(rq, quotes)

    def test_get_runs_qty_should_return_one_plus(self):
        with patch.object(sys, 'argv', [random.randint(0, 100)]):
            runs = get_quote.get_runs_qty()
        self.assertGreaterEqual(runs, 1)

if __name__ == '__main__':
    unittest.main()