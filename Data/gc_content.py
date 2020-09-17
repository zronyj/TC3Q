from sys import argv

nombre = argv[1]

with open(nombre,"r") as fastn:
	texto = fastn.readlines()

descripcion = texto[0]

secuencia = ""
for i in xrange(1, len(texto)):
	secuencia += texto[i][:-1]

secuencia = secuencia.upper()

contenido_c = secuencia.count("C")
contenido_g = secuencia.count("G")

porcentaje = float(contenido_c + contenido_g) / len(secuencia) * 100

print "Contenido GC: {:.2}%".format(porcentaje)
