n = int(input("You want to get Fibonacci number at position: "))

def fibo(n: int):
	if n<2:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)

print('The Fibonacci number at position {0} is {1}'.format(n,fibo(n)))