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
from vista import proveedor

#====================
#DEFINICION DE CLASES
#====================

#Creacion de la clase vistaLista
class ListaProveedores(QtWidgets.QWidget):
	#Inicializacion del Objeto QWidget
	def __init__(self):
		QWidget.__init__(self)

		#Importamos la vista "listaAfiliados" y la alojamos dentro de la variable "vistaLista"
		self.listaProveedores = uic.loadUi("ui/listaproveedores.ui", self)
		self.nuevo.clicked.connect(self.seleccionarProveedor)

	def seleccionarProveedor(self):
		detalle_proveedor = proveedor.Proveedor()
		detalle_proveedor.show()		