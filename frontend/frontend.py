import streamlit as st
import requests

#Inseta en la página una presentación
st.write('Bienvenido a appTiempo')
st.write('¿Que te gustaría saber?')

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
st.write('Frío o Calor')
if st.button('Calor'):
    y = requests.get('http://api_backend:5000/probabilidad_calor')
    st.write(y.text,'%')
if st.button('Frío'):
    z = requests.get('http://api_backend:5000/probabilidad_frio')
    st.write(z.text,'%')