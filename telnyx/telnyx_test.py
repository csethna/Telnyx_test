integers = list(range(1000))

palindromes = []

def isPalindrome(*integers):
    for integer in integers:
        if str(integer) == str(integer)[::-1]:
            palindromes.append(integer)
            print(palindromes)
