class nodoUsuario:
    def __init__(self, usuario, psw):
        self.usuario = usuario
        self.contrasena = psw
        self.colaCanciones = None
        self.siguiente = None
        self.anterior = None

class listaUsuarios:
    def __init__(self):
        self.cabeza = None

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



