# Bibliotecas que nos permite manipular tipos de datos
from typing import Optional, Any
from __future__ import annotations


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
        
        return prof