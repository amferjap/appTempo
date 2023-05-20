import streamlit as st
import requests
import altair as alt
import pandas as pd

#Inseta en la página una presentación
st.title('Bienvenido a appTiempo')
st.header('¿Que te gustaría saber?')

# Crea un botón en la pagina para la obtención de pormedios, dependiendo que pulse mostrará un promedio u otro.
col1, col2, col5 = st.columns(3)

with col1:
    st.subheader('Precipitaciones')
    r = requests.get('http://api_backend:5000/promedio_prob_precipitacion')
    st.write(r.text)

with col2:
    st.subheader('Temperaturas')
    v = requests.get('http://api_backend:5000/promedio_temperaturas')
    st.write(v.text)

with col5:
    st.subheader('Humedades')
    x = requests.get('http://api_backend:5000/promedio_humedades')
    st.write(x.text)

# Inserta un botón para la obtención de la probabilidad de frío o calor, dependiendo de que pulse mostrará uno u otro.
col3,col4 = st.columns(2)

with col3:
    st.write('Probalidad de calor')
    if st.button('Calor'):
        y = requests.get('http://api_backend:5000/probabilidad_calor')
        st.write(y.text,'%')
with col4:
    st.write('Probalidad de frío')
    if st.button('Frio'):
        w = requests.get('http://api_backend:5000/probabilidad_frio')
        st.write(w.text,'%')

st.subheader('Condciones para navegar')

tab1, tab2 = st.tabs(["Pornóstico", "Actual"])
with tab1:
    z = requests.get('http://api_backend:5000/condiciones_nav')
    st.info(z.text)

with tab2:
    a = requests.get('http://api_backend:5000/condiciones_nav_actual')
    st.info(a.text)