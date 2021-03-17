#Numeros repetidos de la lista qh041

repetidos =[]
unico=[]

for n in qh041:
	if n not in unico:
		unico.append(n)
	else:
		repetidos.append(n)
		
		
print(repetidos)