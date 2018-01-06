import arbolABB

class nodoArbolB:
    def __init__(self, nombre):
        self.nombre = nombre
        self.anterior = None
        self.siguiente = None
        self.derecha = None
        self.izquierda = None
        self.arbolABB = arbolABB.arbolAlbumes()

    def getarbol(self):
       return self.arbolABB

    def getNombre(self):
        return self.nombre

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def getAnterior(self):
        return self.anterior

    def setAnterior(self, anterior):
        self.anterior = anterior

    def getDerecha(self):
        return self.derecha

    def setDerecha(self, derecha):
        self.derecha = derecha

    def getIzquierda(self):
        return self.izquierda

    def setIzquierda(self, izquierda):
        self.izquierda = izquierda


class Rama:
    def __init__(self):
        self.cuenta = 0
        self.hoja = True
        self.primero = None
        self.tempFlechas = ""

    def insertar(self, nuevo):
        if self.estaEnBlanco():
            self.primero = nuevo
            self.primero.setAnterior(None)
            self.primero.setSiguiente(None)
            self.cuenta = self.cuenta + 1
        else:
            temp = self.primero
            while True:
                if nuevo.getNombre().lower() == temp.getNombre().lower():
                    break
                elif nuevo.getNombre().lower() < temp.getNombre().lower():
                    self.cuenta = self.cuenta + 1
                    if (temp == self.primero):
                        self.primero.setAnterior(nuevo)
                        self.primero.setIzquierda(nuevo.getDerecha())
                        nuevo.setSiguiente(self.primero)
                        self.primero = nuevo
                        break
                    else:
                        nuevo.setAnterior(temp.getAnterior())
                        nuevo.setSiguiente(temp)
                        temp.getAnterior().setSiguiente(nuevo)
                        temp.getAnterior().setDerecha(nuevo.getIzquierda())
                        temp.setAnterior(nuevo)
                        temp.setIzquierda(nuevo.getDerecha())
                        break
                elif (temp.getSiguiente() == None):
                    self.cuenta = self.cuenta + 1
                    temp.setSiguiente(nuevo)
                    temp.setDerecha(nuevo.getIzquierda())
                    nuevo.setAnterior(temp)
                    nuevo.setSiguiente(None)
                    break
                temp = temp.getSiguiente()
                if not (temp != None):
                    break

    def estaEnBlanco(self):
        return self.primero == None

    def getGraphNodo(self):
        self.tempFlechas = ""
        temp = '"' + "nodo" + self.primero.getNombre() + '"'+ " [ label =\""
        tempRecorre = self.primero
        detalles = ""
        i = 0
        while i < self.cuenta:
            temp += "<C" + str(i) + ">|<D" + str(i) + \
                    ">Nombre Artista: " + tempRecorre.getNombre() + "|"
            if tempRecorre.getIzquierda() != None:
                self.tempFlechas += "nodo" + self.primero.getNombre() + ":C" + str(i) + "->nodo" + \
                                    tempRecorre.getIzquierda().primero.getNombre() + "\n"
            tempRecorre = tempRecorre.getSiguiente()
            i = i + 1
        temp += "<C" + str(i) + ">\" fillcolor=\"#CCCCCC\"]\n"
        tempRecorre = self.primero
        while tempRecorre.getSiguiente() != None:
            tempRecorre = tempRecorre.getSiguiente()
        if tempRecorre.getDerecha() != None:
            self.tempFlechas += "nodo" + self.primero.getNombre() + ":C" + str(i) + "->nodo" + \
                                tempRecorre.getDerecha().primero.getNombre() + "\n"
        temp += self.tempFlechas
        temp += detalles
        return temp

    def esHoja(self):
        return self.hoja

    def setHoja(self, hoja):
        self.hoja = hoja

    def getCuenta(self):
        return self.cuenta

    def getPrimero(self):
        return self.primero


class arbolB:
    def __init__(self):
        self.raiz = None
        self.nodos = ""
        self.graficab = ""

    def estaVacio(self):
        return self.raiz == None

    def insertar(self, nombre):
        nodo = nodoArbolB(nombre)
        if self.estaVacio():
            self.raiz = Rama()
            self.raiz.insertar(nodo)
        else:
            obj = self.inserta(nodo, self.raiz)
            if isinstance(obj, nodoArbolB):
                self.raiz = Rama()
                self.raiz.insertar(obj)
                self.raiz.setHoja(False)

    def inserta(self, nodo, rama):
        if rama.esHoja():
            rama.insertar(nodo)
            if rama.getCuenta() == 5:
                return self.dividir(rama)
            else:
                return rama
        else:
            temp = rama.getPrimero()
            while True:
                if nodo.getNombre().lower() == temp.getNombre().lower():
                    return rama
                elif nodo.getNombre().lower() < temp.getNombre().lower():
                    obj = self.inserta(nodo, temp.getIzquierda())
                    if isinstance(obj, nodoArbolB):
                        rama.insertar(obj)
                        if (rama.getCuenta() == 5):
                            return self.dividir(rama)
                    return rama
                elif temp.getSiguiente() == None:
                    obj = self.inserta(nodo, temp.getDerecha())
                    if isinstance(obj, nodoArbolB):
                        rama.insertar(obj)
                        if (rama.getCuenta() == 5):
                            return self.dividir(rama)
                    return rama
                temp = temp.getSiguiente()
                if not (temp != None):
                    break
        return rama

    def dividir(self, rama):
        derecha = Rama()
        izquierda = Rama()
        medio = None
        temp = rama.getPrimero()
        i = 1
        while i < 6:
            nodo = nodoArbolB(temp.getNombre())
            nodo.setIzquierda(temp.getIzquierda())
            nodo.setDerecha(temp.getDerecha())
            if (nodo.getDerecha() != None and nodo.getIzquierda() != None):
                izquierda.setHoja(False)
                derecha.setHoja(False)
            if i == 1 or i == 2:
                izquierda.insertar(nodo)
            elif i == 3:
                medio = nodo
            elif i == 4 or i == 5:
                derecha.insertar(nodo)
            temp = temp.getSiguiente()
            i = i + 1
        medio.setIzquierda(izquierda)
        medio.setDerecha(derecha)
        return medio

    def getDot(self):
        aux = "digraph lista{ \nnode [shape = record, style=filled];"
        aux += "splines=line; \n"
        self.getGrafNodos(self.raiz)
        aux += self.nodos
        aux += "}"
        print aux
        self.graficab = aux
        self.CreartxtArbolB()
        #return aux

    def CreartxtArbolB(self):
        arbolbtxt = open('ArbolB.txt', 'w')
        arbolbtxt.close
        self.EscribirArbolB()

    def EscribirArbolB(self):
        matriztxt = open('ArbolB.txt', 'a')
        matriztxt.write(self.graficab)
        matriztxt.close()
        self.ImagenB()

    def ImagenB(self):
        import os
        dotPath = "C:\\Graphviz2.38\\bin\\dot.exe"
        fileInputPath = "C:\\Users\\luisg\\Desktop\\[EDD]PROYECTODIC\\ArbolB.txt"
        fileOutputPath = "C:\\Users\\luisg\\Desktop\\[EDD]PROYECTODIC\\ArbolB.jpg"
        tParam = " -Tjpg "
        tOParam = " -o "
        tuple = (dotPath + tParam + fileInputPath + tOParam + fileOutputPath)
        os.system(tuple)

    def getGrafNodos(self, raiz):
        if raiz == None:
            return
        self.nodos += raiz.getGraphNodo()
        aux = raiz.getPrimero()
        while aux != None:
            self.getGrafNodos(aux.getIzquierda())
            aux = aux.getSiguiente()
        aux = raiz.getPrimero()
        while aux.getSiguiente() != None:
            aux = aux.getSiguiente()
        self.getGrafNodos(aux.getDerecha())

    def busqueda(self, nombre):
        if not (self.estaVacio()):
            return self.buscarNodo(nombre, self.raiz)
        else:
            return None

    def buscarArtista(self,album,artista):
        if not (self.estaVacio()):
            return self.busca(artista, self.raiz, album)
        else:
            return False

    def busca(self, artista, rama, album):
        nodo = rama.getPrimero()
        while nodo != None:
            if artista.lower() < nodo.getNombre().lower():
                if rama.esHoja():
                    return False
                else:
                    return self.busca(artista, nodo.getIzquierda(), album)
            elif artista.lower() == nodo.getNombre().lower():
                nodo.arbolABB.crearNodo(album)
            elif nodo.getSiguiente() == None:
                if rama.esHoja():
                    return False
                else:
                    return self.busca(artista, nodo.getDerecha(), album)
            nodo = nodo.getSiguiente()
        return False

    def buscarNodo(self, nombre, rama):
        nodo = rama.getPrimero()
        while nodo != None:
            if nombre.lower() < nodo.getNombre().lower():
                if rama.esHoja():
                    return None
                else:
                    return self.busca(nombre, nodo.getIzquierda())
            elif nombre.lower() == nodo.getNombre().lower():
                return nodo
            elif nodo.getSiguiente() == None:
                if rama.esHoja():
                    return None
                else:
                    return self.busca(nombre, nodo.getDerecha())
            nodo = nodo.getSiguiente()
        return None

    def escribir(self):
        archivo = open("arbolb.txt", 'a')
        archivo.write(self.getDot())
        archivo.close()

    def crearTxt(self):
        archivo = open("arbolb.txt", 'w')
        archivo.close()
        self.escribir()



