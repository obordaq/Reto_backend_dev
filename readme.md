# Reto Python
Contamos con mediciones ambientales de manera periodica e irregularmente en formato json.

Los campos que se encuentran en cada json son:
```
'CO', 'CO_ug_m3', 'H2S', 'H2S_ug_m3', 'I_temperature', 'NO2', 'NO2_ug_m3', 'O3', 'O3_ug_m3', 'PM10', 'PM25', 'SO2', 'SO2_ug_m3', 'SPL', 'UV', 'humidity', 'lat','lon', 'pressure', 'temperature', 'timestamp_zone'
```
En el repositorio van a encontrar 4 archivos:

contiene los nombres de cada modulo:
```
modulos.json
```
contienen las mediciones respectivas de cada modulo:
```
qh019_processed.json
qh032_processed.json
qh041_processed.json
```

#

### El reto consiste en desarrollar una o más funciones que permitan detectar valores repetidos. Valores repetidos se consideran los valores que en un periodo de 5 min tengan el mismo valor en el mismo modulo y mismo contaminante.
#

Los campos de contaminantes donde se deberian buscar los valores repetidos son:
```
'humidity','pressure','temperature','SPL','I_temperature','UV','CO_ug_m3','H2S_ug_m3','NO2_ug_m3','O3_ug_m3','PM1','PM10','PM25','SO2_ug_m3'
```
Se espera un output de la siguente manera (en consola):
```
'NOMBRE envió el mismo valor en un periodo de 5 min'
'Se congelaron los siguientes valores: {'contaminante': valor repetido}'
```
por ejemplo:
```
'qH0XX envió el mismo valor en un periodo de 5 min'
'Se congelaron los siguientes valores: {'H2S_ug_m3': 526.36, 'I_temperature': 30.9, 'pressure': 997.759}'
```
### Pasos a seguir:

1- Clonar el repositorio

2- Resolver el reto en su computadora de forma local

3- Crear un branch en GitHub con su nombre

4- Subir su respuesta al branch creado

### Tiempo de desarrollo: 2 horas