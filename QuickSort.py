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
