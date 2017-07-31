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

# sym2va = {
# '0': 0,
# '1': 1,
# '2': 2,
# '3': 3,
# '4': 4,
# '5': 5,
# '6': 6,
# '7': 7,
# '8': 8,
# '9': 9,
# }
# # Create symbol-to-value table
#
# def string2integer(string, base):
#     integer = 0
#     for character in string:
#         assert character in sym2va, 'Found unknown character!'
#         value = sym2va[character]
#         assert value < base, 'Found digit outside base!'
#         integer *= base
#         integer += value
#         return(integer)
# # Take a string and base to convert to.
# # Allocate space to store your number.
# # For each character in your string:
# #     Ensure character is in your table.
# #     Find the value of your character.
# #     Ensure value is within your base.
# #     Self-multiply your number with the base.
# #     Self-add your number with the digit's value.
# # Return the number.
