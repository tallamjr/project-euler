# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

max_three_digit = ( 999*999 )

numbers_list = list(xrange(100, 999))

palindrome_list = []

def palindrome(x,y):
    digit1 = x
    digit2 = y
    if digit1*digit2 < max_three_digit:
        print "Getting there"

palindrome(123, 342)

print numbers_list
