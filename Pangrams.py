string = "We promptly judged antique ivory buckles for the prize"

response = set(string.replace(" ", "").casefold())

if(len(response) == 26):
	print("pangram")
else:
	print("not pangram")
