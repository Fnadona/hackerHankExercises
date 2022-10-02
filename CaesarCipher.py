s = "159357lcfd`()[]{}?*<"
k = 98

def caesarCipher(s,k):
	alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	symbols = ["-","_","\'","&","!",".","1","2","3","4","5","6","7","8","9","0","`","/","(",")","[","]","{","}","?","*","<"]
	s = [*s]

	queue = []
	indexMatrix = []
	
	response = ""

	for index in range(0,len(s)):
		character = s[index].lower()
		
		if(character in symbols):
			continue

		if(character not in queue):
			queue.append(character)
			indexMatrix.append([index])
		else:
			indexMatrix[queue.index(character)].append(index)
	
	for letter in queue:
		index = (alphabet.index(letter) + k) % 26

		for position in indexMatrix[queue.index(letter)]:
			if(s[position].isupper()):
				s[position] = alphabet[index].upper()
			else:
				s[position] = alphabet[index]
	
	for symbol in s:
		response = response + symbol
	
	print(response)

caesarCipher(s,k)
