class nodoCancion:
    def __init__(self, nombre, path):
        self.nombre = nombre
        self.path = path
        self.siguiente = None
        self.anterior = None

class listaCanciones:
    def __init__(self):
        self.primero = None
        self.grafica = "digraph {rankdir=LR;"

    def insertarCancion(self, nombre, path):
        if nombre == 'cancion con c':
            t = ""
        if self.primero is None:
            self.primero = nodoCancion(nombre, path)
            self.primero.siguiente = self.primero
            self.primero.anterior = self.primero
        else:
            aux = self.primero
            nuevo = nodoCancion(nombre, path)
            while aux.siguiente != self.primero:
                aux = aux.siguiente
            aux.siguiente = nuevo
            nuevo.anterior = aux
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo

    def eliminarCancion(self, cancion):
        aux = self.primero
        if self.primero is not None:
            while aux.siguiente != self.primero:
                if aux.nombre == cancion:
                    if aux == self.primero:
                        prev = aux.anterior
                        next = aux.siguiente
                        prev.siguiente = next
                        next.anterior = prev
                        self.primero = next
                        return True
                    else:
                        prev = aux.anterior
                        next = aux.siguiente
                        prev.siguiente = next
                        next.anterior = prev
                        return True
                else:
                    aux = aux.siguiente
            return False

    def graficarListaCanciones(self):
        if self.primero is not None:
            aux = self.primero
            while aux.siguiente != self.primero:
                self.grafica += '"' + aux.nombre + '"->"' + aux.siguiente.nombre + '"[dir = both];'
                aux = aux.siguiente
            self.grafica += '"' + aux.nombre + '"->"' + self.primero.nombre + '"[dir = both]}'
        #print self.grafica
        self.CreartxtCanciones()
        return self.grafica


    def CreartxtCanciones(self):
        cancionestxt = open('ListaCanciones.txt', 'w')
        cancionestxt.close
        self.EscribirCanciones()

    def EscribirCanciones(self):
        cancionestxt = open('ListaCanciones.txt', 'a')
        cancionestxt.write(self.grafica)
        cancionestxt.close()
        self.ImagenCanciones()

    def ImagenCanciones(self):
        import os
        dotPath = "C:\\Graphviz2.38\\bin\\dot.exe"
        fileInputPath = "C:\\Users\\luisg\\Desktop\\[EDD]PROYECTODIC\\ListaCanciones.txt"
        fileOutputPath = "C:\\Users\\luisg\\Desktop\\[EDD]PROYECTODIC\\ListaCanciones.jpg"
        tParam = " -Tjpg "
        tOParam = " -o "
        tuple = (dotPath + tParam + fileInputPath + tOParam + fileOutputPath)
        os.system(tuple)

