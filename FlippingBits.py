integer=9

binaryBase = [0]*32
index = 1
response = 0

while(integer!=0):
	binaryBase[-index] = integer%2
	integer = integer//2
	index = index + 1

for number in range(31,-1,-1):
	if(binaryBase[number] == 0):
		binaryBase[number] = 1
	else:
		binaryBase[number] = 0
	
	response = response + (2**(31-number))*binaryBase[number]

print(response)
