strings = ['ab','abc','abc']
queries = ['ab','abc','bc']

response = []

for query in queries:
	response.append(strings.count(query))

print(response)
