arr = [3,8,9,10,0,23,2,3,1,77,7,15]

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

quickSort(arr,0,len(arr) - 1)

if(len(arr)%2 == 0):
	print((arr[len(arr)//2] + arr[len(arr)//2 + 1])/2)
else:
	print(arr[len(arr)//2])
