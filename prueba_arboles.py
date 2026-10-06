import arboles as ar
#Crear un arbol desde una lista anidada
lista = ["A", ["B", ["E", "F"], "G"], ["C", "H"], ["D", "I", "J"] ]
raiz = ar.desde_anidado(lista)

# Imprimo los atributos de la raiz
print("Valor: ", raiz.valor)
print("Hijo: ", raiz.hijos)
print("Padre: ", raiz.padre)

# Imprimo los atributos del primer hijo d ela raíz
primer_hijo = raiz.hijos[0]
print("Valor del primer hijo: ", primer_hijo.valor)
print("Padre del primer hijo: ", primer_hijo.padre)
print("Hijos del primer hijo: ", primer_hijo.hijos)