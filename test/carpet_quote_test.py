import unittest
from src.carpet_quote import CarpetQuote


class CarpetQuoteTest(unittest.TestCase):
    def test_quote_no_rounding(self):
        carpet_quote = CarpetQuote(12.55, 10.0, 10.0, False)
        self.assertEqual(1255, carpet_quote.quote())

    def test_quote_with_rounding(self):
        carpet_quote = CarpetQuote(12.55, 10.0, 10.0, True)
        self.assertEqual(1260, carpet_quote.quote())


if __name__ == '__main__':
    unittest.main()
