from bs4 import BeautifulSoup
import requests
import mariadb
conexion = mariadb.connect( #Parámetros necesarios para la conexión con el servidor de base de datos.
    user='ruben',
    password='ruben',
    host='192.168.1.33',
    database='appTiempo',
)
cursor = conexion.cursor() #Inicialización del cursor que recibirá las secuencias sql.
datos = requests.get('https://www.aemet.es/xml/municipios/localidad_41034.xml') #Sentencia request que utiliza un método get para obtener la información del fichero xml.
soup = BeautifulSoup(datos.text, features='xml') #Creación de la sopa. Se debe formatear en texto la salida del método get y debemos expecifiar que formato estamos parseando "xml"

# Filtrar los datos para obtener los días y las probabilidades de precipitaciones. Inicializo dos duplas.
dias=[] #Tupla que contendrá los días.
precipitacionest=[] #Tupla que contendrá las propabilidades de cada día.
#Bucle para almacenar información en las tuplas
for dia in soup.find_all('dia'): #De esta manera busco todas las etiquetas del xml que se llamen día
    precipitacionest.append(dia.prob_precipitacion.text) #Ingreso el contenido de la etiqueta de probabilidad en la tupla corrspondiente.
    dias.append(dia['fecha'])#Ingreso el día en la tupla correspondiente.
precipitaciones = tuple(zip(dias, precipitacionest)) #Unifico las dos tuplas en una, de manera que cada día esté con su probabilidad.
for valor in precipitaciones: #Bucle para crear la sentencia sql de cada día. El bucle recorrerá toda la tupla.
    valor0=str(valor[0]) #Posición de la fecha en la tupla.
    valor1=int(valor[1]) #Posición de la probabilidad en la tupla.
    consulta_p = "INSERT INTO precipitaciones VALUES (clave_prec, ?, ?)"# Creo la variable de la sentencia sql. Las '?' significan que le paseré posteriormente los valores.
    cursor.execute(consulta_p, (valor0, valor1))#Le paso los valores y ejecuto la sentencia sql.
conexion.commit()#Guardo los cambios. Importante hacerlo.
#Filtrar datos para obener temperaturas.
dias_temperaturas=[]
maximas_t=[]#Tupla de las máximas temperaturas.
minimas_t=[]#Tupla de las mínimas temperaturas.
for dia in soup.find_all('dia'):
    temperatura = dia.find('temperatura')
    maximas_t.append(temperatura.maxima.text)
    minimas_t.append(temperatura.minima.text)
    dias_temperaturas.append(dia['fecha'])
temperaturas = tuple(zip(dias_temperaturas, maximas_t, minimas_t))
#Bucle para almacenar en las tuplas de temperaturas.
for valor in temperaturas:
    valor0=str(valor[0])
    valor1=int(valor[1])
    valor2=int(valor[2])
    consulta_p = "INSERT INTO temperaturas VALUES (clave_t, ?, ?, ?)"
    cursor.execute(consulta_p, (valor0, valor1, valor2))
conexion.commit()
#Filtrar datos para obtener humedades relativas.
dias_h=[]
maxima_h=[]
minima_h=[]
for dia in soup.find_all('dia'):
    humedad = dia.find('humedad_relativa')
    maxima_h.append(humedad.maxima.text)
    minima_h.append(humedad.minima.text)
    dias_h.append(dia['fecha'])
humedades = tuple(zip(dias_h, maxima_h, minima_h))
#Bucle para almacenar en las tuplas de humedades.
for valor in humedades:
    valor0=str(valor[0])
    valor1=int(valor[1])
    valor2=int(valor[2])
    consulta_p = "INSERT INTO humedades VALUES (clave_h, ?, ?, ?)"
    cursor.execute(consulta_p, (valor0, valor1, valor2))
conexion.commit()
conexion.close()#Cerrar la conexión. Si no se hace el código no parará de ejecutarse hasta cerrar conexión.