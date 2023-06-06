import pandas as pd
import mariadb
from flask import Flask, jsonify
from flask_caching import Cache

# Conexión a la base de datos
def establecer_conexion():
    conexion = mariadb.connect(
        user='root',
        password='root',
        host='bd_app',
        database='appTiempo',
        )
    return(conexion)

# Leer datos de la tabla precipitaciones en un DataFrame
def precipitaciones():
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    consulta_p = "SELECT prob FROM precipitaciones WHERE dia >= DATE_SUB(CURDATE(), INTERVAL 10 DAY) AND dia <= CURDATE()"
    cursor.execute(consulta_p)
    datos_precipitaciones = cursor.fetchall()
    df_precipitaciones = pd.DataFrame(datos_precipitaciones, columns=['prob'])
    conexion.close()
    return(df_precipitaciones)
df_precipitaciones = precipitaciones()

# Leer datos de la tabla temperaturas en un DataFrame
def temperaturas():
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    consulta_t = "SELECT dia,maxima FROM temperaturas WHERE dia >= DATE_SUB(CURDATE(), INTERVAL 10 DAY) AND dia <= CURDATE()"
    cursor.execute(consulta_t)
    datos_temperaturas = cursor.fetchall()
    df_temperaturas = pd.DataFrame(datos_temperaturas, columns=['dia','maxima'])
    conexion.close()
    return(df_temperaturas)
df_temperaturas = temperaturas()

# Leer datos de la tabla humedades en un DataFrame
def humedades():
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    consulta_h = "SELECT maxima FROM humedades WHERE dia >= DATE_SUB(CURDATE(), INTERVAL 10 DAY) AND dia <= CURDATE()"
    cursor.execute(consulta_h)
    datos_humedades = cursor.fetchall()
    df_humedades = pd.DataFrame(datos_humedades, columns=['maxima'])
    conexion.close()
    return(df_humedades)
df_humedades = humedades()

# Leer datos de la tabla vientos en un DataFrame
def vientos():
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    consulta_v = "SELECT velocidad,gust,gradosº FROM vientos WHERE dia >= DATE_SUB(CURDATE(), INTERVAL 10 DAY) AND dia <=CURDATE()"
    cursor.execute(consulta_v)
    datos_vientos = cursor.fetchall()
    df_vientos = pd.DataFrame(datos_vientos, columns=['velocidad','gust', 'gradosº'])
    conexion.close()
    return(df_vientos)
df_vientos = vientos()

# Hacer cálculos necesarios para determinar las condiciones de navegación del mar en función de la velocidad del viento, en función de la velocidad la cual está medida en nudos, mandará un valor al endpoint.
def condiciones():
    media_v = df_vientos['velocidad'].mean()
    if media_v < 1:
        return(str(10))#'calma'

    if media_v >= 1 or media_v <=3:
        return(str(20))#'ventolina'

    if media_v >= 4 or media_v <=6:
        return(str(30))#'flojito'
    
    if media_v >= 7 or media_v <=10:
        return(str(40))#'flojo'

    if media_v >= 11 or media_v <=16:
        return(str(50))#'bonancible'

    if media_v >= 17 or media_v <=21:
        return(str(60))#'fresquito'

    if media_v >= 22 or media_v <=27:
        return(str(70))#'fresco'

    if media_v >= 28 or media_v <=33:
        return(str(80))#'frescachon'

    if media_v >= 34 or media_v <=40:
        return(str(90))#'temporal'

    if media_v >= 41 or media_v <=47:
        return(str(100))#'temporal fuerte'

    if media_v >= 48 or media_v <=55:
        return(str(110))#'temporal duro'

    if media_v >= 56 or media_v <=63:
        return(str(120))#'temporal muy duro'

    if media_v >= 64 or media_v <=71:
        return(str(130))#'huracanado'
nav = condiciones()

def vientos_actual():
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    consulta_v_actual = "SELECT velocidad, gust, gradosº FROM vientos ORDER BY dia DESC LIMIT 1"
    cursor.execute(consulta_v_actual)
    datos_vientos_actual = cursor.fetchall()
    df_vientos_actual = pd.DataFrame(datos_vientos_actual, columns=['velocidad','gust', 'gradosº'])
    conexion.close()
    return(df_vientos_actual)
df_vientos_actual = vientos_actual()

# Calcula las condiciones actuales de navegación
def condiciones_actual():
    velocidad_actual = df_vientos_actual['velocidad'].iloc[0]
    if velocidad_actual < 1:
        return(str(10))#'calma'

    if velocidad_actual >= 1 or velocidad_actual <=3:
        return(str(20))#'ventolina'

    if velocidad_actual >= 4 or velocidad_actual <=6:
        return(str(30))#'flojito'
    
    if velocidad_actual >= 7 or velocidad_actual <=10:
        return(str(40))#'flojo'

    if velocidad_actual >= 11 or velocidad_actual <=16:
        return(str(50))#'bonancible'

    if velocidad_actual >= 17 or velocidad_actual <=21:
        return(str(60))#'fresquito'

    if velocidad_actual >= 22 or velocidad_actual <=27:
        return(str(70))#'fresco'

    if velocidad_actual >= 28 or velocidad_actual <=33:
        return(str(80))#'frescachon'

    if velocidad_actual >= 34 or velocidad_actual <=40:
        return(str(90))#'temporal'

    if velocidad_actual >= 41 or velocidad_actual <=47:
        return(str(100))#'temporal fuerte'

    if velocidad_actual >= 48 or velocidad_actual <=55:
        return(str(110))#'temporal duro'

    if velocidad_actual >= 56 or velocidad_actual <=63:
        return(str(120))#'temporal muy duro'

    if velocidad_actual >= 64 or velocidad_actual <=71:
        return(str(130))#'huracanado'
nav_actual = condiciones_actual()

# Leer la tabla presiones en un DataFrame
def presiones():
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    consulta_pre = "SELECT absoluta,relativa FROM presion WHERE dia >= DATE_SUB(CURDATE(), INTERVAL 10 DAY) AND dia <=CURDATE()"
    cursor.execute(consulta_pre)
    datos_presion = cursor.fetchall()
    df_presion = pd.DataFrame(datos_presion, columns=['absoluta', 'relativa'])
    conexion.close()
    return(df_presion)
df_presion = presiones()

# Creación de los métodos get para la obtención de datos de las tablas
app = Flask(__name__)

# Creación Caché
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Método get para obtener los promedios de la probabilidad de lluvia
@app.route('/promedio_prob_precipitacion', methods=['GET'])
@cache.cached(timeout=120)
def obtner_promedio_prob_precipitacion():
    global df_precipitaciones
    promedio_prob_precipitacion = df_precipitaciones['prob'].mean()
    precipitaciones_formateada = '{:.2f}'.format(promedio_prob_precipitacion)
    return jsonify(precipitaciones_formateada)

# Obtener la temperatura máxima promedio por día
@app.route('/promedio_temperaturas', methods=['GET'])
@cache.cached(timeout=120)
def obtener_promedio_maxima_temperatura():
    promedio_maxima_temperatura = df_temperaturas['maxima'].mean()
    temperaturas_formateada = '{:.2f}'.format(promedio_maxima_temperatura)
    return jsonify(temperaturas_formateada)

# Obtener la humedad relativa máxima promedio por día
@app.route('/promedio_humedades', methods=['GET'])
@cache.cached(timeout=120)
def obtener_promedio_maxima_humedad():
    promedio_maxima_humedad = df_humedades['maxima'].mean()
    humedad_formateada = '{:.0f}'.format(promedio_maxima_humedad)
    return jsonify(humedad_formateada)

# Obtener probabilidad de temperaturas
@app.route('/probabilidad_calor', methods=['GET'])
@cache.cached(timeout=120)
def obtener_probabilidad_calor():
    df_filtrado = df_temperaturas[df_temperaturas['maxima'] > 20]
    df_filtrado_h = df_humedades[df_humedades['maxima'] > 45]
    df_prob_calor = len(df_filtrado) + len(df_filtrado_h)
    df_prob_m = len(df_humedades['maxima']) + len(df_temperaturas['maxima'])
    probabilidad_calor = df_prob_calor/df_prob_m
    temperatura_porcentaje = probabilidad_calor * 100
    probabilidad_formateada = '{:.0f}'.format(temperatura_porcentaje)
    return jsonify(probabilidad_formateada)

#Obtener probabilidad de frío
@app.route('/probabilidad_frio', methods=['GET'])
@cache.cached(timeout=120)
def obtener_probabilidad_frio():
    df_filtrado = df_temperaturas[df_temperaturas['maxima'] < 20]
    probabilidad_frio = len(df_filtrado)/len(df_temperaturas['maxima'])
    temperatura_porcentaje = probabilidad_frio * 100
    probabilidad_formateada = '{:.0f}'.format(temperatura_porcentaje)
    return jsonify(probabilidad_formateada)

@app.route('/condiciones_nav', methods=['GET'])
@cache.cached(timeout=120)
def navegar():
    global nav
    if nav == '10' or nav == '20' or nav == '30' or nav == '40':
        return ('El mar es óptimo para navegar')
    if nav == '50' or nav == '60' or nav == '70' or nav == '80':
        return ('Se recomienda no navegar con barcos pequeños')
    if nav == '90' or nav == '100':
        return ('Se recomienda no navegar')
    if nav == '110' or nav == '120' or nav == '130':
        return ('Imposible Navegar')
    
@app.route('/condiciones_nav_actual', methods=['GET']) #Manda un mensaje en función del valor calculado por la función.
@cache.cached(timeout=120)
def navegar_actual():
    global nav_actual
    if nav_actual == '10' or nav_actual == '20' or nav_actual == '30' or nav_actual == '40':
        return ('El mar es óptimo para navegar')
    if nav_actual == '50' or nav_actual == '60' or nav_actual == '70' or nav_actual == '80':
        return ('Se recomienda no navegar con barcos pequeños')
    if nav_actual == '90' or nav_actual == '100':
        return ('Se recomienda no navegar')
    if nav_actual == '110' or nav_actual == '120' or nav_actual == '130':
        return ('Imposible Navegar')

@app.route('/icono', methods=['GET']) #Endpoint para pasarle al frontend el tipo de icono a mostrar en el mapa en función de las condiciones climatológicas.
@cache.cached(timeout=120)
def ficon():
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    consulta_tic = "SELECT maxima FROM temperaturas ORDER BY dia DESC LIMIT 1"
    cursor.execute(consulta_tic)
    i_temp = cursor.fetchall()
    df_i_temp = pd.DataFrame(i_temp, columns=['maxima'])
    consulta_tpre = "SELECT prob FROM precipitaciones ORDER BY dia DESC LIMIT 1"
    cursor.execute(consulta_tpre)
    i_pre = cursor.fetchall()
    df_i_pre = pd.DataFrame(i_pre, columns=['prob'])
    consulta_uvi = "SELECT uvi FROM solar ORDER BY dia DESC LIMIT 1"
    cursor.execute(consulta_uvi)
    i_uvi = cursor.fetchall()
    df_i_uvi = pd.DataFrame(i_uvi, columns=['uvi'])
    conexion.close()
    if df_i_uvi['uvi'].iloc[0] <= 2 and df_i_uvi['uvi'].iloc[0] > 0:
        return('cloud')
    elif df_i_pre['prob'].iloc[0] >= 40:
        return('umbrella')
    elif df_i_temp['maxima'].iloc[0] >= 20 and df_i_uvi['uvi'].iloc[0] > 2:
        return('sun')
    else:
        return('moon')
    
@app.route('/temperatura', methods=['GET'])
@cache.cached(timeout=120)
def demo():
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    consulta_tic = "SELECT maxima FROM temperaturas ORDER BY dia DESC LIMIT 1"
    cursor.execute(consulta_tic)
    d_temp = cursor.fetchall()
    df_d_temp = pd.DataFrame(d_temp, columns=['maxima'])
    demo = str(df_d_temp['maxima'].iloc[0])
    conexion.close()
    return jsonify(demo)

#Iniciar la API
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)