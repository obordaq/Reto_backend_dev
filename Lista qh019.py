#Numeros repetidos de la lista qh019


repetidos =[]
unico=[]

for n in qh019:
	if n not in unico:
		unico.append(n)
	else:
		repetidos.append(n)
			
print(repetidos)
