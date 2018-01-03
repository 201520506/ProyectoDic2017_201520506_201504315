__author__ = "Luisgui"

from flask import Flask, request, Response
app = Flask("EDD")
import  listaUsuarios
import Archivo

lista = listaUsuarios.listaUsuarios()
arch = Archivo.Archivo()


@app.route('/insertarLista',methods=['POST'])
def registrar():
    user = str(request.form['dato'])
    pas = str(request.form['dato2'])
    lista.insertarUsuario(user,pas)
    return "REGISTRADO"

@app.route('/login',methods= ['POST'])
def ingresar():
    user = str(request.form['dato'])
    pas = str(request.form['dato2'])
    ingreso = lista.buscarUsuario(user,pas)
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

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')