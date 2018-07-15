# -*- coding: utf-8 -*-
import numpy as np
import pymysql.cursors
from scipy import linalg
#Definiendo patrones para enfermedades.

#Cada síntoma corresponde a una letra
diccionarioSintomas = {'a': 'Sintoma1', 'b': 'Sintoma2','c': 'Sintoma3','d': 'Sintoma4',
'e': 'Sintoma5','f': 'Sintoma6','g': 'Sintoma7','h': 'Sintoma8','i': 'Sintoma9','j': 'Sintoma10',
'k': 'Sintoma11','l': 'Sintoma12', 'm': 'Sintoma13','n': 'Sintoma14','o': 'Sintoma15',
'p': 'Sintoma16','q':'Sintoma17', 'r':'Sintoma18', 's':'Sintoma19', 't': 'Sintoma20'}

uno = 1

enfermedades = np.array([
# a-t significan síntomas
# a b c d e f g h i j k l m n o p q r s t
 [1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0, uno], #Enfermedad 1
 [0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0, uno], #Enfermedad 2
 [1,1,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0, uno], #Enfermedad 3
 [1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0, uno], #Enfermedad 4
 [1,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0, uno], #Enfermedad 5
 [1,0,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,1,0, uno], #Enfermedad 6
 [1,0,1,0,0,1,0,1,1,0,1,1,1,0,1,0,1,1,1,0, uno], #Enfermedad 7
 [1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,1,1,1,0, uno], #Enfermedad 8
 [1,0,1,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0, uno], #Enfermedad 9
 [1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,0, uno] #Enfermedad 10
])

def conexionDataBase():
	connection = pymysql.connect(host='localhost',
	                             user='root',
	                             password='1234567890',
	                             db='usuarioEnfermedades',
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	cur = connection.cursor()
	cur.execute("select cadena from usuario")
	matriz = cur.fetchall()
	cur.close()
	return matriz #TIENE QUE RETORNAR SOLO LA CADENA
def envio(numero, enfermedad):
	datos = datosAenviar
	logging.info("Subiendo datos a bases de datos")
	try:
		c = pymysql.connect(host = "localhost", user = "root", password = "1234567890", db = "aguapro")
		string = "INSERT INTO usuario(Numero, Enfermedad) VALUES "+'('+str(numero)+','+str(enfermedad)+')'
	 	with c.cursor() as cursor:
			sql = string
			cursor.execute(sql)
		c.commit()
	except:
			print"No se ha encontrado DataBase"

matrizUnos = np.ones((1, len(enfermedades)))
q = len(enfermedades)

z = enfermedades.transpose()

#Patrones de activación para cada enfermedad
Enfermedad1 = np.array([1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
Enfermedad2 = np.array([-1,1,-1,-1,-1,-1,-1,-1,-1,-1])
Enfermedad3 = np.array([-1,-1,1,-1,-1,-1,-1,-1,-1,-1])
Enfermedad4 = np.array([-1,-1,-1,1,-1,-1,-1,-1,-1,-1])
Enfermedad5 = np.array([-1,-1,-1,-1,1,-1,-1,-1,-1,-1])
Enfermedad6 = np.array([-1,-1,-1,-1,-1,1,-1,-1,-1,-1])
Enfermedad7 = np.array([-1,-1,-1,-1,-1,-1,1,-1,-1,-1])
Enfermedad8 = np.array([-1,-1,-1,-1,-1,-1,-1,1,-1,-1])
Enfermedad9 = np.array([-1,-1,-1,-1,-1,-1,-1,-1,1,-1])
Enfermedad10 =np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1,1])

T = np.array([Enfermedad1, Enfermedad2, Enfermedad3, Enfermedad4,
Enfermedad5, Enfermedad6, Enfermedad7, Enfermedad8,
Enfermedad9, Enfermedad10])

#Aprendizaje

w1 = []
w2 = []
w3 = []
w4 = []
w5 = []
w6 = []
w7 = []
w8 = []
w9 = []
w10 = []

R =  float(1)/float(q)  * np.dot(z, z.transpose())
H = float(1)/float(q)   * np.dot(z, T.transpose())
Xm = np.dot(linalg.pinv(R), H)


for i in range(len(Xm) - 1):
    w1.append(Xm[i][0])
    w2.append(Xm[i][1])
    w3.append(Xm[i][2])
    w4.append(Xm[i][3])
    w5.append(Xm[i][4])
    w6.append(Xm[i][5])
    w7.append(Xm[i][6])
    w8.append(Xm[i][7])
    w9.append(Xm[i][8])
    w10.append(Xm[i][9])

b1 = Xm[20][0]
b2 = Xm[20][1]
b3 = Xm[20][2]
b4 = Xm[20][3]
b5 = Xm[20][4]
b6 = Xm[20][5]
b7 = Xm[20][6]
b8 = Xm[20][7]
b9 = Xm[20][8]
b10 = Xm[20][9]


def net_input(entrada, W, B):
	 return np.dot(entrada, W) + B

def definir(expresion):
  if expresion < 0:
    print "desactivada\n"
  else:
    print "activada\n"

entrada = [1,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0]

pesos = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10]

polaridadesF = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]

etiqueta = ["Enf1","Enf2","Enf3","Enf4","Enf5","Enf6","Enf7","Enf8","Enf9","Enf10"]

for i in range(10):
    if(net_input(entrada, pesos[i], polaridadesF[i]) > 0):
        print etiqueta[i]
