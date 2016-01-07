
while True:
	number = int(input("Input an odd number:"))
	if number%2 == 0:
		print("Sorry, the number you enter is even number")
		continue
	else:
		for i in range(number,0,-2):
			t = int((number-i)/2)
			for k in range(0,t):
				print(" ", end="")
			for j in range(0,i):
				print(i, end='')
			print("")
