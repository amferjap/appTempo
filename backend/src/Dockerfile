#Indica la imagen base del contenedor.
FROM debian
#Especifica el directorio de trabajo del contenedor.
WORKDIR /
#Copia los archivos que se encuentran en el directorio del Dockerfile al directorio de trabajo.
COPY . .
#Instala paquetes necesaarios para el funcionamiento del programa.
RUN apt-get update && apt-get install -y cron python3.9 python3-pip libmariadbd-dev libmariadb3
#Instala las librerías necesarias de python.
RUN pip install --no-cache-dir -r requirements.txt
#Instala la librería de Mariadb.
RUN pip install mariadb
#Copia el archivo de crontab a la ruta del demonio de crontab.
RUN cp crontab /etc/cron.d/crontab
#Añade una línea vacia al final del archivo. Si no se hace da error.
RUN echo >> /etc/cron.d/crontab
#Reinicia el servicio de crontab.
RUN service cron restart
#Inicializa la tarea.
RUN crontab /etc/cron.d/crontab
#Inicia el servicio de Cron al crear el contenedor y lo mantiene ejecutando en segundo plano.
CMD cron && tail -f /dev/null