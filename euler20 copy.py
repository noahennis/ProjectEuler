
#digitsum

#factorial recursion

def digitSum(n):
	#positives only
	sum = 0
	while n > 0:
		sum = sum + n%10
		n = n / 10
	return sum



def Factorial(n):
	if n < 1:
		return 1
	else: 
		return n * Factorial(n - 1)


digitSum(Factorial(100))

#demo functional programming


#In [60]: Factorial(100)
#Out[60]: 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000L

#648L