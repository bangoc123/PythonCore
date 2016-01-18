M = int(input("Type the amount: "))

R = float(input("Type the interest per month(%): "))

N = int(input("Type the number of months: "))

def interestCalculation(amount, rate, months):
	
	interestedAmountNmonths = amount
	
	for i in range(months):

		interestedAmountNmonths = interestedAmountNmonths * (1+rate/100)

	return (interestedAmountNmonths, interestedAmountNmonths - amount)

print('The amount in your account is: %.2f and the real interest amount is: %.2f'%interestCalculation(M,R,N))