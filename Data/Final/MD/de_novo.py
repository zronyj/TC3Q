with open("residuos.smiles", "r") as sonrisas:
	smiles = sonrisas.readlines()



explo = []
for s in smiles:
	for c in range(len(s)):
		if s[c] == "C":
			explo.append( s[:c+1] + "(N(=O)=O)" + s[c:] )

with open("nuevos.smiles","w") as risas:
	risas.writelines(explo)
