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
import mysql.connector


#====================
#DEFINICION DE CLASES
#====================

#Creacion de la clase vistaLista
class Vendedores(QtWidgets.QWidget):
	#Inicializacion del Objeto QWidget
	def __init__(self):
		QWidget.__init__(self)

		#Importamos la vista "listaAfiliados" y la alojamos dentro de la variable "vistaLista"
		self.venden = uic.loadUi("ui/vendedores.ui", self)
		self.guardar.clicked.connect(self.Insertar)
		
		conexion = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="tpv")
		cursor = conexion.cursor()
		last_id = "SELECT * FROM vendedores ORDER BY id_vendedor DESC LIMIT 1"	
		cursor.execute(last_id)
		codigo = cursor.fetchone()
		for row in codigo:
			cod = codigo[0] + 1
			self.id_vendedor.setText(str(cod))

	def Insertar(self):
		conexion = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="tpv")
		cursor = conexion.cursor()
		idvend = self.id_vendedor.text()
		nombrevend = self.nombre_vendedor.text()
		contravend = self.contrasenia_vendedor.text()			
		sql = "INSERT INTO vendedores (id_vendedor, nombre_vendedor, contrasenia_vendedor) VALUES (%s, %s, %s)"
		val=(idvend, nombrevend, contravend)
		cursor.execute(sql, val)
		conexion.commit()
		conexion.close()
		self.close()		