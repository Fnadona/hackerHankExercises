n = 506003
m = 100818

def towerBreakers(n,m):
	if(n % 2 == 0 or m == 1):
		return 2
	else:
		return 1

print(towerBreakers(n,m))
