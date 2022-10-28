def isValid(s):

	if(len(s) == 1 or len(s) == 2):
		return "YES"
	
	countLetters = [0 for i in range(26)]

	for letter in s:
		countLetters[ord(letter) - ord("a")] = countLetters[ord(letter) - ord("a")] + 1

	isFirst = True
	isSecond = True
	countFirst = 0
	countSecond = 0

	for index in range(26):
		if(countLetters[index] != 0 and isFirst):
			firstQuantity = countLetters[index]
			countFirst = countFirst + 1
			isFirst = False
		elif(countLetters[index] != 0 and isSecond and firstQuantity == countLetters[index]):
			countFirst = countFirst + 1
		elif(countLetters[index] != 0 and isSecond and firstQuantity != countLetters[index]):
			secondQuantity = countLetters[index]
			countSecond = countSecond + 1
			isSecond = False
		elif(countLetters[index] != 0 and not isSecond):
			if(countLetters[index] == firstQuantity):
				countFirst = countFirst + 1
			elif(countLetters[index] == secondQuantity):
				countSecond = countSecond + 1
			else:
				return "NO"
			
	if(countSecond == 0):
		return "YES"
	elif(countFirst == 1 and firstQuantity == 1):
		return "YES"
	elif(countSecond == 1 and secondQuantity == 1):
		return "YES"
	elif(firstQuantity - secondQuantity == 1 and (countFirst == 1 or countSecond == 1)):
		return "YES"
	elif(secondQuantity - firstQuantity == 1 and (countFirst == 1 or countSecond == 1)):
		return "YES"
	else:
		return "NO"

s = "aabbccc"

print (isValid(s))
