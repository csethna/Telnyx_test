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

sym2va = {
'0': 0,
'1': 1,
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
}
# Create symbol-to-value table
