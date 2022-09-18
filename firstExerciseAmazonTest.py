lista = ["88 99 100", "77 77 200", "88 32 400", "99 99 300", "99 88 100", "77 65 500", "54 77 900"]
dicionario = {}

for log in lista:
	transacao = log.split(" ")
	
	if(transacao[0] == transacao[1]):
		if(dicionario.get(transacao[0]) == None):
			dicionario.update({transacao[0]: 1})
		else:
			dicionario.update({transacao[0]: dicionario.get(transacao[0])+1})
	else:
		if(dicionario.get(transacao[0]) == None):
			dicionario.update({transacao[0]: 1})
		else:
			dicionario.update({transacao[0]: dicionario.get(transacao[0])+1})

		
		if(dicionario.get(transacao[1]) == None):
			dicionario.update({transacao[1]: 1})
		else:
			dicionario.update({transacao[1]: dicionario.get(transacao[1])+1})

limite = 2
response = []

for item in dicionario:
	if(dicionario[item] > limite):
		response.append(int(item))	

response.sort()
response = [str(x) for x in response]
print(dicionario)
print(response)
