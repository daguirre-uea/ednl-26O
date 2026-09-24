class Nodo:
    # Constructor
    def __init__(self, identificador, padre, hijos):
        # atributos
        self.identificador = identificador
        self.padre = padre
        self.hijos = hijos
    
    # métodos
    def es_hoja(self):
        if len(self.hijos) == 0:
            return True
        else:
            return False

mi_nodo = Nodo("B", "A", ["D","E"])
print(mi_nodo.es_hoja())
hijos = mi_nodo.hijos

print(hijos)
print("padre: ",  mi_nodo.padre)

raiz = Nodo("C",None, ["G","H"])