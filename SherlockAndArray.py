arr = [0,0,2,0]

def balancedSums(arr):
	if(len(arr) == 1):
		return "YES"

	leftSum = 0
	rightSum = 0

	for number in arr:
		rightSum = rightSum + number

	rightSum = rightSum - arr[0]
	
	for index in range(0,len(arr)):
		if(index == len(arr) -1 and leftSum == 0):
			return "YES"

		if(index == len(arr)-1 and leftSum != 0):
			return "NO"
		
		if(leftSum == rightSum):
			return "YES"
		
		leftSum = leftSum + arr[index]
		rightSum = rightSum - arr[index+1]

print(balancedSums(arr))
