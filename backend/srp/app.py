import pandas as pd
import mariadb
from flask import Flask, jsonify

# Conexión a la base de datos
conexion = mariadb.connect(
    user='ruben',
    password='ruben',
    host='bd_app',
    database='appTiempo',
)
cursor = conexion.cursor()

# Leer datos de la tabla precipitaciones en un DataFrame
consulta_p = "SELECT probabilidad FROM precipitaciones WHERE fecha >= DATE_SUB(CURDATE(), INTERVAL 10 DAY) AND FECHA <= CURDATE()"
cursor.execute(consulta_p)
datos_precipitaciones = cursor.fetchall()
df_precipitaciones = pd.DataFrame(datos_precipitaciones, columns=['probabilidad'])

# Leer datos de la tabla temperaturas en un DataFrame
consulta_t = "SELECT maxima FROM temperaturas WHERE fecha >= DATE_SUB(CURDATE(), INTERVAL 10 DAY) AND FECHA <= CURDATE()"
cursor.execute(consulta_t)
datos_temperaturas = cursor.fetchall()
df_temperaturas = pd.DataFrame(datos_temperaturas, columns=['maxima'])

# Leer datos de la tabla humedades en un DataFrame
consulta_h = "SELECT maxima FROM humedades WHERE fecha >= DATE_SUB(CURDATE(), INTERVAL 10 DAY) AND FECHA <= CURDATE()"
cursor.execute(consulta_h)
datos_humedades = cursor.fetchall()
df_humedades = pd.DataFrame(datos_humedades, columns=['maxima'])

conexion.close()
# Creación de los métodos get para la obtención de datos de las tablas
app = Flask(__name__)
# Método get para obtener los promedios de la probabilidad de lluvia
@app.route('/promedio_prob_precipitacion', methods=['GET'])
def obtner_promedio_prob_precipitacion():
    promedio_prob_precipitacion = df_precipitaciones['probabilidad'].mean()
    return jsonify(promedio_prob_precipitacion)

# Obtener la temperatura máxima y mínima promedio por día
@app.route('/promedio_temperaturas', methods=['GET'])
def obtener_promedio_maxima_temperatura():
    promedio_maxima_temperatura = df_temperaturas['maxima'].mean()
    return jsonify(promedio_maxima_temperatura)

# Obtener la humedad relativa máxima y mínima promedio por día
@app.route('/promedio_humedades', methods=['GET'])
def obtener_promedio_maxima_humedad():
    promedio_maxima_humedad = df_humedades['maxima'].mean()
    return jsonify(promedio_maxima_humedad)

# Obtener probabilidad de temperaturas
@app.route('/probabilidad_calor', methods=['GET'])
def obtener_probabilidad_calor():
    df_filtrado = df_temperaturas[df_temperaturas['maxima'] > 30]
    probabilidad_calor = len(df_filtrado)/len(df_temperaturas['maxima'])
    temperatura_porcentaje = probabilidad_calor * 100
    probabilidad_formateada = '{:.0f}'.format(temperatura_porcentaje)
    return jsonify(probabilidad_formateada)

#Iniciar la API
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)