queries = [[1,0,5], [1,1,7], [1,0,3], [2,1,0], [2,1,1]]
n = 2

def dynamicArray(n, queries):

	lastAnswer = 0
	arr = []
	count = 0

	response = []

	while(count<n):
		arr.append([])
		count = count + 1

	for query in queries:
		if(query[0] == 1):
			index = (query[1]^lastAnswer)%n
			arr[index].append(query[2])
		else:
			index = (query[1]^lastAnswer)%n
			lastAnswer = arr[index][query[2]%len(arr[index])]
			response.append(lastAnswer)

	print(response)

dynamicArray(n,queries)
