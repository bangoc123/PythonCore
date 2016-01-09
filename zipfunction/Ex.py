x = [9, 2, 3, 2, 1, 2]
y = [4, 5, 6, 7, 12, 15]

b = list(zip(x,y))

for a in zip(x,y):
	if sum(a)>10:
		b.remove(a)

print(b)