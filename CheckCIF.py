#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Algoritmo de calculo y verificacion CIF personas juridicas
# en especial para las Comunidades de Propietarios

letras = "ABCDEFGHIJKLMNPQRSVW"

entradaCodigoCIF = input('Enter the VAT number: ')

def validarCodigoCIF(entrada):
    if len(entrada) != 9:
        return False
    # prefijo = entrada[:2]
    numero = entrada[1:10]
    pares = int(numero[1]) + int(numero[3]) + int(numero[5])
    impares = 0
    for i in range(0, 8, 2):
        j = int(numero[i]) * 2
        if j < 10:
            impares += j
        else:
            impares += j - 9
    # print(pares)
    # print(impares)
    digito = str(pares+impares)[-1]
    if int(digito) == 0:
        checkCIF = 0
    else:
        checkCIF = 10 - int(digito)
    # print(checkCIF)
    if str(checkCIF) == entrada[-1]:
        return True
    else:
        return False

print(validarCodigoCIF(entradaCodigoCIF))