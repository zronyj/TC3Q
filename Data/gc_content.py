from sys import argv
import fpformat

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

bonito = fpformat.fix( porcentaje , 2)

print "Contenido GC:", bonito + "%"
