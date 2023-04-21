import streamlit as st
import requests

st.write('Bienvenido a appTiempo')
st.write('¿Que te gustaría saber?')

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

st.write('Frío o Calor')
if st.button('Calor'):
    y = requests.get('http://api_backend:5000/probabilidad_calor')
    st.write(y.text,'%')
if st.button('Frío'):
    z = requests.get('http://api_backend:5000/probabilidad_frio')
    st.write(z.text,'%')