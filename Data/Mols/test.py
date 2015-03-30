import os
plantilla = """receptor = 1PXX.pdbqt
ligand = {0}.pdbqt
out = {0}.pdbqt
log = {0}.log
center x = 27
center y = 25
center z = 15
size x = 20
size y = 20
size z = 20
cpu = 2
exhaustiveness = 8
num modes = 10
energy range = 3"""
archivos = os.listdir(os.getcwd())
for mol in archivos:
	if mol[-4:] == "mol2":
		with open(mol[:-5] + ".conf", "w") as arch:
			arch.write(plantilla.format(mol[:-5]))