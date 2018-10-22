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
from vista import caja, listaCategorias, listaVendedores, listaVentas

#====================
#DEFINICION DE CLASES
#====================

#Creacion de la clase vistaLista
class Configuracion(QtWidgets.QWidget):
	#Inicializacion del Objeto QWidget
	def __init__(self):
		QWidget.__init__(self)

		#Importamos la vista "listaAfiliados" y la alojamos dentro de la variable "vistaLista"
		self.confi = uic.loadUi("ui/configuraciones.ui", self)
		self.caja.clicked.connect(self.seleccionarCaja)
		self.categorys.clicked.connect(self.seleccionarListaCategorias)
		self.vendedores.clicked.connect(self.seleccionarListaVendedores)
		self.ventas_del_dia.clicked.connect(self.seleccionarListaVentas)

	def seleccionarCaja(self):
		cajas = caja.Caja()
		cajas.show()		

	def seleccionarListaCategorias(self):
		lista_categorias = listaCategorias.ListaCategorias()
		lista_categorias.show()				

	def seleccionarListaVendedores(self):
		lista_vendedores = listaVendedores.ListaVendedores()
		lista_vendedores.show()			

	def seleccionarListaVentas(self):
		lista_ventas = listaVentas.ListaVentas()
		lista_ventas.show()			