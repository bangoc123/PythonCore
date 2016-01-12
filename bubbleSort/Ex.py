import random

characters = {'b', 'k', 'o', 'c', 'z', 'p', 'r', 'a', 't', 'q', 'u', 'n', 'g', 'j', 'w', 'x', 'v', 'f', 'h', 'i', 'e', 'l', 's', 'd', 'y', 'm'}

listOfCharacters = list(characters)

lst = []

for i in range(0,20):
	
	k = []

	m = random.randrange(5,11,1)
	
	for j in range(0,m):
		
		k.append(random.choice(listOfCharacters))
	
	str1 = ''.join(k)

	lst.append(str1)

for i in range(0, len(lst)-1):
	for j in range(i, len(lst)):
		if ord(lst[j][0].upper()) >= ord(lst[i][0].upper()):
			temp = lst[i]
			lst[i] = lst[j]
			lst[j] = temp
print(lst)



