numList = [9, 3, 2, 5, 6, 8, 11]

list1 = []

list2 = []

for num in numList:
	if num<=5:
		list1.append(num)
	else:
		list2.append(num)

Result = (sorted(list1),sorted(list2))

print(Result)
