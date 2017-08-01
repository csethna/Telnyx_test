# Define function for digits and bases
def toDigits(decimal, base):
    digits = []
    while decimal > 0:
      digits.insert(0, decimal % base)
      decimal = decimal//base
    return digits

# Define function to check for palindromes
def isPalindrome(digits):
    palindrome = False
    if digits == digits[::-1]:
       palindrome = True
    return palindrome

# Use previously defined functions to cycle through range
def processPalindrome(n):
    palindromic_numbers={}
    for number in range(0, n):
        for base in range (n, 1, -1):
	    digits = toDigits(number, base)
	    if isPalindrome(digits):
	       palindromic_numbers[number] = base
    return palindromic_numbers


# First 1000 non-negative integers
number = 1000
palindrome = processPalindrome(number)
for decimal in palindrome:
    print decimal, '\t', palindrome[decimal]
