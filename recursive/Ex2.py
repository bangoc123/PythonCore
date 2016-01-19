
lines = int(input('Nhap so dong: '))

def pascal(n,k):
    if (k == 0) or (k == n):
      return 1
    else:
      return pascal(n-1, k-1) + pascal(n-1, k)

for n in range(0,lines):
    print("   "*(lines-n),end="")
    for k in range(0,n+1):    
        print('%5s'%(pascal(n, k)), end=" ")
    print("\n")