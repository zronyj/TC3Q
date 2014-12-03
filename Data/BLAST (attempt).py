
## Intento de un algoritmo tipo BLAST

#### Función para determinar el "score" de un segmento

def get_score(subject, query, subject_start, query_start, length):
    # Establecemos el score en 0
    score = 0
    # Recorremos las secuencias en un cierto numero de bases
    for i in xrange(length):
        # Averiguamos que base es la que toca en ambas secuencias
        subject_base = subject[subject_start + i]
        query_base = query[query_start + i]
        # Comparamos si la base es igual, sumamos 1, si no, restamos 1
        if subject_base == query_base:
            score += 1
        else:
            score -= 1
    return score


#### Función para dividir la secuencia en palabras de n letras

def splitter(sequence, word_length=3):
    # Inicializamos una lista donde van a ir todas las palabras
    words = []
    # Vamos recorriendo toda la secuencia
    for i in xrange(len(sequence) - word_length):
        # Agregamos los segmentos de secuencia como palabras a la lista
        words.append(sequence[i:i+word_length])
    return words


#### Buscador de palabras repetidas para hallar sus posiciones

def rank(words):
    # Creamos un diccionario para que cada palabra tenga su numero de posiciones
    diccionario = {}
    # Recorremos todas las palabras
    for i in words:
        # Definimos que cada palabra va a estar asociada a una lista
        diccionario[i] = []
        # Recorremos todas las palabras otra vez (buscando posiciones)
        for j in range(len(words)):
            # Si las palabras son iguales, agregamos la posicion a nuestro diccionario
            if i == words[j]:
                diccionario[i].append(j)
    # Recorremos todo el diccionario eliminando entradas dobles de las listas
    for k in diccionario:
        diccionario[k] = set(diccionario[k])
    return diccionario


#### Función para escoger las palabras con un número de entradas mayor o igual a m

def filtro(diccionario, entradas):
    # Nuevo diccionario para guardar las palabras con mas entradas
    new_diccionario = {}
    # Recorremos el diccionario original
    for k in diccionario:
        # Si la cantidad de entradas es mayor o igual al numero que propusimos ...
        if len(diccionario[k]) >= entradas:
            # ... incluir esa palabra en el nuevo diccionario.
            new_diccionario[k] = diccionario[k]
    return new_diccionario


#### Función para eliminar duplicados de una lista

def remove_duplicates(lista):
    # Creamos una lista nueva
    new_lista = []
    # Recorremos nuestra lista
    while len(lista) > 0:
        # Si el elemento en nuestra lista no esta en la lista nueva ...
        if lista[0] not in new_lista:
            # ... agregamos el elemento a la lista nueva.
            new_lista.append(lista[0])
        # Si el elemento estaba o no estaba en la lista nueva, igual hay que eliminarlo de nuestra lista
        lista = lista[1:]
    return new_lista


#### Función para escoger los segmentos con score arriba de x

def high_score(lista, high):
    # Creamos una lista en donde van a ir las posiciones a ser descartadas
    pos = []
    # Recorremos toda la lista buscando scores bajos
    for i in range(len(lista)):
        # Si el score es bajo, guardar la posicion
        if lista[i][2] < high:
            pos.append(i)
    # Recorremos la lista de posiciones en reversa ...
    for j in pos[::-1]:
        # ... y eliminamos las posiciones guardadas.
        lista.pop(j)
    return lista


#### Función para visualizar resultados

def visual(subject, query, match):
    largo = match[0][1] - match[0][0] + 2
    tab = len(str(max(match[0][0], match[1][0]))) + 1
    print "Referencia"
    print str(match[0][0]) + largo * " " + str(match[0][1])
    print " " * tab + subject[match[0][0]:match[0][1]]
    print " " * tab + query[match[1][0]:match[1][1]]
    print str(match[1][0]) + largo * " " + str(match[1][1])
    print "Consulta"


#### Algoritmo tipo BLAST

def BLAST(subject, query, word_length, entries, threshold):
    # Obtenemos las palabras significativas que vamos a usar para buscar
    query_words = filtro(rank(splitter(query, word_length)),entries)
    # Revisamos que nuestra secuencia de referencia tenga al menos una palabra igual a la de consulta
    control = 0
    for h in query_words:
        if h in subject:
            control += 1
    if control == 0:
        print "No se hallo ninguna similitud entre las secuencias"
        return None
    # Creamos una lista donde meter todos los segmentos que si son similares
    matches = []
    # Comenzamos con la busqueda: recorremos las palabras significativas
    for k in query_words:
        # Recorremos todas las posiciones en nuestra secuencia de referencia
        for i in xrange(len(subject)):
            # Si hallamos un segmento igual ...
            if k == subject[i:i+word_length]:
                for j in query_words[k]:
                    # ... establecemos limites de las secuencias ...
                    subject_limits = [i, i+word_length]
                    query_limits = [j, j+word_length]
                    score = get_score(subject, query, i, j, word_length)
                    palabra = word_length
                    inversor = 1
                    # ... y nos comenzamos a expander hacia ambos lados.
                    while True:
                        coef = (-1)**inversor
                        left_alive = True
                        right_alive = True
                        # Hacia la izquierda
                        if coef == -1:
                            if subject_limits[0] - 1 >= 0 and query_limits[0] - 1 >= 0 and left_alive:
                                if get_score(subject, query, subject_limits[0] - 1, query_limits[0] - 1, palabra + 1) >= threshold * (palabra + 1):
                                    subject_limits[0] -= 1
                                    query_limits[0] -= 1
                                    palabra += 1
                                else:
                                    break
                            else:
                                left_alive = False
                        # Hacia la derecha
                        else:
                            if subject_limits[1] + 1 < len(subject) and query_limits[1] + 1 < len(query) and right_alive:
                                if get_score(subject, query, subject_limits[0] + 1, query_limits[0] + 1, palabra + 1) >= threshold * (palabra + 1):
                                    subject_limits[1] += 1
                                    query_limits[1] += 1
                                    palabra += 1
                                else:
                                    break
                            else:
                                right_alive = False
                        inversor += 1
                        if not left_alive and not right_alive:
                            break
                    # Agregamos los segmentos prometedores con todo y score
                    score = get_score(subject, query, subject_limits[0], query_limits[0], palabra)
                    matches.append([subject_limits, query_limits, score])
    return matches


ref = 'actgatcgattgatcgatcgatcg'
cons = 'tttagatcgatctttgatc'
results = BLAST(ref, cons, 3, 1, 0.6)
results = remove_duplicates(results)
best_results = high_score(results, 5)
visual(ref, cons, best_results[7])
