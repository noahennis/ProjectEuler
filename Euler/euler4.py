

#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is:
# 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


#a palindrome checker; can hardcore the number of digits, probably.
#can either turn it into a string and then subset the string
#or... do the mod/division trick, check that the digits equal, and then see if they pass
#what would be a more general case?


#unsure how to handle the counting down; could just do a shotgun of all the numbers and compare?

#999 * 999 = 998001

#one way: start with the two large numbers, and decrement one? 
#so two loops.... seems inefficient, relatively.

#inner loop: decrement number X; check palindrome quality
#outer loop: decrement number Y; check palindrome quality
#if palindrome, test against max; then return new max
#but how to know what the component numbers are, raather than just the sum?
#this just asks for the sum.


#instead of for i in range, i should be doing map, reduce, filter, pipeline, etc

def palindromeCheck():
#checks the digits
#assumes it's going to be 6 or 5 digits

#decomposing digits:


def palindromeFind():
#two loops


palindromeFind()