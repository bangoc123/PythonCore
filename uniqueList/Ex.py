names = ['Juice', 'Tomato', 'Potatoes', 'Banana', 'Tomato', 'Banana']

uniqueNames = []

for name in names:
	if uniqueNames.count(name) == 0:
		uniqueNames.append(name)

counter = []

for name in uniqueNames:
	count = names.count(name)
	counter.append(count)

zipped = zip(uniqueNames,counter)

print(list(zipped))