names = ["Car","Bus","Taxi","Bus","Taxi","Bus","Taxi","Bus"]

uniqueNames = [] 

def unique(names):
	for name in names:
		if uniqueNames.count(name) == 0:
			uniqueNames.append(name)
	return uniqueNames

print(unique(names))