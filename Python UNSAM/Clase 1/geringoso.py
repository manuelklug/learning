# geringoso.py

cadena = "Geringoso"
capadepenapa = ""

for c in cadena:
	if c == "a":
		capadepenapa += c+"pa"
	elif c == "e":
		capadepenapa += c+"pe"
	elif c == "i":
		capadepenapa += c+"pi"
	elif c == "o":
		capadepenapa += c+"po"
	elif c == "u":
		capadepenapa += c+"pu"
	else:
		capadepenapa += c

print(capadepenapa)
