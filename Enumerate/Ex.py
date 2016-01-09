x = [1,5,7,3,8]

dict = (dict(enumerate(x)))

print('x = %s'%(x))

for i in dict.keys():
	print('x[%s] =%s'%(i,x[i]))