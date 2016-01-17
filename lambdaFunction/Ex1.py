n = int(input("You want to get Fibonacci number at position: "))

fibo = lambda x: 1 if x <2 else fibo(x-1) + fibo(x-2)

print('The Fibonacci number at position {0} is {1}'.format(n,fibo(n)))