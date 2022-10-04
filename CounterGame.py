n = 1463674015

def binaryNumber(n):
	binaryDigits = []
	isPowerOfTwo = True
	ones = 0
	firstOnePosition = 0
	isFirst = True
	count = 0

	if(n == 1):
		return 1, True, 0, 0

	if(n == 0):
		return 1, False, 0, 0

	while(n>1):
		if(n % 2 == 1):
			isPowerOfTwo = False
			ones = ones + 1
			
			if(isFirst):
				isFirst = False
				firstOnePosition = count
			
		binaryDigits.append(n % 2)
		n = n // 2
		count = count + 1
	
	binaryDigits.append(n)
	
	return len(binaryDigits), isPowerOfTwo, ones, len(binaryDigits) - firstOnePosition - 1

def counterGame(n):
	lengthBinaryNumber, isPowerOfTwo, ones, lastOnePosition = binaryNumber(n)

	if(isPowerOfTwo):
		if(lengthBinaryNumber % 2 == 0):
			return "Louise"
		else:
			return "Richard"
	elif(ones % 2 == 0):
		if((lengthBinaryNumber - lastOnePosition -1) % 2 == 0):
			return "Richard"
		else:
			return "Louise"
	else:
		if((lengthBinaryNumber - lastOnePosition -1) % 2 == 0):
			return "Louise"
		else:
			return "Richard"

print(counterGame(n))
