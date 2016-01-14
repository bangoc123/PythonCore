import random

numList = []

for i in range(20):
    numList.append(random.randint(1, 100))

for i in range(len(numList)):
	for k in range(i,0,-1):
		if numList[k] <= numList[k-1]:
			temp = numList[k]
			numList[k] = numList[k-1]
			numList[k-1] = temp
print(numList) 
