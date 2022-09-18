numberList = [1,2,3,4,3,2,1]

lonelyInteger = 0
for number in numberList:
	if(numberList.count(number) == 1):
		lonelyInteger = number
		break

print(lonelyInteger)

#Another approach without the list's function 'count()' can be seen below: 

#Bubble Sort
#def sortList(arr):
#	
#	for index in range(len(arr)):
#		for indexComparison in range(0, len(arr) - 1 - index):
#		
#			if (arr[indexComparison] > arr[indexComparison + 1]):
#				tempVar = arr[indexComparison + 1]
#				arr[indexComparison + 1] = arr[indexComparison]
#				arr[indexComparison] = tempVar
#
#lonelyInteger = 0
#
#sortList(numberList)
#
#for index in range(0,len(numberList),2):
#	if (index == len(numberList)-1):
#		lonelyInteger = numberList[index]
#		break	
#	
#	if(numberList[index] != numberList[index + 1]):
#		lonelyInteger = numberList[index]
#		break
#
#print(lonelyInteger)
