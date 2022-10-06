a = [2,4]
b = [16,32,96]

def leastCommonMultiple(numberList):
	primeNumbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
	ones = 0
	minimumMultiple = 1

	for prime in primeNumbers:
		count = 0

		if(ones == len(numberList)):
			break
		
		for index in range(0,len(numberList)):
			if(index == 0):
				while(numberList[index] % prime == 0):
					numberList[index] = numberList[index] // prime
					count = count + 1
			else:
				countNext = 0
				while(numberList[index] % prime == 0):
					numberList[index] = numberList[index] // prime
					countNext = countNext + 1

				if(countNext > count):
					count = countNext

			if(numberList[index] == 1):
				ones = ones + 1
				numberList[index] = -1

		minimumMultiple = minimumMultiple*(prime**count)
			
	return minimumMultiple

def minimum(numberList):
	leastNumber = numberList[0]
	
	for number in numberList:
		if(number < leastNumber):
			leastNumber = number

	return leastNumber

def getTotalX(a,b):
	candidates = []
	response = 0
	
	lcm= leastCommonMultiple(a)
	lowerBound = lcm
	upperBound = minimum(b)

	while(lowerBound <= upperBound // 2):
		candidates.append(lowerBound)
		lowerBound = lowerBound + lcm
	
	if(upperBound % lcm == 0):
		candidates.append(upperBound)	

	for candidate in candidates:
		for index in range(0,len(b)):
			if(b[index] % candidate != 0):
				break

			if(index == (len(b) - 1)):
				response = response + 1	

	return response

print(getTotalX(a,b))	
