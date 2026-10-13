import arboles as ar
from typing import Optional
import inspect #para ver la pila de la llamadas 

def dfs_preorden_recursivo(nodo: Optional[ar.Nodo], contador: int):
    print("Tamaño de la pila: ", len(inspect.stack()) )
    print("Llamada: ", nodo, ", ", contador)
    # Si soy la raíz -> termino
    if nodo == None:
        return 

    # Si no he sido visitado - Me asigno una secuencia
    if nodo.secuencia == 0:
        # Incremento el contador
        contador = contador + 1
        # Me asigno secuencia
        nodo.secuencia = contador

    # Si tengo hijo por visitar -> Visito al primer hijo
    if len(nodo.hijos_sin_visitar) > 0:
        # Saco al primero de la lista
        hijo = nodo.hijos_sin_visitar[0]
        nodo.hijos_sin_visitar = nodo.hijos_sin_visitar[1:]
        # Visito
        dfs_preorden_recursivo(hijo, contador)
    # Si ya visite a todos mis hijos -> Regresa al padre
    else:
        dfs_preorden_recursivo(nodo.padre, contador)

lista = ["A", ["B", ["E", "F"], "G"], ["C", "H"], ["D", "I", "J"] ]
raiz = ar.desde_anidado(lista)

dfs_preorden_recursivo(raiz, 0)