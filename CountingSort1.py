arr = [63,25,73,1,98,73,56,84,86,57,16,83,8,25,81,56,9,53,98,67,99,12,83,89,80,91,39,86,76,85]

def countingSort(arr):
	frequencyArray = [0]*100

	for number in arr:
		frequencyArray[number] = frequencyArray[number] + 1

	return frequencyArray

print(countingSort(arr))
