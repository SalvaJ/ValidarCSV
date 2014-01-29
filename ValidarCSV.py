# ValidarCSV.py
# Python 3.3.3
# Author: Salva J. GB.
# Author_email: salvajgb@gmail.com
# Date: 19/12/2013
# Validador para la entrada de datos por fichero CSV al portal Casaktua


import csv
# import sys
# import os
import time
import logging
# import win32com.client    # Libreria para iMacros

# os.chdir('c:/Python33/learning')


# TODO La carga de constantes debería realizarla a traves de un modulo aparte.(o por proceso de carga de fichero setup)
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

#numero de columnas de encabezados (10 por el momento)
numeroEncabezados = len(ordenEncabezado)
#inicializa la matriz contenedora de los encabezados encontrados
matrizEncabezados = []


# Generar nombre de fichero con fecha y hora
# Formato: NOMBRE_AAAAMDHm.ext
# AAAA año
# M mes, enero es 1, no 01
# D día, 3, no 03
# H hora
# m minutos
# Args:
#       prefijo: (str), nombre inicial del fichero
#       extension: (str), extensión del fichero con el punto (ej. '.log'). Default '.txt'
# Returns:
#       nombreFichero: (str), con formato prefijo_AAAAMDHm.ext
def NombrarFicheroHora(prefijo, extension='.txt'):
    """
    :param prefijo: str
    :param extension: str
    :return nombre_fichero: str
    """
    nombre = prefijo
    tiempo = time.localtime(time.time())    # Objeto con atributos del día y la hora
    dia_hora = str(tiempo.tm_year)+str(tiempo.tm_mon)+str(tiempo.tm_mday)+str(tiempo.tm_hour)+str(tiempo.tm_min)
    nombre_fichero = nombre + '_' + dia_hora + extension
    return nombre_fichero


# Funcion AbrirFicheroCSV()
#   Abre el fichero 'datos.csv'
def AbrirFicheroCSV():
    """
    :return: :raise:
    """
    global ficheroEntrada       # global para poder cerrarlo luego
    try:
        ficheroEntrada = open('datos.csv','r')
    except:
        logging.error("Error al intentar abrir fichero: 'datos.csv")
        # TODO esto estaría mejor con decoradores de funciones.
        raise
    lectorFicheroEntrada = csv.reader(ficheroEntrada, delimiter=';')
    return lectorFicheroEntrada


# Funcion CerrarCSV()
#   Cierra el fichero 'datos.csv'
def CerrarFicheroCSV():
    """
    :return: :raise: 
    """
    try:
        ficheroEntrada.close()
    except:
        logging.error("Error al intentar cerrar fichero: 'datos.csv")
        # TODO esto estaría mejor con decoradores de funciones.
        raise
    return


# Funcion ExtraeEncabezados()
#   obtiene la primera fila del fichero CSV
def ExtraeEncabezados(lectorFicheroEntrada):
    """
    :param lectorFicheroEntrada: file
    :return encabezado: str
    """
    for encabezado in lectorFicheroEntrada:
        # print(encabezado)
        break
    return encabezado
# TODO: esta funcion no es elegante, tengo que cambiarla


# Validar los nombres de encabezados
def ValidarEncabezados(encabezado):
    """
    :param encabezado: str
    :return isOK: boolean
    """
    isOK = True
    if ordenEncabezado[1] not in encabezado:
        logging.warning('No hay ninguna columna llamada ACTIVO, (es obligatoria)')
        isOK = False
        return isOK
    elif len(list(encabezado)) < 2:
        logging.warning('Se necesitan al menos 2 columnas (ACTIVO y otra)')
        isOK = False
        return isOK
    for campo in encabezado:
        if campo in ordenEncabezado:
            logging.info("%s -> OK", campo)
        else:
            logging.warning("%s Título de columna INCORRECTO!!", campo)
            # TODO esto estaría mejor con decoradores de funciones.
            isOK = False
    return isOK


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

# Para ver si es __main__
print(__name__)

# Inicia el log a nivel de DEBUG (habrá que cambiarlo a INFO en producción)
nombreFicheroLog = NombrarFicheroHora('resultado', '.log')
logging.basicConfig(handlers=[logging.FileHandler(
    nombreFicheroLog, 'w', 'utf-8')], level=logging.DEBUG)

# Lee primera fila del CSV y la carga en 'encabezado'
encabezado = ExtraeEncabezados(AbrirFicheroCSV())
CerrarFicheroCSV()

if ValidarEncabezados(encabezado):
    logging.info(u'FASE FASE VALIDACIÓN TITULOS DE COLUMNAS DE DATOS -> OK')
    # Llama a la funcion cargadora de la matriz de posiciones.
    matrizEncabezados = IniciarMatriz()
    # Imprime el contenido de la matriz de posiciones.
    for campo in range(1,numeroEncabezados):
        print(matrizEncabezados[campo][0], matrizEncabezados[campo][1],
              matrizEncabezados[campo][2])
    # Imprime cada columna con su dato en el orden correcto.
    lectorFicheroEntrada = AbrirFicheroCSV()
    for linea in lectorFicheroEntrada:
        for numeroColumna in range(1,numeroEncabezados):
            print(matrizEncabezados[numeroColumna][1], '\t',      # Titulo de la columna
                  linea[int(matrizEncabezados[numeroColumna][2])])      # Dato de la columna
else:
    logging.warning(u'FASE VALIDACIÓN TITULOS DE COLUMNAS DE DATOS NO SUPERADA. compruebe los nombres de los títulos de las columnas en datos.csv)')
    # TODO esto estaría mejor con decoradores de funciones.
