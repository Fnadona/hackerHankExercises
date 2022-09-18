s = [4]
d = 4
m = 1

def birthday(s,d,m):
	response = 0

	for index in range(len(s)-m+1):
		sumResult = 0
		for count in range(m):
			sumResult = sumResult + s[index + count]
		if(sumResult == d):
			response = response + 1

	return response

print(birthday(s,d,m))
