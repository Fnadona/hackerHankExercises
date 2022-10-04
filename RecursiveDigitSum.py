n = "148"
k = 3

def calculateSuperDigit(n):	
	if(len(n)==1):
		return int(n)
	else:
		sumResponse = 0
			
		for number in n:
			sumResponse = sumResponse + int(number)
		
		return calculateSuperDigit(str(sumResponse))

def superDigit(n,k):
	response = str(k*calculateSuperDigit(n))

	if(len(response) > 1):
		return calculateSuperDigit(response)
	else:
		return int(response)

print(superDigit(n,k))
