import colaDeUsuario
class nodoUsuario:
    def __init__(self, usuario, psw):
        self.usuario = usuario
        self.contrasena = psw
        self.colaCanciones = colaDeUsuario
        self.siguiente = None
        self.anterior = None

class listaUsuarios:
    def __init__(self):
        self.cabeza = None
        self.grafica = "digraph { "

    def insertarUsuario(self, usuario, psw):
        if self.cabeza is None:
            self.cabeza = nodoUsuario(usuario, psw)
        else:
            aux = self.cabeza
            nuevo = nodoUsuario(usuario, psw)
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo
            nuevo.anterior = aux

    def buscarUsuario(self, usuario, psw):
        aux = self.cabeza
        while aux is not None:
            if aux.usuario == usuario:
                if aux.contrasena == psw:
                    return True
                else:
                    return False
            else:
                aux = aux.siguiente
        return False

    def eliminarUsuario(self, usuario):
        aux = self.cabeza
        while aux is not None:
            if aux.usuario == usuario:
                if aux == self.cabeza:
                    self.cabeza = None
                    return True
                else:
                    prev = aux.anterior
                    next = aux.siguiente
                    if prev is not None:
                        prev.siguiente = next
                    if next is not None:
                        next.anterior = prev
                    return True
            else:
                aux = aux.siguiente
        return False

    def recorrerLista(self):
        aux = self.cabeza
        while aux is not None:
            print("Usuario: " + aux.usuario)
            aux = aux.siguiente

    def graficarListaUsuarios(self):
        if self.cabeza is not None:
            aux = self.cabeza
            while aux.siguiente is not None:
                self.grafica += aux.usuario + "->" + aux.siguiente.usuario + "[dir = both];"
                aux = aux.siguiente
            self.grafica += aux.usuario + "[dir = both]}"
        print self.grafica
        self.Creartxtusuarios()
        return self.grafica

    def Creartxtusuarios(self):
        usuariostxt = open('Usuarios.txt', 'w')
        usuariostxt.close
        self.EscribirUsuarios()

    def EscribirUsuarios(self):
        usuariostxt = open('Usuarios.txt', 'a')
        usuariostxt.write(self.grafica)
        usuariostxt.close()
        self.ImagenUsuarios()

    def ImagenUsuarios(self):
        import os
        dotPath = "C:\\Graphviz2.38\\bin\\dot.exe"
        fileInputPath = "C:\\Users\\luisg\\Desktop\\[EDD]PROYECTODIC\\Usuarios.txt"
        fileOutputPath = "C:\\Users\\luisg\\Desktop\\[EDD]PROYECTODIC\\Usuarios.jpg"
        tParam = " -Tjpg "
        tOParam = " -o "
        tuple = (dotPath + tParam + fileInputPath + tOParam + fileOutputPath)
        os.system(tuple)


