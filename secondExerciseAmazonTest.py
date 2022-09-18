related = ["1100", "1110", "0110", "0001"]
matrix = []
neighbor = []
notneighbor = []

for string in related:
	matrix.append([*string])

for index in range(1,len(related)):
	if(matrix[0][index] == "1"):
		neighbor.append(index)
	else:
		notneighbor.append(index)

neighborLength = len(neighbor)

for index in neighbor:
	if len(notneighbor) == 0:
		break
	
	for n in notneighbor:
		if(matrix[index][n] == "1"):
			neighbor.append(n)
			notneighbor.remove(n)
if len(notneighbor) == 0:
	return 1
	
print(neighbor)
print(notneighbor)
