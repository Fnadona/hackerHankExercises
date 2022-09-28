n = 95073
p = 17440

def pageCount(n,p):
	difference = n-p

	if(difference < p):
		if(difference % 2 == 0):
			return difference // 2
		elif(n % 2 == 0):
			return (difference + 1) // 2
		else:
			return (difference - 1) // 2
	else:
		if(p % 2 == 0):
			return p // 2
		else:
			return (p - 1) // 2

print(pageCount(n,p))
