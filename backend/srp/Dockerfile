#Indica la imagen base del contenedor.
FROM debian
#Especifica el directorio de trabajo del contenedor.
WORKDIR /
#Copia los archivos que se encuentran en el directorio del Dockerfile al directorio de trabajo.
COPY . .
#Instalar paquetes en contenedor.
RUN apt-get update && apt-get install -y cron python3.9 python3-pip libmariadbd-dev libmariadb3
#Instala las librerías necesarias de python.
RUN pip install --no-cache-dir -r requirements.txt
#Instala mariadb
RUN pip install mariadb
#Indicar puerto del contenedor
EXPOSE 5000
#Inicia el servicio del contenedor
CMD [ "python3", "app.py" ]