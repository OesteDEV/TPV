#=============
#IMPORTACIONES
#=============

# Importamos el módulo sys que provee el acceso a funciones y objetos mantenidos por el intérprete.
import sys
# Importamos las herramientas de PyQT que vamos a utilizar
from PyQt5 import QtWidgets, uic, QtGui
# Importamos los elementos que se encuentran dentro del diseñador
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QStackedWidget, QMessageBox, QTableWidgetItem, QTableWidget, QAbstractItemView, QHeaderView, QMenu, QActionGroup, QAction)
# Importamos el modulo uic necesario para levantar un archivo .ui
from PyQt5 import uic
from vista import vendedores
import mysql.connector

#====================
#DEFINICION DE CLASES
#====================

#Creacion de la clase vistaLista
class ListaVendedores(QtWidgets.QWidget):
	#Inicializacion del Objeto QWidget
	def __init__(self):
		QWidget.__init__(self)

		#Importamos la vista "listaAfiliados" y la alojamos dentro de la variable "vistaLista"
		self.listaVendedores = uic.loadUi("ui/listavendedores.ui", self)
		self.nuevo.clicked.connect(self.seleccionarVendedores)
		self.eliminar.clicked.connect(self.eliminarFila)
		#variable de conexion a mysql
		conexion = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="tpv")
		#creacion del cursor
		cursor = conexion.cursor()
		#guardar en una variable la consulta SQL
		listavendedores = "SELECT * FROM vendedores"
		#Ejecutar la consulta	
		cursor.execute(listavendedores)
		#guardar en una variable todos los elementos de la consulta
		lista = cursor.fetchall()
		#crear un ciclo for para recorrer todos los elementos de la lista
		for row in lista:
			id_ven = row[0]
			nom_ven = row[1]
			numRows = self.tableWidget.rowCount()
			self.tableWidget.insertRow(numRows)
			#insertar los datos en el TableWidget
			self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(id_ven))
			self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(nom_ven))
			print(id_ven, nom_ven)
			#Hacer que la ultima columna ocupe todo el espacio
			self.tableWidget.horizontalHeader().setStretchLastSection(True)
			#ponerle nombre a los encabezados de las columnas
			nombreColumnas = ("Id","Nombre")
			self.tableWidget.setHorizontalHeaderLabels(nombreColumnas)
			#hacer que las filas no sean editables
			self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
			# Dibujar el fondo usando colores alternados
			self.tableWidget.setAlternatingRowColors(True)
			# Seleccionar toda la fila
			self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)	

	def seleccionarVendedores(self):
		detalle_vendedores = vendedores.Vendedores()
		detalle_vendedores.show()

	def eliminarFila(self):
		filaSeleccionada = self.tableWidget.selectedItems()
		print(filaSeleccionada)
		if filaSeleccionada:
			fila = filaSeleccionada[0].row()
			self.tableWidget.removeRow(fila)
			self.tableWidget.clearSelection()
		else:
			QMessageBox.critical(self, "Eliminar fila", "Seleccione una fila.   ",
                                 QMessageBox.Ok)		