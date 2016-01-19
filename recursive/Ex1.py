while True:
	a = int(input("Nhap vao a: "))
	
	if a <= 0:
		print("a phai la so nguyen duong!!!")
		continue
	
	b = int(input("Nhap vao b: "))
	
	if b <=0:
		print("b phai la so nguyen duong!!!")
		continue
	c = b

	def div(c):
		if a % c == 0 and b % c == 0:
			return c
		else:
			return div(c-1)

	print(div(c))