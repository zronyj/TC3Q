from sys import argv

pKa = {
	"G": [2.34,  9.58],
	"A": [2.33,  9.71],
	"V": [2.27,  9.52],
	"L": [2.32,  9.58],
	"I": [2.26,  9.60],
	"M": [2.16,  9.08],
	"P": [1.95, 10.47],
	"F": [2.18,  9.09],
	"W": [2.38,  9.34],
	"N": [2.16,  8.76],
	"Q": [2.18,  9.00],
	"S": [2.13,  9.05],
	"T": [2.20,  8.96],
	"C": [1.91, 10.28,  8.14, -1],
	"Y": [2.24,  9.04, 10.10, -1],
	"D": [1.95,  9.66,  3.71, -1],
	"E": [2.16,  9.58,  4.15, -1],
	"K": [2.15,  9.16, 10.67,  0],
	"R": [2.03,  9.00, 12.10,  0],
	"H": [1.70,  9.09,  6.04,  0]}

def get_charge(tabla, switch=0):
	carga = 0
	for i in range(len(tabla)):
		if tabla[i][0] < switch:
			carga += tabla[i][1]
		else:
			carga += tabla[i][1] + 1
	return carga

def probe_charge(tabla):
	for i in range(15):
		c = get_charge(tabla, i)
		if c == 0:
			for j in range(len(tabla)):
				if i < tabla[j][0]:
					return j-1
	raise ValueError("No se pudo hallar el punto isoelectrico.")

# Abriendo documento
nombre = argv[1]

with open(nombre,"r") as fastp:
	texto = fastp.readlines()

descripcion = texto[0]

# Ordenando datos
secuencia_aa = ""
for i in range(1, len(texto)):
	if (texto[i][-1] == "\n"):
		secuencia_aa += texto[i][:-1]
	else:
		secuencia_aa += texto[i][:]

# Sacando pKa de extremos N-terminal y C-terminal
iso = []
iso.append([pKa[secuencia_aa[0]][1],0])
iso.append([pKa[secuencia_aa[-1]][0],-1])

# Sacando pKa de cadenas laterales
for a in range(0,len(secuencia_aa)):
	if secuencia_aa[a] in "CYDEKRH":
		iso.append(pKa[secuencia_aa[a]][-2:])

# Eliminando duplicados
simple = []
for i in iso:
	if not( i in simple ):
		simple.append(i)

#Ordenando por pKa
simple.sort(key=lambda p: p[0])

# Hallando donde la carga es 0
indice = probe_charge(simple)

# Mostrando resultados
print( "pI = {:.4}".format((simple[indice][0] + simple[indice+1][0])/2))

print("\npKas:", end=" ")
for j in simple:
	print(j[0], end=" ")

print("\nKas:", end=" ")
for k in simple:
	print( "{:.4e}".format(10**(-1*k[0])), end=" ")

print("")