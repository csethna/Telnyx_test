import unittest
from palindrome import processPalindrome

class isPalindromeTestCase(unittest.TestCase):
    # tests for palindromes.py

    def test_processPalindrome(self):
        self.assertTrue(processPalindrome(2))
        # starts at '2' because there is no base(1) or base(2). see:
        # https://math.stackexchange.com/questions/371972/what-would-base-1-be

if __name__ == '__main__':
    unittest.main()
