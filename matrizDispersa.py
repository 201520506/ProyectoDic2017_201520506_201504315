import arbolB
class nodoEncabezado:
    def __init__(self, anio, gen):
        self.Anio = anio
        self.Genero = gen
        self.siguiente = None
        self.anterior = None
        self.primero = None


class nodoDato:
    def __init__(self, anio, genero):
        self.izquierda = None
        self.derecha = None
        self.arriba = None
        self.abajo = None
        self.Anio = anio
        self.Genero = genero
        self.arbolB = arbolB.arbolB()


class matrizDispersa:
    def __init__(self):
        self.pGenero = None
        self.pAnio = None
        self.grafica = 'digraph g{ rankdir = TB; node [shape = rectangle]; graph [nodesep = 0.5];'

    # EN CASO DE QUE NO EXISTA EL NODO DEL GENERO Y ANO CORRESPONDIENTE
    # LO INSERTARA PARA DESPUES AGREGAR ALBUM CON CANCIONES

    def insertar(self, anio, genero):
        nuevo = nodoDato(anio, genero)
        if self.pAnio is None:
            self.pAnio = nodoEncabezado(anio, "")
            self.pGenero = nodoEncabezado("", genero)
            self.pAnio.primero = nuevo
            nuevo.arriba = self.pAnio
            self.pGenero.primero = nuevo
            nuevo.izquierda = self.pGenero
        else:
            cabezaGenero = self.pGenero
            while cabezaGenero is not None:
                if cabezaGenero.Genero != genero:
                    if cabezaGenero.Genero < genero:
                        if cabezaGenero.siguiente is None:
                            # crea encabezado nuevo al final de las filas existentes
                            aux = nodoEncabezado("", genero)
                            aux.anterior = cabezaGenero
                            cabezaGenero.siguiente = aux
                            aux.primero = nuevo
                            nuevo.izquierda = aux
                            cabezaGenero = None
                        else:
                            cabezaGenero = cabezaGenero.siguiente
                    elif cabezaGenero.Genero > genero:
                        # crea encabezado nuevo en medio de dos existentes
                        if cabezaGenero == self.pGenero:
                            aux = nodoEncabezado(0, genero)
                            self.pGenero.anterior = aux
                            aux.siguiente = self.pGenero
                            aux.primero = nuevo
                            nuevo.izquierda = aux
                            self.pGenero = aux
                            cabezaGenero = None
                        else:
                            aux = nodoEncabezado("", genero)
                            nodoAnterior = cabezaGenero.anterior
                            nodoAnterior.siguiente = aux
                            aux.anterior = nodoAnterior
                            aux.siguiente = cabezaGenero
                            cabezaGenero.anterior = aux
                            nuevo.izquierda = aux
                            aux.primero = nuevo
                            cabezaGenero = None
                else:
                    bandera = True
                    nodo = cabezaGenero.primero
                    while bandera:
                        columna = nodo
                        if columna.Anio < anio:
                            if nodo.derecha is None:
                                nodo.derecha = nuevo
                                nuevo.izquierda = nodo
                                cabezaGenero = None
                                bandera = False
                            else:
                                nodo = nodo.derecha
                        elif columna.Anio > anio:
                            if nodo == cabezaGenero.primero:
                                cabezaGenero.primero.izquierda = nuevo
                                nuevo.derecha = cabezaGenero.primero
                                nuevo.izquierda = cabezaGenero
                                cabezaGenero.primero = nuevo
                                cabezaGenero = None
                                bandera = False
                            else:
                                prev = nodo.izquierda
                                prev.derecha = nuevo
                                nuevo.izquierda = prev
                                nuevo.derecha = nodo
                                nodo.izquierda = nuevo
                                cabezaGenero = None
                                bandera = False
            # BUSCA COLUMNA A LA QUE PERTENECE EL NUEVO NODO
            cabezaCol = self.pAnio
            while cabezaCol is not None:
                if cabezaCol.Anio != anio:
                    if cabezaCol.Anio < anio:
                        if cabezaCol.siguiente is None:
                            # crea encabezado nuevo al final de las filas existentes
                            aux = nodoEncabezado(anio, "")
                            aux.anterior = cabezaCol
                            cabezaCol.siguiente = aux
                            aux.primero = nuevo
                            nuevo.arriba = aux
                            cabezaCol = aux.siguiente
                        else:
                            cabezaCol = cabezaCol.siguiente
                    elif cabezaCol.Anio > anio:
                        # crea encabezado nuevo en medio de dos existentes
                        if cabezaCol == self.pAnio:
                            aux = nodoEncabezado(anio, "")
                            self.pAnio.anterior = aux
                            aux.siguiente = self.pAnio
                            aux.primero = nuevo
                            nuevo.arriba = aux
                            self.pAnio = aux
                            cabezaCol = None
                        else:
                            aux = nodoEncabezado(anio, "")
                            nodoAnterior = cabezaCol.anterior
                            nodoAnterior.siguiente = aux
                            aux.anterior = nodoAnterior
                            aux.siguiente = cabezaCol
                            cabezaCol.anterior = aux
                            nuevo.arriba = aux
                            aux.primero = nuevo
                            cabezaCol = None
                else:
                    # LA COLUMNA ES IGUAL A UNA YA EXISTENTE
                    nodo = cabezaCol.primero
                    bandera = True
                    while bandera:
                        row = nodo
                        if row.Genero < genero:
                            if nodo.abajo is None:
                                nodo.abajo = nuevo
                                nuevo.arriba = nodo
                                cabezaCol = None
                                bandera = False
                            else:
                                nodo = nodo.abajo
                        elif row.Genero > genero:
                            if nodo == cabezaCol.primero:
                                nodo.arriba = nuevo
                                nuevo.abajo = nodo
                                nuevo.arriba = cabezaCol
                                cabezaCol.primero = nuevo
                                cabezaCol = None
                                bandera = False
                            else:
                                prev = nodo.arriba
                                prev.abajo = nuevo
                                nuevo.arriba = prev
                                nuevo.abajo = nodo
                                nodo.arriba = nuevo
                                cabezaCol = None
                                bandera = False

    # BUSCA EL NODO CORRESPONDIENTE AL GENERO Y ANO DEL ALBUM DEL ARTISTA A INSERTAR
    # SI NO LO ENCUENTRA SE DEBE INSERTAR ANTES EL NODO Y VOLVER A ESTE METODO

    def validarArtista(self, anio, genero, artista):
        nodoAnio = self.pAnio
        flag = True
        if nodoAnio is None:
            return False
        else:
            while flag is True:
                if nodoAnio.Anio != anio:
                    if nodoAnio.Anio < anio:
                        if nodoAnio.siguiente is None:
                            return False
                        else:
                            nodoAnio = nodoAnio.siguiente
                    elif nodoAnio.Anio > anio:
                        return False
                else:
                    # Encontro el ano a buscar
                    nodoGen = nodoAnio.primero
                    bandera = True
                    while bandera is True:
                        if nodoGen.Genero != genero:
                            if nodoGen.Genero < genero:
                                if nodoGen.abajo is None:
                                    return False
                                else:
                                    nodoGen = nodoGen.abajo
                            elif nodoGen.Genero > genero:
                                return False
                        else:
                            # SE DEBE INSERTAR EL ARTISTA AL ARBOL B DEL NODO DE LA MATRIZ QUE SE ENCONTRO
                            nodoGen.arbolB.insertar(artista)
                            return True
    def getNodoMatrizD(self, anio, genero):
        nodoAnio = self.pAnio
        flag = True
        if nodoAnio is None:
            return None
        else:
            while flag is True:
                if nodoAnio.Anio != anio:
                    if nodoAnio.Anio < anio:
                        if nodoAnio.siguiente is None:
                            return None
                        else:
                            nodoAnio = nodoAnio.siguiente
                    elif nodoAnio.Anio > anio:
                        return None
                else:
                    # Encontro el ano a buscar
                    nodoGen = nodoAnio.primero
                    bandera = True
                    while bandera is True:
                        if nodoGen.Genero != genero:
                            if nodoGen.Genero < genero:
                                if nodoGen.abajo is None:
                                    return None
                                else:
                                    nodoGen = nodoGen.abajo
                            elif nodoGen.Genero > genero:
                                return None
                        else:
                            # SE DEBE INSERTAR EL ARTISTA AL ARBOL B DEL NODO DE LA MATRIZ QUE SE ENCONTRO
                            return nodoGen

    def addArtista(self, anio, genero, artista):
        if(self.validarArtista(anio,genero,artista) == False):
            self.insertar(anio, genero)
            self.addArtista(anio, genero, artista)

    def graficarMatriz(self):

        genero = self.pGenero
        anio = self.pAnio
        texto = self.grafica
        txt = ""
        if genero is not None:
            if genero.siguiente is not None:
                while genero.siguiente is not None:
                    txt = '{rank = same; "' + str(genero.Genero) + '" '
                    texto = texto + '"' + str(genero.Genero) + '"->"' + str(
                        genero.siguiente.Genero) + '" [dir=both];'
                    nodo = genero.primero
                    texto = texto + '"' + str(genero.Genero) + '"->"' + str(nodo.Anio) + str(nodo.Genero)  +'" [dir = both];'
                    txt = txt + '"'  + str(nodo.Anio) + str(nodo.Genero) + '" '
                    if nodo.derecha is not None:
                        while nodo.derecha is not None:
                            texto = texto + '"' + str(nodo.Anio) + str(nodo.Genero) + '"->"' + \
                                    str(nodo.derecha.Anio) + str(nodo.derecha.Genero) + '" [dir = both];'
                            txt = txt + '"' + str(nodo.derecha.Anio) + str(nodo.derecha.Genero) + '" '
                            nodo = nodo.derecha
                        txt = txt + "}"
                        texto += txt
                        genero = genero.siguiente
                    else:
                        texto = texto + txt + "}"
                        genero = genero.siguiente
                txt = '{rank = same; "' + str(genero.Genero) + '" '
                nodo = genero.primero
                texto = texto + '"' + str(genero.Genero) + '"->"' + str(nodo.Anio) + str(nodo.Genero) + '" [dir = both];'
                txt = txt + '"' + str(nodo.Anio) + str(nodo.Genero) + '" '
                if nodo.derecha is not None:
                    while nodo.derecha is not None:
                        texto = texto + '"' + str(nodo.Anio) + str(nodo.Genero) + '"->"' \
                                + str(nodo.derecha.Anio) + str(nodo.derecha.Genero) + '" [dir = both];'
                        txt = txt + '"' + str(nodo.derecha.Anio) + str(nodo.derecha.Genero) + '" '
                        nodo = nodo.derecha
                    txt = txt + "}"
                    texto = texto + txt
                else:
                    texto = texto + txt + "}"
        txt = "{rank = same; "
        if anio is not None:
            txt = txt + '"' + str(anio.Anio) + '" '
            if anio.siguiente is not None:
                while anio.siguiente is not None:
                    texto = texto + '"' + str(anio.Anio) + '"->"' + str(anio.siguiente.Anio) + '" [dir=both];'
                    nodo = anio.primero
                    texto = texto + '"' + str(anio.Anio) + '"->"' + str(nodo.Anio) + str(nodo.Genero) + '" [dir = both];'
                    txt = txt + '"' + str(anio.siguiente.Anio) + '" '
                    if nodo.abajo is not None:
                        while nodo.abajo is not None:
                            texto = texto + '"' + str(nodo.Anio) + str(nodo.Genero) + '"->"' \
                                    + str(nodo.abajo.Anio) + str(nodo.abajo.Genero) + '" [dir = both];'
                            nodo = nodo.abajo
                        anio = anio.siguiente
                    else:
                        texto = texto + txt + "}"
                        anio = anio.siguiente
                nodo = anio.primero
                texto = texto + '"' + str(anio.Anio) + '"->"' + str(nodo.Anio) + str(nodo.Genero) + '" [dir = both];'
                if nodo.abajo is not None:
                    while nodo.abajo is not None:
                        texto = texto + '"' + str(nodo.Anio) + str(nodo.Genero) + '"->"' \
                                + str(nodo.abajo.Anio) + str(nodo.abajo.Genero) + '" [dir = both];'
                        nodo = nodo.abajo
                else:
                    texto = texto + txt + "}"
        texto = texto + txt + "}}"
        print texto
        self.grafica = texto
        self.CreartxtMatriz()

    def CreartxtMatriz(self):
        matriztxt = open('MatrizDispersa.txt', 'w')
        matriztxt.close
        self.EscribirMatriz()

    def EscribirMatriz(self):
        matriztxt = open('MatrizDispersa.txt', 'a')
        matriztxt.write(self.grafica)
        matriztxt.close()
        self.ImagenMatriz()

    def ImagenMatriz(self):
        import os
        dotPath = "C:\\Graphviz2.38\\bin\\dot.exe"
        fileInputPath = "C:\\Users\\luisg\\Desktop\\[EDD]PROYECTODIC\\MatrizDispersa.txt"
        fileOutputPath = "C:\\Users\\luisg\\Desktop\\[EDD]PROYECTODIC\\MatrizDispersa.jpg"
        tParam = " -Tjpg "
        tOParam = " -o "
        tuple = (dotPath + tParam + fileInputPath + tOParam + fileOutputPath)
        os.system(tuple)



    def insertaalbum(self,anio,genero,album,artista):
        nodoAnio = self.pAnio
        flag = True
        if nodoAnio is None:
            return False
        else:
            while flag is True:
                if nodoAnio.Anio != anio:
                    if nodoAnio.Anio < anio:
                        if nodoAnio.siguiente is None:
                            return False
                        else:
                            nodoAnio = nodoAnio.siguiente
                    elif nodoAnio.Anio > anio:
                        return False
                else:
                    # Encontro el ano a buscar
                    nodoGen = nodoAnio.primero
                    bandera = True
                    while bandera is True:
                        if nodoGen.Genero != genero:
                            if nodoGen.Genero < genero:
                                if nodoGen.abajo is None:
                                    return False
                                else:
                                    nodoGen = nodoGen.abajo
                            elif nodoGen.Genero > genero:
                                return False
                        else:
                            nodoGen.arbolB.buscarArtista(album,artista)
                            return True

