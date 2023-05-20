import streamlit as st
import requests
import altair as alt

#Inseta en la página una presentación
st.header('Bienvenido a appTiempo')
st.subheader('¿Que te gustaría saber?')

graf_t = requests.get('http://api_backend:5000/grafica_temperatura')
st.bar_chart(data=graf_t.content, width=3, height=3, use_container_width=True)

# Crea un botón en la pagina para la obtención de pormedios, dependiendo que pulse mostrará un promedio u otro.
st.write('Promedios')
if st.button('Precipitaciones'):
    r = requests.get('http://api_backend:5000/promedio_prob_precipitacion')
    st.write(r.text)
elif st.button('Temperaturas'):
    v = requests.get('http://api_backend:5000/promedio_temperaturas')
    st.write(v.text)
elif st.button('Humedades'):
    x = requests.get('http://api_backend:5000/promedio_humedades')
    st.write(x.text)

# Inserta un botón para la obtención de la probabilidad de frío o calor, dependiendo de que pulse mostrará uno u otro.
st.write('Probalidad de calor')
if st.button('Calor'):
    y = requests.get('http://api_backend:5000/probabilidad_calor')
    st.write(y.text,'%')
st.write('Probalidad de calor')
if st.button('Frio'):
    w = requests.get('http://api_backend:5000/probabilidad_frio')
    st.write(w.text,'%')

st.write('Condiciones para navegar')
if st.button('Navegar'):
    z = requests.get('http://api_backend:5000/condiciones_nav')
    st.write(z.text)

st.write('Condiciones para navegar actuales')
if st.button('Navegar actualmente'):
    a = requests.get('http://api_backend:5000/condiciones_nav_actual')
    st.write(a.text)