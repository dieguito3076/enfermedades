#utf8mb4
import pymysql.cursors
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')
#Extrayendo datos de database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234567890',
                             db='usuarioenfermedades',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT lectura FROM lecturaspulso")
        for row in cursor:
            1
        cursor.execute("SELECT lectura FROM lecturastemp")
        for row1 in cursor:
            1
        cursor.execute("SELECT lectura FROM lecturasresp")
        for row2 in cursor:
            1
        cursor.execute("SELECT edad FROM usuarioe")
        for row3 in cursor:
            1
        cursor.execute("SELECT cadenaVal FROM usuarioe")
        for row4 in cursor:
            1
        cursor.execute("SELECT lecturaDiastolica FROM lecturaspulsosistolicodiastolico")
        for row5 in cursor:
            1
        cursor.execute("SELECT lecturaSistolica FROM lecturaspulsosistolicodiastolico")
        for row6 in cursor:
            1
finally:
    connection.close()

resp  =  row2['lectura']
temp  =  row1['lectura']
pulso =  row['lectura']
edad  =  row3['edad']
sintomas = row4['cadenaVal']
diastolicaLec = row5['lecturaDiastolica']
sistolicaLec = row6['lecturaSistolica']


print "\n***********************************************************************\n"
print "Respiraciones: "+ str(resp)
print "Temperatura: "+ str(temp)
print "Pulso: "+ str(pulso)
print "Edad: "+ str(edad)
print "Pulso Diastolico: "+ str(diastolicaLec)
print "Pulso Sistolico: " + str(sistolicaLec)


matrizSintomasWebUsuario = []
for i in range(len(sintomas)):
    matrizSintomasWebUsuario.append(sintomas[i])

print "Cadena: "
print matrizSintomasWebUsuario
print "\n***********************************************************************"
def analizarSignosVitales(edad):
    signoTensionArterial = {'Recien_Nacido':[70, 100, 50, 68],
                            'Infante':[84,106,56,70],
                            'Lactante_Mayor':[98,106,58,70],
                            'Pre-escolar':[99,112,64,70],
                            'Escolar':[104,124,64,86],
                            'Adolescente':[118,132,70,82],
                            'Adulto':[110,140,70,90],
                            'Adultos_Mayores':[110,140,70,110]}

    signoFrecuenciaCardiaca = {'Recien_Nacido':[120,140],
                                'Infante':[100,130],
                                'Lactante_Mayor':[100,120],
                                'Pre-escolar':[80,120],
                                'Escolar':[80,100],
                                'Adolescente':[70,80],
                                'Adulto':[60,80],
                                'Adultos_Mayores':[60,100]}

    signoFrecuenciaRespiratoria = {'Recien_Nacido':[40,45],
                                'Infante':[20,30],
                                'Lactante_Mayor':[20,30],
                                'Pre-escolar':[20,30],
                                'Escolar':[12,20],
                                'Adolescente':[12,20],
                                'Adulto':[12,20],
                                'Adultos_Mayores':[15,20]}

    signoTemperatura = {'Recien_Nacido':[38,38],
                        'Infante':[37.5,37.8],
                        'Lactante_Mayor':[37.5, 37.8],
                        'Pre-escolar':[37.5, 37.8],
                        'Escolar':[37,37.5],
                        'Adolescente':[37,37],
                        'Adulto':[36.2, 37.2],
                        'Adultos_Mayores':[37,37]}

    categorias = ['Menor','Mayor']
    dataFrameSignoTensionArterial = pd.DataFrame(signoTensionArterial)
    dataFrameSignoFrecuenciaRespiratoria = pd.DataFrame(signoFrecuenciaRespiratoria,index=[categorias])
    dataFrameSignoFrecuenciaCardiaca = pd.DataFrame(signoFrecuenciaCardiaca,index=[categorias])
    dataFrameSignoTemperatura = pd.DataFrame(signoTemperatura,index=[categorias])

    #Determinar la etiqueta que recibira la edad para comenzar comparacion

    if(edad<1 and edad<0.5):
        etiqueta = 'Recien_Nacido'
    elif(edad<1 and edad>0.5):
        etiqueta = 'Infante'
    elif(edad>= 1 and edad <2):
        etiqueta = 'Lactante_Mayor'
    elif(edad >= 2 and edad <6):
        etiqueta = 'Pre-escolar'
    elif(edad >= 6 and edad <13):
        etiqueta = 'Escolar'
    elif(edad >= 13 and edad <16):
        etiqueta = 'Adolescente'
    elif(edad>=16 and edad <70):
        etiqueta = 'Adulto'
    elif(edad>70):
        etiqueta = 'Adultos_Mayores'
    #Una vez determinada, extraer la matriz correspondiente por data frame

    matrizFrecuenciaRespiratoria = dataFrameSignoFrecuenciaRespiratoria[etiqueta]
    matrizFrecuenciaCardiaca     = dataFrameSignoFrecuenciaCardiaca[etiqueta]
    matrizTemperatura            = dataFrameSignoTemperatura[etiqueta]
    matrizPulso                  = dataFrameSignoTensionArterial[etiqueta]

    print "\nLa matriz con valores de Frecuencia Respiratoria es:"
    print "\nMenor:" + str(matrizFrecuenciaRespiratoria[0]) + " Y Mayor:" + str(matrizFrecuenciaRespiratoria[1])
    print "\nLa matriz con valores de Frecuencia Cardiaca es:"
    print "\nMenor:" + str(matrizFrecuenciaCardiaca[0]) + " Y Mayor:" + str(matrizFrecuenciaCardiaca[1])
    print "\nLa matriz con valores de Temperatura es:"
    print "\nMenor:" + str(matrizTemperatura[0]) + " Y Mayor:" + str(matrizTemperatura[1])
    print "\nLa matriz con valores de Pulso es:"
    print "\nSISTOLICA  Menor:" + str(matrizPulso[0]) + " Y Mayor:" + str(matrizPulso[1])
    print "DIASTOLICA  Menor:" + str(matrizPulso[2]) + " Y Mayor:" + str(matrizPulso[3])

    #Llevar a cabo la comparacion

    cadenaSintomaticaSignosVitales = [0,0,0,0,0,0,0,0,0,0]
    #Evaluando las respiraciones por minuto.
    if(resp < matrizFrecuenciaRespiratoria[0]):
        cadenaSintomaticaSignosVitales[0] = 1
    elif(resp > matrizFrecuenciaRespiratoria[1]):
        cadenaSintomaticaSignosVitales[1] = 1
    if(pulso < matrizFrecuenciaCardiaca[0]):
        cadenaSintomaticaSignosVitales[2] = 1
    elif(pulso > matrizFrecuenciaCardiaca[1]):
        cadenaSintomaticaSignosVitales[3] = 1
    if(temp < matrizTemperatura[0]):
        cadenaSintomaticaSignosVitales[4] = 1
    elif(temp > matrizTemperatura[1]):
        cadenaSintomaticaSignosVitales[5] = 1

    #Producir la cadena binaria que se anexara a la cadena sintomatica

    print "La cadena Sintomatica para los signos vitales es: "
    print cadenaSintomaticaSignosVitales

    #Visualizacion de signos vitales
    dataFrameSignoTensionArterial.plot()
    plt.title('Tension Arterial')
    dataFrameSignoFrecuenciaRespiratoria.plot()
    plt.title('Frecuencua Respiratoria')
    dataFrameSignoFrecuenciaCardiaca.plot()
    plt.title('Frecuencia Cardiaca')
    dataFrameSignoTemperatura.plot()
    plt.title('Temperatura')
    plt.show()

analizarSignosVitales(edad)
