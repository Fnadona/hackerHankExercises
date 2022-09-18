arr = [[1,2,3],[4,5,6],[9,8,9]]

primaryDiagonal = 0

for i in range(len(arr)):
	primaryDiagonal = primaryDiagonal +arr[i][i] - arr[i][len(arr)-1-i]

print(abs(primaryDiagonal))
