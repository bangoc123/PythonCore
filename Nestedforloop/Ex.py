print('  ', end='')
for i in range(1,10):
	print('%3d'%i, end = '')
print('\n')
print('-----------------------------')
for i in range(1,10):
	print('%1d|'%i, end = '')
	for j in range(1,10):	
		print('%3d'%(i*j), end ='')
	print('\n')