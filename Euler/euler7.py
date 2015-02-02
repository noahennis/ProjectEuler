

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13:
#  we can see that the 6th prime is 13.

# What is the 10 001st prime number?



#two issues:
#1: not counting 3 as prime
#2: reporting a number 1 over the goal prime count

#nb: had not done i in range


def primeCheck(n):
	if n < 2: return False
	if n == 2: return True
	if n % 2 == 0: return False

	for i in range(3, int((n ** 0.5) + 1), 2):
		if n % i == 0:
			return False

	return True




def primeGet(goal):
	primecount = 1  
	number = 3
	
	while primecount < goal:

		if primeCheck(number) == False:
			print number, "is false"
			number+= 1
			
		if primeCheck(number) == True:
			print number, "is true"
			print primecount, "is the primecount"
			primecount+= 1
			number+= 1

		if primecount == goal:
			print "The goal prime is", number - 1  #undoes the last number add when prime == True
			break


#enormously faster with ** 0.5, and same answer

primeGet(10001)
#The goal prime is 104743



