import unittest
from palindrome import toDigits

class toDigitsTestCase(unittest.TestCase):
    # tests for palindromes.py

    def test_five_toDigits(self):
        self.assertTrue(toDigits(5, 10)) # 5, base(10)

if __name__ == '__main__':
    unittest.main()
