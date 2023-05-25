# appTempo

## Propósito

Este es el proyecto que he realizado para la finalización del Grado Superior de Administración en Sistermas Informáticos en Red. Consiste en el desarrollo de una app con Python para la recogida automática de datos y el análisis de los mismos para realizar previsiones futuras. El desarrollo de la app, estará sometido a los principios
de la integración continua utilizando las herraminetas necesarias para ello.

Por otro lado, esta app estará conformada por un backend y un frontend. El backend se compone de una aplicación de recogida de datos, una aplicación de análisis de datos, una base de datos y una api rest. Esta última, servirá para
establecer la comunicación entre el backend y el frontend, el cual mostrará a través de la web los análisis realizados de los datos.

 El proyecto tiene dos versiones, cada una se aloja en una rama:

- [AEMET](https://github.com/rubenamadoc/App_proyecto/tree/aemet)

Los datos se recogerán desde la web de aemet, realizando web scrapping.

- [Estación Meteorológica](https://github.com/rubenamadoc/App_proyecto/tree/estacion_meteo)

Los datos se obtendrán a través de una estación meteorológica proporcionada por el centro.

Ambas versiones utilizarán las mismas base de datos, api y frontend. La diferencia entre ambas, es como se obtienen e insertan los datos.

Para facilitarme la tarea de que datos utilizar para hacer cálculos y tener valores más realistas y efectivos, he planteado una aplicación para calcular las condiciones meteorológicas de una playa. La aplicación mostrará promedios (temperaturas, lluvias y humedad), condiciones del mar para navegar y estado actual del clima. Este último se mostrará a través de un icono en un mapa con la la localización de la estación.

Para finalizar, ambas versiones tienen toda la documentación de los procedimientos y explicaciones de los códigos. Accediendo a las ramas, podréis ver la documentación. Además de programas y archivos necesarios para el funcionamiento de la app.

![](licencia.png)