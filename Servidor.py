from click.formatting import measure_table

__author__ = "Luisgui"

from flask import Flask, request, Response
app = Flask("EDD")
import Archivo
arch = Archivo.Archivo()

@app.route('/login',methods= ['POST'])
def ingresar():
    user = str(request.form['dato'])
    pas = str(request.form['dato2'])
    ingreso = arch.listaUsuarios.buscarUsuario(user,pas)
    if(ingreso is True):
        return "INGRESADO"
    else:
        return "NO INGRESADO"
    return "NULL"

@app.route('/leer',methods= ['POST'])
def leer():
    archivo = str(request.form['dato'])
    arch.leerArchivoNodo(archivo)
    return "LEIDO"

@app.route('/GraficarMatriz',methods=['POST'])
def graficaM():
    si = str(request.form['dato'])
    arch.matriz.graficarMatriz()
    return "SE GRAFICO LA MATRIZ"

@app.route('/GraficarArbolB',methods=['POST'])
def graficab():
    anio = str(request.form['dato'])
    genero = str(request.form['dato2'])
    nodomatriz = arch.matriz.getNodoMatrizD(anio,genero)
    if nodomatriz is not None:
        nodomatriz.arbolB.getDot()
        return "SE GRAFICO EL ARBOL B"
    return "DATOS NO SON CORRECTOS"

@app.route('/GraficarABB',methods=['POST'])
def graficarabb():
    anio = str(request.form['dato'])
    genero = str(request.form['dato2'])
    artista = str(request.form['dato3'])
    nodomatriz = arch.matriz.getNodoMatrizD(anio,genero)
    if nodomatriz is not None:
        nodob = nodomatriz.arbolB.busqueda(artista)
        if nodob is not None:
            ABB = nodob.arbolABB
            if ABB is not None:
                ABB.preOrden(ABB.raiz)
                return "SE GRAFICO EL ABB"
    return "DATOS NO SON CORRECTOS"

@app.route('/GraficarListaC',methods=['POST'])
def grafiicalis():
    anio = str(request.form['dato'])
    genero = str(request.form['dato2'])
    artista = str(request.form['dato3'])
    nombre = str(request.form['dato4'])
    nodoMatriz = arch.matriz.getNodoMatrizD(anio,genero)
    if nodoMatriz is not None:
        nodoB = nodoMatriz.arbolB.busqueda(artista)
        if nodoB is not None:
            ABB = nodoB.arbolABB
            if ABB is not None:
                lista = ABB.buscarAlbum(ABB.raiz, nombre).listaCanciones
                if lista is not None:
                    lista.graficarListaCanciones()
                    return "SE GRAFICO LA LISTA DE CANCIONES"
    return "DATOS NO SON CORRECTOS"

@app.route('/graficar',methods=['POST'])
def graficarusuarios():
    si = str(request.form['dato'])
    arch.listaUsuarios.graficarListaUsuarios()
    return "SE GRAFICO LA LISTA DE USUARIOS"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')