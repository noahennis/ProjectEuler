

#actually euler 10?



#Find the sum of all the primes below two million.
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#iterate through all the numbers up to 2 million
#check if they're prime
#if they are, add sum to result
#print result


def primeCheck(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range (3, int(n**0.5 + 1), 2):
		if n % i == 0:
			return False
	return True
	


#redundant conditions to %2, and skip by 2 in the check?
#generally-- try it on a very small range first, like the given range, before going to the
#huge number; have the range be a variable like "a"

#taking a long time... i should use the sqrt condition instead.

def primeFind():
	sum = 2

	for x in range (3, 2000001, 2):
		if primeCheck(x) == True:
			sum = sum + x
	print sum
		
		
primeFind()

#142913828922


#filter = logic check
#lambda = anonymous functions
#mary functional programming
#map; reduce;

#num_heredoc
'''
*

num_heredoc.strip().split('\n')
#monokai


#git gui
#homebrew -- git install
brew search
brew install 
