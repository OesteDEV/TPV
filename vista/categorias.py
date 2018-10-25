#=============
#IMPORTACIONES
#=============

# Importamos el módulo sys que provee el acceso a funciones y objetos mantenidos por el intérprete.
import sys
# Importamos las herramientas de PyQT que vamos a utilizar
from PyQt5 import QtWidgets, uic, QtGui
# Importamos los elementos que se encuentran dentro del diseñador
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QStackedWidget, QMessageBox
# Importamos el modulo uic necesario para levantar un archivo .ui
from PyQt5 import uic
import mysql.connector


#====================
#DEFINICION DE CLASES
#====================

#Creacion de la clase vistaLista
class Categorias(QtWidgets.QWidget):
	#Inicializacion del Objeto QWidget
	def __init__(self):
		QWidget.__init__(self)

		#Importamos la vista "listaAfiliados" y la alojamos dentro de la variable "vistaLista"
		self.category = uic.loadUi("ui/categorias.ui", self)		
		self.guardar.clicked.connect(self.Insertar)

	def Insertar(self):
		conexion = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="tpv")
		cursor = conexion.cursor()
		idcateg = self.id_categoria.text()
		nombrecateg = self.nombre_categoria.text()			
		sql = "INSERT INTO categorias (id_categoria, nombre_categoria) VALUES (%s, %s)"
		val=(idcateg, nombrecateg)
		cursor.execute(sql, val)
		conexion.commit()
		conexion.close()
		self.close()

	def actualizar(self):
		conexion = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="tpv")
		cursor = conexion.cursor()
		idcateg = self.id_categoria.text()
		nombrecateg = self.nombre_categoria.text()			
		sql = "INSERT INTO categorias (id_categoria, nombre_categoria) VALUES (%s, %s)"
		val=(idcateg, nombrecateg)
		cursor.execute(sql, val)
		conexion.commit()
		conexion.close()
		self.close()


	def verDetalle(self):
		detalle_categorias = categorias.Categorias()
		detalle_categorias.show()
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			tmp_id_cat = currentQTableWidgetItem.row()
			tmp_nom_cat = currentQTableWidgetItem.text()
			detalle_categorias.id_categoria.setText(str(tmp_id_cat))
			detalle_categorias.id_categoria.setEnabled(False)
			nombre_cat = detalle_categorias.nombre_categoria.setText(tmp_nom_cat)
			detalle_categorias.guardar.setEnabled(False)