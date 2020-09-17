import math, random

# Clase del objeto particula
class Particle(object):

	""" Inicializamos estableciendo numero de dimensiones
	y si la particula esta dentro de los limites """
	def __init__(self, lims, func):
		try:
			self.coords = []
			self.limits = lims
			self.eval = func
			dims = len(lims)
			for i in xrange(dims):
				lower, upper = lims[i][0], lims[i][1]
				diff = upper - lower
				if diff < 0:
					raise Exception("Limits are wrong.")
				self.coords.append(lower + diff * random.random())
			self.value = self.eval(self.coords)
		except Exception as err:
			print err
			return None

	""" Creamos un metodo para poder visualizar la
	informacion de la particula """
	def __repr__(self):
		output = "Value: " + str(self.value) + "\n"
		for i in xrange(len(self.coords)):
			output += "q(" + str(i+1) + ") = " + str(self.coords[i]) + " ... " + str(self.limits[i]) + "\n"
		return output

	""" Metodo para generar coordenadas nuevas aleatorias """
	def new_coordinates(self):
		ctrl = []
		for i in xrange(len(self.coords)):
			ctrl.append(-1 + 2 * random.random())
		return ctrl

	""" Metodo para evaluar si las coordenadas nuevas
	estan dentro de los limites, y de ser asi, mover
	a la particula a esas coordenadas """
	def update_coordinates(self, new_coords):
		if len(new_coords) == len(self.coords):
			for i in xrange(len(self.coords)):
				self.coords[i] = new_coords[i]
			self.value = self.eval(self.coords)
		else:
			raise IndexError("Dimensions of vectors are not the same.")

# Funcion para sumar vectores
def vect_add(vo, vf):
	nv = []
	for i in xrange(len(vf)):
		nv.append(vf[i] + vo[i])
	return nv

# Funcion para restar vectores
def vect_sub(vo, vf):
	nv = []
	for i in xrange(len(vf)):
		nv.append(vf[i] - vo[i])
	return nv

# Funcion para multiplicar un vector por un escalar
def scalar_mul(s, v):
	nv = []
	for i in xrange(len(v)):
		nv.append(s * v[i])
	return nv

# Algoritmo de anillamiento simulado
@profile
def simulated_annealing(parts, lim, tempi, steps, optfunc, temp_prog=0):
	particles = []
	temp_funt = []
	# Funciones para disminuir la temperatura
	const1 = steps / math.log(tempi + 1.0)
	const2 = float(tempi) / steps ** 2
	const3 = - tempi / float(steps)
	temp_funt.append( lambda t: math.e ** (- (t - steps) / const1) - 1 )
	temp_funt.append( lambda t: const2 * (t - steps) ** 2 )
	temp_funt.append( lambda t: const3 * t + tempi )
	# Archivo en el que se guardara el camino
	# recorrido por cada particula
	f = open("path.pth", "w")
	f.writelines("Path of the particles.\n")
	f.close()
	# Probando funcion de enfriamiento
	try:
		cooling = temp_funt[temp_prog]
	except IndexError as err:
		print err
		return None
	# Creando particulas
	for i in xrange(parts):
		particles.append(Particle(lim, optfunc))
	# Moviendo particulas
	for j in xrange(steps):
		f = open("path.pth", "a")
		for k in xrange(parts):
			# Escribiendo posicion de la particula
			f.writelines("p(" + str(k) + ") : " + str(particles[k].coords) + " - " + str(particles[k].value) + "\n")
			# Generando coordenadas nuevas
			v = particles[k].new_coordinates()
			# Generando nueva posicion en base a coordenadas nuevas
			u = vect_add(particles[k].coords, scalar_mul(cooling(j) / tempi, v))
			control = 0
			# Evaluacion si las coordenadas estan dentro de los limites
			for l in range(len(u)):
				if u[l] < lim[l][0] or u[l] > lim[l][1]:
					control += 1
			# Evaluacion de las coordenadas nuevas
			if control == 0:
				energ = optfunc(u) # Calculando la energia
				# Si la energia es mas baja, se aceptan las nuevas coordenadas
				if energ < particles[k].value:
					particles[k].update_coordinates(u)
				# Si la energia no es mas baja, se somete a jucio si aceptarlas
				elif energ >= particles[k].value:
					cte = math.e ** (- (energ - particles[k].value) * tempi / cooling(j))
					if cte >= random.random() and cte < 1:
						particles[k].update_coordinates(u)
		f.close()
	# Imprimir coordenadas finales y energia obtenida
	for m in particles:
		print "---------------------------\n", m
	return particles

# Funcion de prueba
fv = lambda v: (v[0] - 11.2)**2 + (v[1] + 15.3)**2

# Corrida del algoritmo
simulated_annealing(4, [[0,15],[-20,0]], 100, 100000, fv, 0)