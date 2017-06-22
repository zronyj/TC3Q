import os
import subprocess
aqui = os.getcwd()
lista = os.listdir(aqui)

for f in lista:
	try:
		nam, ext = f.split(".")
	except ValueError as e:
		nam = f
		ext = ""
	if ext == 'prmtop':
		print nam, ext,
		with open(nam + "_vmd_energy", "w") as energ:
			ene = """mol new {0}.prmtop
mol addfile {0}.inpcrd type rst7 top
mol addfile {1}/{0}/{0}.dcd waitfor -1 top
set sel1 [atomselect top "not waters"]
package require namdenergy
namdenergy -all -sel $sel1 -ofile {0}.dat -tempname {0} -extsys {1}/{0}/{0}.xsc -pme 
mol delete top
quit""".format(nam, aqui)
			energ.write(ene)
		confirm = subprocess.check_output(["vmd","-dispdev","text","-e",nam + "_vmd_energy"])
		os.remove(nam + "_vmd_energy")
		print " finished!"
