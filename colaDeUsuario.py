class nodoCancion:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None

class colaCanciones:
    def __init__(self):
        self.head = None
        self.grafica = "digraph { rankdir=LR; node[shape = box]; "
    def encolar(self, cancion):
        nuevoNodo = nodoCancion(cancion)
        if self.head is None:
            self.head = nuevoNodo
            nuevoNodo.siguiente = self.head
        else:
            nodoaux = self.head
            while nodoaux.siguiente != self.head:
                nodoaux = nodoaux.siguiente
            nodoaux.siguiente = nuevoNodo
            nuevoNodo.siguiente = self.head

    def desencolar(self):
        if self.head is not None:
            aux = self.head
            while aux.siguiente != self.head:
                aux = aux.siguiente
            print "Desencolo: " + str(self.head.cancion)
            song = self.head.cancion
            self.head = self.head.siguiente
            aux.siguiente = self.head
            return song

    def recorrer(self):
        if self.head is not None:
            nodo = self.head.siguiente
            print "Dato de cola: " + str(self.head.cancion)
            while nodo != self.head:
                print "Dato de cola: " + str(nodo.cancion)
                nodo = nodo.siguiente

    def graficarColaUsuario(self):
        if self.head is not None:
            nodo = self.head
            while nodo.siguiente != self.head:
                self.grafica += nodo.cancion + "->"
                nodo = nodo.siguiente
            self.grafica += self.head.cancion + "}"
            print self.grafica

