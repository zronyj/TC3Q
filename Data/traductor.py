from sys import argv

tablacodon = {
	'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
	'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
	'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
	'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
	'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
	'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
	'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
	'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def translate(aminoacidos, inicio=0):
	prot = ""
	for c in xrange(inicio, len(aminoacidos)+3, 3):
		codon = aminoacidos[c:c+3]
		if codon in tablacodon.keys():
			prot += tablacodon[codon]
		else:
			print "Codon no reconocido:", codon
	return prot
	
nombre = argv[1]

with open(nombre,"r") as fastn:
	texto = fastn.readlines()

descripcion = texto[0]

secuencia_nu = ""
for i in xrange(1, len(texto)):
	secuencia_nu += texto[i][:-1]

secuencia_aa = translate(secuencia_nu)

formato = [secuencia_aa[frag:frag+70] + "\n" for frag in xrange(0, len(secuencia_aa)+70,70)]

nueva_descripcion = descripcion[0] + "Traduccion " + descripcion[1:]

with open("trad_" + nombre, "w") as fastp:
	fastp.writelines([nueva_descripcion])
	fastp.writelines(formato)
