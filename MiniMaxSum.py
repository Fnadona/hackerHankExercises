arr = [5,4,3,2,1]

#Bubble Sort
def sortList(arr):
	
	for index in range(len(arr)):
		for indexComparison in range(0, len(arr) - 1 - index):
		
			if (arr[indexComparison] > arr[indexComparison + 1]):
				tempVar = arr[indexComparison + 1]
				arr[indexComparison + 1] = arr[indexComparison]
				arr[indexComparison] = tempVar

def miniMaxSum(arr):

	sortList(arr)
	maximum = 0
	minimum = 0
	
	for index in range(1,len(arr)):
		maximum = maximum + arr[-index]
		minimum = minimum + arr[index-1]

	print(str(minimum) + " " + str(maximum))

miniMaxSum(arr)
