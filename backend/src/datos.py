import requests
import mariadb
import pytemperature
import datetime

conexion = mariadb.connect( #Parámetros necesarios para la conexión con el servidor de base de datos.
    user='root',
    password='root',
    host='bd_app',
    database='appTiempo',
)
cursor = conexion.cursor() #Inicialización del cursor que recibirá las secuencias sql.

data = requests.get('https://api.ecowitt.net/api/v3/device/real_time?application_key=4BB7A8EAD086979D5CD6F826A0701FB3&api_key=b0a66202-442d-4f17-9be6-7a4ace047048&mac=7C:87:CE:BC:C1:33&call_back=all') #Sentencia request que utiliza un método get para obtener la información del fichero xml.
datos = data.json()

fecha = datetime.datetime.now()

temperatura_bruta = float(datos['data']['outdoor']['temperature']['value'])
temperatura_neta = pytemperature.f2c(temperatura_bruta)

consulta_p = "INSERT INTO temperaturas VALUES (clave_t, ?, ?)"# Creo la variable de la sentencia sql. Las '?' significan que le paseré posteriormente los valores.
cursor.execute(consulta_p, (fecha, temperatura_neta))#Le paso los valores y ejecuto la sentencia sql.
conexion.commit()

humedad = float(datos['data']['outdoor']['humidity']['value'])

consulta_p = "INSERT INTO humedades VALUES (clave_h, ?, ?)"# Creo la variable de la sentencia sql. Las '?' significan que le paseré posteriormente los valores.
cursor.execute(consulta_p, (fecha, humedad))#Le paso los valores y ejecuto la sentencia sql.
conexion.commit()

prob_lluvia = float(datos['data']['rainfall']['rain_rate']['value'])

consulta_p = "INSERT INTO precipitaciones VALUES (clave_prec, ?, ?)"# Creo la variable de la sentencia sql. Las '?' significan que le paseré posteriormente los valores.
cursor.execute(consulta_p, (fecha, prob_lluvia))#Le paso los valores y ejecuto la sentencia sql.
conexion.commit()

velocidad = float(datos['data']['wind']['wind_speed']['value'])
gust = float(datos['data']['wind']['wind_gust']['value'])
direccion = float(datos['data']['wind']['wind_direction']['value'])

velocidad_km = velocidad * 1.60934
nudos = velocidad * 0.868976
gust_km = gust * 1.60934

consulta_p = "INSERT INTO vientos VALUES (clave_v, ?, ?, ?, ?)"# Creo la variable de la sentencia sql. Las '?' significan que le paseré posteriormente los valores.
cursor.execute(consulta_p, (fecha, nudos, gust_km, direccion))#Le paso los valores y ejecuto la sentencia sql.
conexion.commit()

presion_a = float(datos['data']['pressure']['absolute']['value'])
presion_r = float(datos['data']['pressure']['relative']['value'])

consulta_p = "INSERT INTO presion VALUES (clave_p, ?, ?, ?)"# Creo la variable de la sentencia sql. Las '?' significan que le paseré posteriormente los valores.
cursor.execute(consulta_p, (fecha, presion_a, presion_r))#Le paso los valores y ejecuto la sentencia sql.
conexion.commit()

conexion.close()