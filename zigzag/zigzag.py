while True:
	n = int(input("Moi nhap so duong zic zac: "))
	if n<2:
		print("1 zig zag luon co so duong lon hon 1")
		continue

	m = int(input("Moi nhap so diem tren moi duong: "))
	
	if m<2:
		print("1 zig zag luon co so diem tren mot duong lon hon 1")
		continue
	
	# Khoảng cách giữa các đỉnh.

	e = 2*(m-1) 

	# Chiều dài tối đa

	max = n*(m-1) +1

	for i in range(0,m):
		for j in range(1,max+1):
			k = m
			for k in range(k,max,e):
				if n%2 ==0:	
					if j ==(k+i) or j==(k-i):
						print("*", end="")
						break
				elif n%2 ==1:
					if j ==(k+i) or j==(k-i) or j== (k+e*(n//2)-i):
						print("*", end="")
						break
			else:
				print(" ", end="")
		print("")