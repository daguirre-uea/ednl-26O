print("Hola mundo") 
print("Grupo: ", 5)

# Variables
x = 5
print("x=",x)
nombre = "Juan"
print("Nombre: ", nombre)

# Función sin tipado
def multiplicar(x,y):
    r = x * y
    return r

resultado = multiplicar(9,10)
print("Resultado: ", resultado)

# Función indicando tipos de datos
def sumar(x: int,y:int) -> int:
    r = x + y
    return r

# Listas, conjuntos, diccionarios
lista = [1,2,3,4,5] # Esta ordenada y se pueden repetir elementos

print("Lista: ", lista)
print("lista[3]: ", lista[3])
print("Tamaño de la lista: ", len(lista))
lista.append(6)
print("Lista: ", lista)

conjunto = {1,2,3,3,4,5,1} # No se repiten elementos y no tiene orden
print("Conjunto: ", conjunto)

nodo = {"id": "A", "hijos":["C","S"], "padre": None}

