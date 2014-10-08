def tabla(datos=[[0,0],[0,0]], tiene_titulos=False):
    titulos = "|"
    if tiene_titulos:
        segunda_linea = "|"
        tiene_segunda_linea = False
        for nombre in datos[0]:
            largo = len(nombre)
            if largo > 18:
                tiene_segunda_linea = True
                titulos += " " + nombre[:18] + " |"
                segunda_linea += " "*(37 - largo) + nombre[18:] + " |"
            else:
                titulos += " "*(19 - largo) + nombre + " |"
                segunda_linea += " "*19 + " |"
        print titulos
        if tiene_segunda_linea:
            print segunda_linea
        print "-"*len(segunda_linea)
        datos = datos[1:]
    else:
        print "-"*(21 * len(datos[0]) + 1)
    for linea in datos:
        fila = "|"
        for dato in linea:
            dato = str(dato)
            fila += " "*(19 - len(dato)) + dato + " |"
        print fila
