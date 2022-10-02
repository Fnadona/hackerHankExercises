k = 3
arr = [100,200,300,350,400,401,402]

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

def maxMin(k, arr):
	quickSort(arr,0,len(arr)-1)
	
	count = 1
	minimum = arr[k-1] - arr[0]
	
	while(count + k - 1 < len(arr)):
		if((arr[count + k-1] - arr[count]) < minimum):
			minimum = arr[count+k-1] - arr[count]

		count = count + 1

	print(minimum)

maxMin(k,arr)
