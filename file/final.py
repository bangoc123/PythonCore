import os

currentdir = os.getcwd()

dirs = list(os.walk(currentdir)) 

for i in range(1,len(dirs)):
	
	if len(dirs[i][2]) == 1:
		continue
	
	name = dirs[i][2][1] 

	originPath = dirs[i][0] + '/' +dirs[i][2][1] 
	
	name1 = name[3:6]

	if name1.find('_') > 0:
		newname = '/part' + name1.strip('_').replace('u','0') + '.mp3'
		changeNamePath = currentdir + '/final'+ newname 
		os.rename(originPath,changeNamePath)
	else:
		newname = '/part' + name1.strip('u') + '.mp3'
		changeNamePath = currentdir + '/final'+ newname
		os.rename(originPath,changeNamePath)

	