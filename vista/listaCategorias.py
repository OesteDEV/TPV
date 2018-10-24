#=============
#IMPORTACIONES
#=============

# Importamos el módulo sys que provee el acceso a funciones y objetos mantenidos por el intérprete.
import sys
# Importamos las herramientas de PyQT que vamos a utilizar
from PyQt5 import QtWidgets, uic, QtGui
# Importamos los elementos que se encuentran dentro del diseñador
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QStackedWidget, QTableWidgetItem, QTableWidget, QAbstractItemView, QHeaderView, QMenu, QActionGroup, QAction)
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
		#boton nuevo llama a la funcion seleccionar categoria
		self.nuevo.clicked.connect(self.seleccionarCategorias)
		self.eliminar.clicked.connect(self.eliminarFila)
		#variable de conexion a mysql
		conexion = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="tpv")
		#creacion del cursor
		cursor = conexion.cursor()
		#guardar en una variable la consulta SQL
		listacategorias = "SELECT * FROM categorias"
		#Ejecutar la consulta	
		cursor.execute(listacategorias)
		#guardar en una variable todos los elementos de la consulta
		lista = cursor.fetchall()
		#crear un ciclo for para recorrer todos los elementos de la lista
		for row in lista:
			id_cat = row[0]
			nom_cat = row[1]
			numRows = self.tableWidget.rowCount()
			self.tableWidget.insertRow(numRows)
			#insertar los datos en el TableWidget
			self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(id_cat))
			self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(nom_cat))
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
		#Ver detalle del afiliado al hacer doble click
		category = self.tableWidget.itemDoubleClicked.connect(self.verDetalle)


	def verDetalle(self):
		detalle_categorias = categorias.Categorias()
		detalle_categorias.show()
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			tmp_id_cat = currentQTableWidgetItem.column()
			tmp_nom_cat = currentQTableWidgetItem.text()

	def seleccionarCategorias(self):
		detalle_categorias = categorias.Categorias()
		detalle_categorias.show()

	def eliminarFila(self):
		filaSeleccionada = self.tableWidget.selectedItems()
		if filaSeleccionada:
			fila = filaSeleccionada[0].row()
			self.tableWidget.removeRow(fila)
			self.tableWidget.clearSelection()
		else:
			QMessageBox.critical(self, "Eliminar fila", "Seleccione una fila.   ",
                                 QMessageBox.Ok)