import urllib2
import json
import pandas as pd

data = {}

def num_or_dump(x):
	try:
		t = float(x)
	except ValueError as e:
		t = -9999.
	return t

for a in range(2008,2018):
	d = urllib2.urlopen('http://api.wunderground.com/api/api-key/history_' + str(a) + '0601/q/MGGT.json')
	j = d.read()
	with open(str(a) + ".json","w") as f:
		f.write(j)
	pj = json.loads(j)
	temp = []
	ttime = []
	restantes = 24 - len(pj["history"]["observations"])
	for o in pj["history"]["observations"]:
		hora = int(o["date"]["hour"])
		if not(hora in ttime):
			ttime.append(hora)
			temp.append({"hora":hora,
				"temperatura":num_or_dump(o["tempm"]),
				"humedad":num_or_dump(o["hum"]),
				"presion":num_or_dump(o["pressurem"]),
				"lluvia":bool(int(o["rain"])),
				"visibilidad":num_or_dump(o["vism"])})
	totales = set(range(24))
	dados = set(ttime)
	restantes = list(totales.difference(dados))
	for i in restantes:
		temp.append({"hora":i,
			"temperatura":-9999.,
			"humedad":-9999.,
			"presion":-9999.,
			"lluvia":False,
			"visibilidad":-9999.})
	data[str(a)] = temp[:]
	d.close()

for p in ["temperatura", "humedad", "presion", "lluvia", "visibilidad"]:
	v = pd.DataFrame.from_dict({a:[t[v] for t in data[a]] for a in data.keys()})
	v.to_csv(p + ".csv")