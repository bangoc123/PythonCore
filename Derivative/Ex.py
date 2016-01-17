from sympy import *

x,y,z,t = symbols('x y z t')

userInput = input("Nhap vao ham : ")

var = input("Ban muon tinh dao ham theo bien :")

level = input("Ban muon tinh dao ham cap : ")

init_printing(use_unicode=True)

# In ra duoi dang ki hieu toan hoc pprint()
	
pprint(diff(userInput,var,level))