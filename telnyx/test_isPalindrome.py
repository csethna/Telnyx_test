import unittest
from palindrome import isPalindrome

class isPalindromeTestCase(unittest.TestCase):
    # tests for palindromes.py

    def test_isPalindrome(self):
        self.assertTrue(isPalindrome([1001]))

if __name__ == '__main__':
    unittest.main()
