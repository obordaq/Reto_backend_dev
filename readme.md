# Reto
Los módulos qHAWAX envían mediciones ambientales cada 20 segundos a una base de datos a través de un API.

#

### El reto consiste en desarrollar una o más funciones que recorran por el nombre de modulo y recorran sus resultados de medicion de data processed correspondientes para detectar si es que hay valores repetidos en alguna medicion en un periodo de 5 min.
#

Los campos de contaminantes donde se deberia buscar los valores repetidos son:
```
'humidity','pressure','temperature','SPL','I_temperature','UV','CO_ug_m3','H2S_ug_m3','NO2_ug_m3','O3_ug_m3','PM1','PM10','PM25','SO2_ug_m3'
```
Se espera un output de la siguente manera:
```
'qHAWAX NOMBRE envió el mismo valor en un periodo de 5 min'
'Se congelaron los siguientes valores: {'contaminante': valor repetido}'
```
por ejemplo:
```
'qHAWAX qH004 envió el mismo valor en un periodo de 5 min'
'Se congelaron los siguientes valores: {'H2S_ug_m3': 526.36, 'I_temperature': 30.9, 'pressure': 997.759}'
```
Tiempo de desarrollo: 1 hora.
