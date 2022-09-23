ar = [1,2,1,2,1,3,2]

def put(stack, element):
	stack.append(element)

def pop(stack):
	stack.pop(len(stack)-1)

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

def sockMerchant(ar):
	stack = []
	numberPairs = 0

	quickSort(ar,0,len(ar)-1)

	for index in range(0,len(ar)):
		if(len(stack) != 0):
			if(stack[len(stack)-1] == ar[index]):
				pop(stack)
				numberPairs = numberPairs + 1
			else:
				put(stack, ar[index])
		else:
			put(stack,ar[index])

	return numberPairs

print(sockMerchant(ar))
