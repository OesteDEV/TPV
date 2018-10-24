import mysql.connector

def Conexion():
		conexion = mysql.connector.connect(host="localhost", 
											user="root", 
											passwd="admin", 
											database="tpv")