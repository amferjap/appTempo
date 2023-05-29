FROM mariadb:latest
# Contraseña de usuario root para mariadb
ENV MARIADB_ROOT_PASSWORD root
# Base de datos que queremos crear en el inicio del contenedor
ENV MARIADB_DATABASE appTiempo
# Se añade el script de creación de las tablas
ADD init.sql /docker-entrypoint-initdb.d/
# Se expone el puerto por defecto de mariadb
EXPOSE 3306