import arboles as ar
#Crear un arbol desde una lista anidada
lista = ["A", ["B", ["E", "F"], "G"], ["C", "H"], ["D", "I", "J"] ]
raiz = ar.desde_anidado(lista)

# Imprimo los atributos de la raiz
print("Valor: ", raiz.valor)
print("Hijo: ", raiz.hijos)
print("Padre: ", raiz.padre)

# Imprimo los atributos del primer hijo de la raíz
primer_hijo = raiz.hijos[0]
print("Valor del primer hijo: ", primer_hijo.valor)
print("Padre del primer hijo: ", primer_hijo.padre)
print("Hijos del primer hijo: ", primer_hijo.hijos)

# Imprimir los atributos de H
# nodoH = raiz.hijos[1].hijos[0]
nodoC = raiz.hijos[1]
nodoH = nodoC.hijos[0]
print("Valor nodo H: ", nodoH.valor)

# Imprimir los datos de los hijos A
print("Estos son los hijos de la raíz:")
for hijo in raiz.hijos:
    print("Hijo: ", hijo.valor)
    
print("Estos son los hijos de D:")
nodoD = raiz.hijos[2]
for hijo in nodoD.hijos:
    print("hijos: ", hijo.valor) 
    
padreD = nodoD.padre