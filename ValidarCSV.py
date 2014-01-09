# ValidarCSV.py
# Python 3.3.3
# Author: Salva J. GB.
# Author_email: salvajgb@gmail.com
# Date: 19/12/2013
# Validador para la entrada de datos por fichero CSV al portal Casaktua


import csv, sys, os, math
import win32com.client    # Libreria para iMacros

os.chdir('c:/Python33/learning')

# TODO La carga de constantes debería realizarla a traves de un modulo aparte. (o por proceso de carga de fichero setup)

# Definicion de constantes e inicializacion de variables globales
ordenEncabezado = ['NULO',
                   'ACTIVO',
                   'COMUNIDAD_CIF',
                   'COMUNIDAD_CCC',
                   'COMUNIDAD_OBSER',
                   'IBI_EJERCICIO',
                   'IBI_OBSER',
                   'TITULARIDAD',
                   'CARTA_PAGO',
                   'AGENDA']

numeroEncabezados = len(ordenEncabezado) #numero de columnas de encabezados (10 por el momento)

matrizEncabezados = []  #inicializa la matriz contenedora de los encabezados encontrados


# Funcion AbrirFicheroCSV()
#   Abre el fichero 'datos.csv'
def AbrirFicheroCSV():
    global ficheroEntrada       # global para poder cerrarlo luego
    ficheroEntrada = open('datos.csv','r')
    lectorFicheroEntrada = csv.reader(ficheroEntrada, delimiter=';')
    return lectorFicheroEntrada


# Funcion CerrarCSV()
#   Cierra el fichero 'datos.csv'
def CerrarFicheroCSV():
    ficheroEntrada.close()
    return


# Funcion ExtraeEncabezados()
#   obtiene la primera fila del fichero CSV
def ExtraeEncabezados(lectorFicheroEntrada):
    for encabezado in lectorFicheroEntrada:
        # print(encabezado)
        break
    return encabezado
# TODO: esta funcion no es elegante, tengo que cambiarla

# Inicializar Matriz de posiciones matrizEncabezados de filas x 3 columnas con ceros.
# Luego carga la matriz con los siguientes datos
#   columna 1: numero de orden.
#   columna 2: nombre del dato.
#   columna 3: posicion en el CSV de entrada (ojo, la posicion 0 es la primera)
def IniciarMatriz():
    for i in range(0, numeroEncabezados):
        matrizEncabezados.append(['0'] * 3 )  # Se inicializa con los datos a 0

    for j in range(1, numeroEncabezados):
        matrizEncabezados[j][0] = j # el numero de la fila
        matrizEncabezados[j][1] = ordenEncabezado[j]
        if ordenEncabezado[j] in encabezado:
            matrizEncabezados[j][2] = encabezado.index(ordenEncabezado[j])
        else:
            matrizEncabezados[j][2] = 0
    return matrizEncabezados

# Para ver si en __main__
print(__name__)

# Lee primera fila del CSV y la carga en 'encabezado'
encabezado = ExtraeEncabezados(AbrirFicheroCSV())
CerrarFicheroCSV()

# Llama a la funcion cargadora de la matriz de posiciones.
matrizEncabezados = IniciarMatriz()

# Imprime el contenido de la matriz de posiciones.
for campo in range(1,numeroEncabezados):
    print(matrizEncabezados[campo][0], matrizEncabezados[campo][1], matrizEncabezados[campo][2])

# Imprime cada columna con su dato en el orden correcto.
lectorFicheroEntrada = AbrirFicheroCSV()
for linea in lectorFicheroEntrada:
    for numeroColumna in range(1,numeroEncabezados):
        print(matrizEncabezados[numeroColumna][1], '\t',      # Titulo de la columna
              linea[int(matrizEncabezados[numeroColumna][2])])      # Dato de la columna

