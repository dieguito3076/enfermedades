import pymysql.cursors
lenPulso = 0
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
            lenPulso = lenPulso + 1
        cursor.execute("SELECT lectura FROM lecturastemp")
        for row1 in cursor:
            lenPulso = lenPulso + 1
        cursor.execute("SELECT lectura FROM lecturasresp")
        for row2 in cursor:
            lenPulso = lenPulso + 1
        cursor.execute("SELECT edad FROM usuarioe")
        for row3 in cursor:
            lenPulso = lenPulso + 1
        cursor.execute("SELECT cadenaVal FROM usuarioe")
        for row4 in cursor:
            lenPulso = lenPulso + 1
finally:
    connection.close()

resp  =  row2['lectura']
temp  =  row1['lectura']
pulso =  row['lectura']
edad  =  row3['edad']
sintomas = row4['cadenaVal']
print "Respiraciones: "+ str(resp)
print "Temperatura: "+ str(temp)
print "Pulso: "+ str(pulso)
print "Edad: "+ str(edad)
print "Cadena: "+ sintomas 
#Determinar que enfermedades tienen por sintoma superficial una determinada edad para hacer la comparacion
#pulsoNomralXedad = num1
#pulsoNomralX1edad = num2
#pulsoNomralX2edad = num3
#pulsoNomralX3edad = num4
def bluetooth():
	port = "COM5"
	bluetooth = serial.Serial(port, 9600)
	bluetooth.flushInput()
	val = bluetooth.readline() #LITROS SOBRE HORA
	valorFinal = val.decode()
	bluetooth.close()
	return valorFinal
