def minimumBribes(q):
	count = 0

	for index in range(len(q)):
		if(q[index] - index -1 > 2):
			return "Too chaotic"
		if(q[index] - index -1 <= 0):
			aux = index + 1 - q[index]
			for i in range(index-1, index - aux - 3, -1):
				if(index != 0 and q[index] < q[i] and i>=0):
					count += 1
	return count	

q = [1,2,5,3,7,8,6,4]

print(minimumBribes(q))
