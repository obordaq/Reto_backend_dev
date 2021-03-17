#Numeros repetidos de la lista qh032


repetidos =[]
unico=[]

for n in qh032:
	if n not in unico:
		unico.append(n)
	else:
		repetidos.append(n)
				
print(repetidos)