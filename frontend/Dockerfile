#Indica la imagen base del contenedor.
FROM python
#Especifica el directorio de trabajo del contenedor.
WORKDIR /usr/src/app
#Copia los archivos que se encuentran en el directorio del Dockerfile al directorio de trabajo.
COPY . .
#Instala las librerías necesarias de python.
RUN pip install --no-cache-dir -r requirements.txt
#Exponer puerto de Contenedor
EXPOSE 8501
#Inicia el servicio del contenedor con el frontend
CMD [ "streamlit", "run", "frontend.py" ]