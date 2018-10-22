

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
from vista import factura, listaProductos, listaProveedores, listaClientes, configuracion

#====================
#DEFINICION DE CLASES
#====================

#Creacion de la clase menuPrincipal. Objeto tipo QMainWindow
class MenuPrincipal(QMainWindow):
	#Inicializacion del Objeto MainWindow
	def __init__(self):
		QMainWindow.__init__(self)

		#Importamos la vista "menuPrincipal" y la alojamos dentro de la variable "vistaprincipal"
		vistaprincipal = uic.loadUi("ui/inicio.ui", self)
		self.stacked = vistaprincipal.findChild(QStackedWidget)
		#variables que alojan las clases que se encuentran dentro del archivo .py. (nombredelArchivo.nombredelaClase)
		fact = factura.Factura()
		listado_productos = listaProductos.ListaProductos()
		listado_proveedores = listaProveedores.ListaProveedores()
		listado_clientes = listaClientes.ListaClientes()
		configuraciones = configuracion.Configuracion()

		#Creamos una variable del tipo lista que guardara las variables anteriormente declaradas
		self.menu = [fact, listado_productos, listado_proveedores, listado_clientes, configuraciones]

		#se crea un ciclo for que indexara las variables
		for index, vista in enumerate(self.menu):
			self.stacked.insertWidget(index, vista)

		#Tomamos los eventos de los botones que se encuentran dentro del archivo .ui y llamamos a las FUNCIONES
		self.venta_rapida.clicked.connect(self.seleccionarVenta)
		self.stock.clicked.connect(self.seleccionarListaProductos)
		self.proveedores.clicked.connect(self.seleccionarListaProveedores)
		self.clientes.clicked.connect(self.seleccionarListaClientes)
		self.config.clicked.connect(self.seleccionarConfiguracion)
		self.showMaximized()

	def seleccionarVenta(self):
		self.stacked.setCurrentIndex(0)

	def seleccionarListaProductos(self):
		self.stacked.setCurrentIndex(1)	

	def seleccionarListaProveedores(self):
		self.stacked.setCurrentIndex(2)			

	def seleccionarListaClientes(self):
		self.stacked.setCurrentIndex(3)
	
	def seleccionarConfiguracion(self):
		self.stacked.setCurrentIndex(4)


#======================
#EJECUTAR LA APLICACION
#======================

#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = MenuPrincipal()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()
