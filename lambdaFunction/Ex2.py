import functools

#lambda

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

g = lambda x: x%2 ==1

listOfOdd = list(filter(g, foo))

s = lambda x,y: x+y

sumOfOdd = functools.reduce(s,listOfOdd)

print('Sum of odd numbers is: ',sumOfOdd)


#normal

def sumOfOdd2(foo):
	
	sumOfOdd2 = 0
	
	for number in foo:
		
		if number %2 == 1:
			
			sumOfOdd2 += number
			
	return sumOfOdd2

print('Sum of odd numbers is: ',sumOfOdd2(foo))