#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#this seems really easy-- just a loop from 1-20, divide and check remainder with mod, and if it hits false, increment and continue

#as a test, do it for 10



#errors: double equals; function missing () and not called; while condition not defined
#not initially setting condition to true
#mixing up assignment vs checking equality AGAIN

#optimizing this... increment by odds? nvm
#okay, try it with 10
#mixing up return and print
#Q-- how to see progress while its working



#ok, reproduced it for 2520
def divx():
	
	num = 12252240
	condition1 = True
	x = 20
	#18 gives  12252240
	
	while condition1 == True:
		
		for i in range (1, x+1):
			if num % i != 0:
				num = num + 1
				break
			if i == x:
				condition1 = False
				print num

	print num
	
	
	#range count down
	#jump 20
	

divx()

#my terminal seems not to answer
#the 18num, * 19 * 20 gives: 4655851200

#finally got it, after several minutes! 232792560

