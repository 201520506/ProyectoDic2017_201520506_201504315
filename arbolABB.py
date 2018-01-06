import listaCanciones
class nodoAlbum:
    def __init__(self, album):
        self.album = album
        self.listaCanciones = listaCanciones
        self.izquierda = None
        self.derecha = None

class arbolAlbumes:
    def __init__(self):
        self.raiz = None
        self.grafica = "digraph g {"

    def crearNodo(self, album):
        aux = album
        if self.raiz is None:
            #print "Se creo la raiz: " + str(aux.album)
            self.raiz = aux
        else:
            "Enviando a insertar usuario, self.raiz: " + str(self.raiz.album) + ", aux: " + str(aux.album)
            self.insertarAlbum(self.raiz, aux)

    def insertarAlbum(self, raiz, nuevo):
        bandera = 0
        while bandera == 0:
            album1 = raiz.album
            album2 = nuevo.album
            if album1 > album2:
                if raiz.izquierda is None:
                    #print str(raiz.album) + ".izquierda = " + str(nuevo.album)
                    raiz.izquierda = nuevo
                else:
                    raiz.izquierda = self.insertarAlbum(raiz.izquierda, nuevo)
                bandera = -1
            elif album2 > album1:
                if raiz.derecha is None:
                    #print str(raiz.album) + ".derecha = " + str(nuevo.album)
                    raiz.derecha = nuevo
                else:
                    raiz.derecha = self.insertarAlbum(raiz.derecha, nuevo)
                bandera = -1
            elif album1 == album2:
                print "Album ya existente"
            return raiz

    def preOrden(self, raiz):
        if raiz is not None:
            if raiz.izquierda is None and raiz.derecha is None:
                self.grafica += '"' + str(self.raiz.album) + '"'
            if raiz.izquierda is not None:
                self.grafica = self.grafica + '"' + str(raiz.album) + '"->"' + str(raiz.izquierda.album) + '"'
            if raiz.derecha is not None:
                self.grafica = self.grafica + '"' + str(raiz.album) + '"->"' + str(raiz.derecha.album) + '"'
            self.preOrden(raiz.izquierda)
            self.preOrden(raiz.derecha)
        self.CreartxtArbolABB()

    def CreartxtArbolABB(self):
        ABBtxt = open('ArbolABB.txt', 'w')
        ABBtxt.close
        self.EscribirArbolABB()

    def EscribirArbolABB(self):
        ABBtxt = open('ArbolABB.txt', 'a')
        ABBtxt.write(self.grafica)
        ABBtxt.write("}")
        ABBtxt.close()
        self.ImagenABB()

    def ImagenABB(self):
        import os
        dotPath = "C:\\Graphviz2.38\\bin\\dot.exe"
        fileInputPath = "C:\\Users\\luisg\\Desktop\\[EDD]PROYECTODIC\\ArbolABB.txt"
        fileOutputPath = "C:\\Users\\luisg\\Desktop\\[EDD]PROYECTODIC\\ArbolABB.jpg"
        tParam = " -Tjpg "
        tOParam = " -o "
        tuple = (dotPath + tParam + fileInputPath + tOParam + fileOutputPath)
        os.system(tuple)

    def buscarAlbum(self, raiz, album):
        if raiz is not None:
            if raiz.album == album:
                #print "True"
                return raiz
            if raiz.izquierda is not None:
                if raiz.izquierda.album == album:
                    #print "True"
                    return raiz.izquierda
            if raiz.derecha is not None:
                if raiz.derecha.album == album:
                    #print "True"
                    return raiz.derecha
            self.buscarAlbum(raiz.izquierda, album)
            self.buscarAlbum(raiz.derecha, album)
        return None
