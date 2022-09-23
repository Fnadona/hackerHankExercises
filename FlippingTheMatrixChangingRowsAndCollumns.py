from QuickSort import *

matrix = [[112,42,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]]

def partitionM(arr,leftMark,rightMark):
	pivot = arr[leftMark][1]
	count = 1

	for index in range(leftMark+1, rightMark+1):
		if(pivot > arr[index][1]):
			temp = arr[index]
			arr[index] = arr[leftMark + count]
			arr[leftMark + count] = temp
			count = count + 1
	
	temp = arr[leftMark+count-1]
	arr[leftMark+count-1] = arr[leftMark]
	arr[leftMark] = temp

	return leftMark+count-1

def quickSortM(arr,leftMark,rightMark):
	if(leftMark < rightMark):
		lastPivotIndex = partitionM(arr, leftMark, rightMark)
		quickSortM(arr,leftMark,lastPivotIndex-1)
		quickSortM(arr,lastPivotIndex+1,rightMark)

sumRowVector = []

for row in range(len(matrix)):
	sumRow = 0

	for col in range(len(matrix)):
		sumRow = sumRow + matrix[row][col]	

	sumRowVector.append([row,sumRow])

quickSortM(sumRowVector,0,len(matrix)-1)

print(sumRowVector)
print(len(matrix)-1)

maxSum = []

for col in range(0, len(matrix)):
	sumCol = 0
	
	for index in range(len(matrix)-1,len(matrix)//2-1, -1):
		sumCol = sumCol + matrix[sumRowVector[index][0]][col]

	maxSum.append(sumCol)

quickSort(maxSum,0, len(maxSum)-1)
finalSum = 0
for index in range(len(matrix)-1, len(matrix)//2-1, -1):
	finalSum = finalSum + maxSum[index]

print(maxSum)

print(finalSum)
