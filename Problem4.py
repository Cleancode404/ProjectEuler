
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers
#  is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#check if an integer is palindrome 
def isPalindrome(n):
    s = str(n)
    reverseString = ""

    for i in range(len(s) - 1, -1, -1):
        reverseString += s[i]
    return reverseString == s

#find out the product of two 3-digit numbers
def product():
    palindrome = -1
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):

            #check if current palindrome is greater than previous one
            if isPalindrome(i*j) and (i*j) > palindrome:
                palinedrome = i*j
    return palinedrome

print(product())
