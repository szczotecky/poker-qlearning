
def modulo (lista, y):
	
	lista_tmp = lista
	n = len(lista)

	for x in range (n):
		if lista[x] <> 255:
			lista_tmp[x] = lista[x]%y
	
	return [lista_tmp]


	#wywalenie z listy pustych kart
def check_card (lista):
	
	lista_tmp = lista
	
	lista_tmp.sort()
	lista_tmp.reverse()
	
	m = lista_tmp.count(255)
	
	if m<>0:
		del lista[0:m+1]
	return [lista]

