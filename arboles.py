# Bibliotecas que nos permite manipular tipos de datos
from __future__ import annotations
from typing import Optional, Any

class Nodo:
    # Constructor de la clase Nodo
    # Permite crear objetos de tipo Nodo
    # v: id del nodo, puede ser cualquier tipo de dato
    # p: Opcionalmente puede recibir el parametro p, es de tipo Nodo
    # el valor default de p es None
    # "-> None" significa que el constructor no regresa nada
    def __init__(self, v: Any, p: Optional[Nodo] = None) -> None:
        self.valor = v
        self.padre = p
        # hijo debe ser una lista de objetos de tipo Nodo
        # inicialmente está vacío
        self.hijos: list[Nodo] = []

    # Métodos de la clase Nodo
    # Funciones que calculan "algo" del nodo
    def es_raiz(self) -> bool:
        if self.padre == None:
            return True
        else:
            return False

    def es_hoja(self) -> bool:
        return len(self.hijos) == 0
    
    def grado(self) -> int:
        return len(self.hijos)
    
    def profundidad(self) -> int:
        prof = 0
        nodo_actual = self
        while nodo_actual.padre != None:
            # prof +=1
            prof = prof + 1 
            nodo_actual = nodo_actual.padre
        return prof
    
    def anscestros(self) -> list[Nodo]:
        """
        Returns:
            list[Nodo]: [padre, abuelo, bisabuelo, ..., raiz]
        """
        ansc = []
        nodo_actual = self
        while nodo_actual.padre is not None:
            ansc.append(nodo_actual.padre)
            nodo_actual = nodo_actual.padre
        return ansc
    
    def camino_desde_raiz(self) -> list[Nodo]:
        """Returns:
            list[Nodo]: [raiz,..., bisabuelo, abuelo, padre, self]
        """
        #obtengo los anscestro
        ansc = self.anscestros
        # invierto la lista de anscestro
        ansc_inv = list( reversed(ansc) )
        ansc_inv.append(self)
        return ansc_inv
    
    def hermanos(self) -> list[Nodo]:
        """
        Returns:
            list[Nodo]: Lista de hermanos de self - Hijos del padre
            de self, excepto self
        """
        h = self.padre.hijos
        herm = []
        for i in h:
            if i.valor != self.valor:
                herm.append(i)
        return self.herm
    
    def orden(self) -> int:
        if self is None:
            return 0
        else:
            # n guarda la suma de los ordenes de los hijos de self
            n = 0
            for h in self.hijos:
                n = n + h.orden()
            return 1 + n
    
    def orden1(self) -> int:
        if self is None:
            return 0
        else:
            return 1 + sum(h.orden() for h in self.hijos)
    
    def __repr__(self) -> str:
        return f"Nodo({self.valor!r})"
    
    # Crear función para insertar hijos a un nodo
    # Recibe el id (valor del hijo) y opcionalmente la posición (int)
    # Crear un nodo Nodo (valor, padre=self)
    # Agrego el nuevo nodo a mi lista de hijos
    
#subarblo: puede ser de cualquier tipo - Será una lista, numero, letra
#padre: puede ser de tipo Nodo, None, por default None
#devuelve un objeto de tipo Nodo
def desde_anidado(subarbol: Any, padre: Optional[Nodo] = None) -> Nodo:
    #si subarbol no es una lista
    if not isinstance(subarbol, list):
        # El nuevo nodo es una hoja
        nvo_nodo = Nodo(subarbol, padre)
        return nvo_nodo
    else:
        nvo_nodo = Nodo(subarbol[0],padre)
        for h in subarbol[1:]:
            hijo = desde_anidado(h, nvo_nodo)
            nvo_nodo.hijos.append(hijo)
        return nvo_nodo
    

lista = ["A",["B","D","F"],"C"]
raiz = desde_anidado(lista)
print("Hijo de A: ", raiz.hijos)
print("Orden de A: ", raiz.orden())