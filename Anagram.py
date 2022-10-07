s = "abccde"

def anagram(s):
	if(len(s) % 2 != 0):
		return -1
	
	first = [0]*26
	second = [0]*26

	response = 0

	for index in range(0, len(s)):
		if(index < len(s) // 2):
			first[ord(s[index])-ord("a")] = first[ord(s[index]) - ord("a")] + 1
		else:
			second[ord(s[index])-ord("a")] = second[ord(s[index]) - ord("a")] + 1

	for index in range(0,26):
		result = first[index] - second[index]
		if(result > 0):
			response = response + result

	return response

print(anagram(s))
