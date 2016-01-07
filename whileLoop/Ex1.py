#gcd = GreatestCommonDivisor

a = int(input("Enter first integer: "))

b = int(input("Enter second integer: ")) 

if a == 0 and b == 0:
	print("Do not exsist divisor")
elif a!=0 and b == 0:
	print('The greatest common divison for',a,'and',b,'is',abs(a))
elif a==0 and b != 0:
	print('The greatest common divion for',a,'and',b,'is',abs(b))
else:
	if a<b: 
		min = a
	else:
		min = b

	gcd = min

	while gcd <= min:
		if(a%gcd ==0 and b%gcd ==0):
			print('The greatest common divison for',a,'and',b,'is',gcd)
			break
		gcd -= 1

