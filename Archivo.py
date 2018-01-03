import os 
from xml.etree import ElementTree
import codecs 
class Archivo(object):
	"""docstring for Archivo"""
	def leerArchivoNodo(self,cadena):
		full_file = os.path.abspath(cadena)
		#print full_file
		with codecs.open(full_file, "r",encoding='utf-8', errors='ignore') as fdata:
			s = fdata.read().replace('\n', '')
		#print s
		
		root = ElementTree.fromstring(s)
		#print root
		usuarios = root.findall('usuarios')

		for u in usuarios:
			usr = u.findall('usuario')
			for us in usr:
				usrArchivo =us.find('nombre').text
				passArchivo =us.find('pass').text
		artistas = root.findall('artistas')
		for ar in artistas:
			art = ar.findall('artista')
			for Artista in art:
				nombreArtista_archivo = Artista.find('nombre').text
				print "nombre artista: "+ nombreArtista_archivo
				albumes = Artista.findall('albumes')
				for Albumes in albumes:
					album = Albumes.findall('album')
					for Alb in album:
						nombre_album_archivo= Alb.find('nombre').text
						genero_album_archivo=Alb.find('genero').text
						anio_album_archivo=Alb.find('anio').text
						canciones = Alb.findall('canciones')
						for Canc in canciones:
							cancion = Canc.findall('cancion')
							for Cnc in cancion:
								nombre_cancion_archivo =Cnc.find('nombre').text
								path_cancion_archivo =Cnc.find('path').text
								print "nombre cancion: " + str(nombre_cancion_archivo)
								print "path cancion: " + str(path_cancion_archivo)	

						print "nombre album: "+ str(nombre_album_archivo)
						print "genero album: "+ str(genero_album_archivo)
		

