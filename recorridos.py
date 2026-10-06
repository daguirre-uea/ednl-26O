from typing import Optional
import arboles as ar

def dfs(nodo: Optional[ar.Nodo], contador: int):
    # Verificar si el nodo ha sido visitado
    if nodo.secuencia == 0: # No me han vistador
        contador = contador + 1
        nodo.secuencia = contador
        nodo.hijos_sin_visitar = nodo.hijos.copy()
        # TODO: Imprimo mi valor y mi secuencia
    # Verificar si tengo hijos sin vistar
    if len(nodo.hijos_sin_vistar) > 0: # Tengo hijos sin vistar
        # remuevo a mi primer hijo de la lista
        primer_hijo = nodo.hijos_sin_visitar [0]
        nodo.hijos_sin_visitar = nodo.hijos_sin_visitar[1:]
        # TODO: visitar al hijo
    else: # ya visite a todos mis hijos
        # TODO: Regresa al padre

#Crear un arbol desde una lista anidada
lista = ["A", ["B", ["E", "F"], "G"], ["C", "H"], ["D", "I", "J"] ]
raiz = ar.desde_anidado(lista)
# TODO: Llamar a la funcion
