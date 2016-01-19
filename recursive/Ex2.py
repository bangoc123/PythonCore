
lines = int(input('Nhap so dong: '))

def pascal(i,j):
    if (j == 0) or (j == i):
      return 1
    else:
      return pascal(i-1, j-1) + pascal(i-1, j)

for i in range(0,lines):
    print("   "*(lines-i),end="")
    for j in range(0,i+1):    
        print('%5s'%(pascal(i, j)), end=" ")
    print("\n")