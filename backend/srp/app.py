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
consulta_p = "SELECT * FROM precipitaciones"
cursor.execute(consulta_p)
datos_precipitaciones = cursor.fetchall()
df_precipitaciones = pd.DataFrame(datos_precipitaciones, columns=['clave_prec', 'fecha', 'probabilidad'])

# Leer datos de la tabla temperaturas en un DataFrame
consulta_t = "SELECT * FROM temperaturas"
cursor.execute(consulta_t)
datos_temperaturas = cursor.fetchall()
df_temperaturas = pd.DataFrame(datos_temperaturas, columns=['clave_t', 'fecha', 'maxima', 'minima'])

# Leer datos de la tabla humedades en un DataFrame
consulta_h = "SELECT * FROM humedades"
cursor.execute(consulta_h)
datos_humedades = cursor.fetchall()
df_humedades = pd.DataFrame(datos_humedades, columns=['clave_h', 'fecha', 'maxima', 'minima'])

conexion.close()

app = Flask(__name__)

@app.route('/promedio_prob_precipitacion', methods=['GET'])
def obtner_promedio_prob_precipitacion():
    promedio_prob_precipitacion = df_precipitaciones['probabilidad'].mean()
    return jsonify(promedio_prob_precipitacion)

# Obtener la temperatura máxima y mínima promedio por día
@app.route('/promedio_temperaturas', methods=['GET'])
def obtener_promedio_maxima_temperatura():
    promedio_maxima_temperatura = df_temperaturas['maxima'].mean()
    return jsonify(promedio_maxima_temperatura)
def obtener_promedio_minima_temperatura():
    promedio_minima_temperatura = df_temperaturas['minima'].mean()
    return jsonify(promedio_minima_temperatura)

# Obtener la humedad relativa máxima y mínima promedio por día
@app.route('/promedio_humedades', methods=['GET'])
def obtener_promedio_maxima_humedad():
    promedio_maxima_humedad = df_humedades['maxima'].mean()
    return jsonify(promedio_maxima_humedad)
def obtener_promedio_minima_humedad(): 
    promedio_minima_humedad = df_humedades['minima'].mean()
    return jsonify(promedio_minima_humedad)

# Obtener probabilidad de temperaturas
@app.route('/probabilidad_calor', methods=['GET'])
def obtener_probabilidad_calor():
    df_filtrado = df_temperaturas[df_temperaturas['maxima'] > 30]
    probabilidad_calor = len(df_filtrado)/len(df_temperaturas['maxima'])
    temperatura_porcentaje = probabilidad_calor * 100
    probabilidad_formateada = '{:.0f}'.format(temperatura_porcentaje)
    return jsonify(probabilidad_formateada)
@app.route('/probabilidad_frio', methods=['GET'])
def obtener_probabilidad_frio():
    df_filtrado_fr = df_temperaturas[df_temperaturas['minima']<5]
    probabilidad_frio = len(df_filtrado_fr)/len(df_temperaturas['minima'])
    temperatura_porcentaje_fr = probabilidad_frio * 100
    probabilidad_formateada_fr = '{:.0f}'.format(temperatura_porcentaje_fr)
    return jsonify(probabilidad_formateada_fr)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)