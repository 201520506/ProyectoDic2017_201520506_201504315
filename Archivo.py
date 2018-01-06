import os
from xml.etree import ElementTree
import codecs
from listaUsuarios import listaUsuarios
from matrizDispersa import matrizDispersa
from arbolABB import nodoAlbum
from arbolB import arbolB
from listaCanciones import listaCanciones
class Archivo(object):
    """docstring for Archivo"""
    def __init__(self):
        self.listaUsuarios = listaUsuarios()
        self.matriz = matrizDispersa()
        self.lista = listaCanciones()
    def leerArchivoNodo(self, cadena):

        full_file = os.path.abspath(cadena)
        # print full_file
        with codecs.open(full_file, "r", encoding='utf-8', errors='ignore') as fdata:
            s = fdata.read().replace('\n', '')
            # print s
        root = ElementTree.fromstring(s)
        # print root
        Cusuarios = root.findall('usuarios')
        for u in Cusuarios:
            usr = u.findall('usuario')
            for us in usr:
                self.listaUsuarios.insertarUsuario(us.find('nombre').text, us.find('pass').text)
        self.listaUsuarios.graficarListaUsuarios()
        Cartistas = root.findall('artistas')
        for ar in Cartistas:
            art = ar.findall('artista')
            for Artista in art:
                nombreArtista_archivo = Artista.find('nombre').text
                print "nombre artista: " + nombreArtista_archivo
                Calbumes = Artista.findall('albumes')
                for Albumes in Calbumes:
                    album = Albumes.findall('album')
                    for Alb in album:
                        nombre_album_archivo = Alb.find('nombre').text
                        genero_album_archivo = Alb.find('genero').text
                        anio_album_archivo = Alb.find('anio').text
                        arbolitoabb = nodoAlbum(nombre_album_archivo)
                        self.matriz.addArtista(Alb.find('anio').text,Alb.find('genero').text, nombreArtista_archivo)
                        Ccanciones = Alb.findall('canciones')
                        lista = listaCanciones()
                        for Canc in Ccanciones:
                             cancion = Canc.findall('cancion')
                             #Primero se llena la lista de canciones
                             for Cnc in cancion:
                                nombre_cancion_archivo = Cnc.find('nombre').text
                                path_cancion_archivo = Cnc.find('path').text
                                lista.insertarCancion(nombre_cancion_archivo, path_cancion_archivo)
                                print "nombre cancion: " + str(nombre_cancion_archivo)
                                print "path cancion: " + str(path_cancion_archivo)

                        arbolitoabb.listaCanciones = lista
                        self.llenarb(nombreArtista_archivo, anio_album_archivo, genero_album_archivo, arbolitoabb)

                    print "nombre album: " + str(nombre_album_archivo)
                    print "genero album: " + str(genero_album_archivo)
                    print "anio album:   " + str(anio_album_archivo)
        #gficar la matriz
        #print "MATRIZ:---------------------------------------------------------"
        self.matriz.graficarMatriz()
        #graficar el arbol B del nodo de la matriz
        #print "ARBOL B:---------------------------------------------------------"
        self.matriz.getNodoMatrizD("2012","(24)soundtrack").arbolB.getDot()
        #graficar el arbol Abb del nodo del arbol B
        #print "ARBOL ABB:---------------------------------------------------------"
        #aBB = self.matriz.getNodoMatrizD("2012","(24)soundtrack").arbolB.busqueda("brian tuey").arbolABB
        #aBB.preOrden(aBB.raiz)
        #aBB.grafica += "}"
        #print aBB.grafica
        #print "LISTA CANCIONES:---------------------------------------------------------"
        #lista = aBB.buscarAlbum(aBB.raiz, "zalbum con z").listaCanciones
        #print lista.graficarListaCanciones()




    def llenarb(self,artista,anio,genero,album):
        self.matriz.addArtista(anio,genero,artista)
        self.matriz.insertaalbum(anio,genero,album,artista)

#arch = Archivo()
#arch.leerArchivoNodo("entradaEDD2.xml")

