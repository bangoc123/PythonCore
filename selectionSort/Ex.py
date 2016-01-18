numList = [2,3,2,2,2,2,2,4,1,5,6,9,7]

# for i in range(len(numbers)-1):
# 	min = i
# 	for j in range(i,len(numbers)):
# 		if numbers[min] >= numbers[j]:
# 			min = j
# 		temp = numbers[i]
# 		numbers[i] = numbers[min]
# 		numbers[min] = temp 

# print(numbers)  

for i in range(len(numList) - 1):
    #i_min = i
    for j in range(i+1, len(numList)):
        if numList[j] < numList[i_min]:
            i_min = j
            numbers[j]  
            numbers[i] = numbers[i_min]
    # temp = numList[i]
    # numList[i] = numList[i_min]
    # numList[i_min] = temp

print(numList)
