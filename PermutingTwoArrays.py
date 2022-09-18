A = [0,1]
B = [0,2]

k = 1

#Bubble Sort
def sortList(arr):
	
	for index in range(len(arr)):
		for indexComparison in range(0, len(arr) - 1 - index):
		
			if (arr[indexComparison] > arr[indexComparison + 1]):
				tempVar = arr[indexComparison + 1]
				arr[indexComparison + 1] = arr[indexComparison]
				arr[indexComparison] = tempVar

def twoArrays(k, A, B):

	sortList(A)
	sortList(B)


	for numberA in A:
		isNotSatisfied = True
		for numberB in B:
			if(numberA + numberB >= k):
				B.remove(numberB)
				isNotSatisfied = False
				break
	
		if(isNotSatisfied):
			return "NO"

	return "YES"

print(twoArrays(k,A,B))
