import io
import unittest
import get_quote

class TestGetQuotes(unittest.TestCase):

    def test_read_quotes_from_file_returns_list(self):
        rq = get_quote.read_quotes_from_file('quotes.txt')
        self.assertIsInstance(rq, list)

    def test_get_random_quote_returns_string(self):
        rq = get_quote.get_random_quote()
        self.assertIsInstance(rq, str)


if __name__ == '__main__':
    unittest.main()