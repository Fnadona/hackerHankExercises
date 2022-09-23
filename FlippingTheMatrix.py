matrix = [[112,42,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]]

def flippingMatrix(matrix):
	
	sumMatrix = 0	

	for row in range(1,len(matrix)//2 + 1):
		for col in range(1,len(matrix)//2 + 1):
			
			count = 1
			maxNumber = matrix[row-1][col-1]
		
			while(count<4):
				if(count == 1):
					if(maxNumber < matrix[row-1][-col]):
						maxNumber = matrix[row-1][-col]
				elif(count == 2):
					if(maxNumber < matrix[-row][col-1]):
						maxNumber = matrix[-row][col-1]
				else:
					if(maxNumber < matrix[-row][-col]):
						maxNumber = matrix[-row][-col]
				
				count = count + 1
		
			sumMatrix = sumMatrix + maxNumber

	return sumMatrix

print(flippingMatrix(matrix))
