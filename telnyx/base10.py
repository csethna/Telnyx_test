# This script was for testing logic and only iterates through a base(10) list
integers = list(range(1000))
# Creates a list with integers 0 - 999

palindromes = []
# Creates blank list for storing base(10) palindromic integers

def isPalindrome(*integers):
    for integer in integers:
        if str(integer) == str(integer)[::-1]:
            palindromes.append(integer)
    return(palindromes)
# User defined function loops through 'integers' list to detect palindromes
# Palindromes are added to the new list 'palindromes'
