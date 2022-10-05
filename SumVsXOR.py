n = 10

def sumXor(n):
	zeros = 0
	
	if(n == 0 or n == 1):
		return 1

	while(n>1):
		if(n % 2 == 0):
			zeros = zeros + 1

		n = n // 2

	return 2**zeros

print(sumXor(n))
