#=============
#IMPORTACIONES
#=============

# Importamos el módulo sys que provee el acceso a funciones y objetos mantenidos por el intérprete.
import sys
# Importamos las herramientas de PyQT que vamos a utilizar
from PyQt5 import QtWidgets, uic, QtGui
# Importamos los elementos que se encuentran dentro del diseñador
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QStackedWidget, QTableWidgetItem, QTableWidget
# Importamos el modulo uic necesario para levantar un archivo .ui
from PyQt5 import uic
from vista import categorias
import mysql.connector

#====================
#DEFINICION DE CLASES
#====================

#Creacion de la clase vistaLista
class ListaCategorias(QtWidgets.QWidget):
	#Inicializacion del Objeto QWidget
	def __init__(self):
		QWidget.__init__(self)
		
		#Importamos la vista "listaAfiliados" y la alojamos dentro de la variable "vistaLista"
		self.listaCategorias = uic.loadUi("ui/listacategorias.ui", self)
		self.nuevo.clicked.connect(self.seleccionarCategorias)
		conexion = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="tpv")
		cursor = conexion.cursor()
		listacategorias = "SELECT * FROM categorias"	
		cursor.execute(listacategorias)
		lista = cursor.fetchall()
		for row in lista:
			id_cat = row[0]
			nom_cat = row[1]
			numRows = self.tableWidget.rowCount()
			self.tableWidget.insertRow(numRows)
			self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(id_cat))
			self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(nom_cat))

	def seleccionarCategorias(self):
		detalle_categorias = categorias.Categorias()
		detalle_categorias.show()

