from tablas import *
f = open("Agua_Ati_20140224.csv")
datos = []
for linea in f.readlines():
    datos.append(linea)

datos2 = []
for entrada in datos:
    datos2.append(entrada.split(","))

for ultimo in datos2:
    ultimo[len(ultimo) - 1] = ultimo[len(ultimo) - 1][:-1]

tabla(datos2, True)
