grid=[["ebacd"],["fghij"],["olmkn"],["trpqs"],["xywuv"]]

def partition(arr,leftMark,rightMark):
	pivot = arr[leftMark]
	count = 1

	for index in range(leftMark+1, rightMark+1):
		if(pivot > arr[index]):
			temp = arr[index]
			arr[index] = arr[leftMark + count]
			arr[leftMark + count] = temp
			count = count + 1
	
	temp = arr[leftMark+count-1]
	arr[leftMark+count-1] = pivot
	arr[leftMark] = temp

	return leftMark+count-1

def quickSort(arr,leftMark,rightMark):
	if(leftMark < rightMark):
		lastPivotIndex = partition(arr, leftMark, rightMark)
		quickSort(arr,leftMark,lastPivotIndex-1)
		quickSort(arr,lastPivotIndex+1,rightMark)

def alphabeticallySort(grid):
	sortedGrid = []

	for row in range(0,len(grid)):
		splitedString = [*grid[row][0]]

		for index in range(0,len(splitedString)):
			splitedString[index] = ord(splitedString[index])
		
		quickSort(splitedString,0,len(splitedString)-1)
		sortedGrid.append(splitedString)

	return sortedGrid

def gridChallenge(grid):
	sortedGrid = alphabeticallySort(grid)

	for col in range(0, len(sortedGrid)):
		for row in range(0, len(sortedGrid)-1):
			if(sortedGrid[row][col] > sortedGrid[row+1][col]):
				return "NO"
	return "YES"

print(gridChallenge(grid))
