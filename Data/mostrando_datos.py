# Importamos la funcion que deseamos
from tablas import *

# Abrimos el documento del que queremos sacar los datos
f = open("Agua_Ati_20140224.csv")

# Nos preparamos para recibir los datos en una lista
datos = []

# Leemos cada linea del documento y lo agregamos a la lista
for linea in f.readlines():
    datos.append(linea[:-1])

# Nos preparamos para recibir los datos ya procesados en una lista
datos2 = []

# Leemos cada elemento (cadena) de la lista anterior, y lo separamos (donde hay coma) por palabras
for entrada in datos:
    datos2.append(entrada.split(","))

# Visualizamos todos los datos que habia en el documento
tabla(datos2, True)
