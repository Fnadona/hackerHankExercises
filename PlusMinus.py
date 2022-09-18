arr = [-1,-50, 4, 67, 0, -4, 0, 4, 5, 0]

def plusMinus(arr):

	countPositive = 0.000000
	countNegative = 0.000000
	countZero = 0.000000

	for number in arr:
		if(number > 0):
			countPositive = countPositive + 1
		elif (number < 0):
			countNegative = countNegative + 1
		else:
			countZero = countZero + 1

	print("%.6f" % (countPositive/len(arr)))
	print("%.6f" % (countNegative/len(arr)))
	print("%.6f" % (countZero/len(arr)))

plusMinus(arr)
