s = "baa"

def palindromeIndex(s):
	removedIndex = -1

	if(len(s) % 2 == 0):
		limit = len(s) // 2
	else:
		limit = (len(s) // 2) + 1

	for index in range(0,limit):
		if(s[index] == s[len(s)-1-index]):
			continue
		
		if(s[index] == s[len(s)-2-index]):
			removedIndex = len(s) - 1 - index
			isPalindrome = True
			
			for i in range(index + 1, limit):
				if(s[i] != s[len(s)-2-i]):
					isPalindrome = False
					break

			if(isPalindrome):
				return removedIndex
	
		if(s[index + 1] == s[len(s)-1-index]):
			removedIndex = index
			isPalindrome = True
			
			for i in range(index + 2, limit+1):
				if(s[i] != s[len(s)-i]):
					return -1

			return removedIndex
		else:
			return -1

	return removedIndex

print(palindromeIndex(s))
