#=============
#IMPORTACIONES
#=============

# Importamos el módulo sys que provee el acceso a funciones y objetos mantenidos por el intérprete.
import sys
# Importamos las herramientas de PyQT que vamos a utilizar
from PyQt5 import QtWidgets, uic, QtGui
# Importamos los elementos que se encuentran dentro del diseñador
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QStackedWidget
# Importamos el modulo uic necesario para levantar un archivo .ui
from PyQt5 import uic		
from vista import listaProductos, listaClientes


#====================
#DEFINICION DE CLASES
#====================

#Creacion de la clase vistaLista
class Factura(QtWidgets.QWidget):
	#Inicializacion del Objeto QWidget
	def __init__(self):
		QWidget.__init__(self)

		#Importamos la vista "listaAfiliados" y la alojamos dentro de la variable "vistaLista"
		self.factura = uic.loadUi("ui/factura.ui", self)
		self.buscar.clicked.connect(self.buscarProductos)
		self.buscar_cliente.clicked.connect(self.buscarClientes)

	def buscarProductos(self):
		lista_productos = listaProductos.ListaProductos()
		lista_productos.show()
	
	def buscarClientes(self):
		lista_clientes = listaClientes.ListaClientes()
		lista_clientes.show()
