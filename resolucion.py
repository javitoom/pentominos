import time

import búsqueda_espacio_estados as busqee
import heuristica
import problema_espacio_estados_pentominos as probeep
from pentomino import *

#Introducción de datos por consola
num_filas = int(input('Número de filas: '))
num_columnas = int(input('\nNúmero de columnas: '))
detallado = input('\nDetallado (s/n):') == 's'

Pentomino.tablero_filas = num_filas
Pentomino.tablero_columnas = num_columnas

#Creación del estado inicial como una matriz con todos sus valores a cero
estado_inicial = np.zeros(
    (Pentomino.tablero_filas, Pentomino.tablero_columnas),
    dtype=int)

#Obtención de todas las rotaciones de las letras
piezas_con_orientacion = todas_las_orientaciones()

#Obtención de todas las posiciones que puede ocupar cada letra en el tablero
posiciones = todas_las_posiciones(piezas_con_orientacion, estado_inicial)

#Creación de todas las acciónes posibles
acciones = [probeep.poner_pieza(posicion, posicion) for posicion in
            posiciones]
problema_pentominos = probeep.ProblemaEspacioEstadosPentominos(acciones,
                                                               estado_inicial)

while True:
    # ALGORITMOS DE BUSQUEDA
    opcion = int(input(
        '\nSeleccione algoritmo de búsqueda\n' +
        '{0: Búsqueda A*,\n'
        '1: BúsquedaEnAnchura,\n'
        '2: BúsquedaEnProfundidad,\n'
        '3: BúsquedaEnProfundidadAcotada,\n'
        '4: BúsquedaEnProfundidadIterativa,\n'
        '5: BúsquedaPrimeroElMejor,\n'
        '6: BúsquedaÓptima}\n'
        'Cualquier otro parámetro para salir: '))

    if opcion == 0:
        seleccion_heuristica = int(
            input('\nSeleccione heuristica\n' +
                  '0: heurística de bordes y rango,\n'
                  '1: heurística de penalización I,\n'
                  '2: heurística de rango,\n'
                  '3: heurística de premiado I,\n'
                  'Cualquier otro parámetro para salir: '))
        if seleccion_heuristica == 0:
            busqueda = busqee.BúsquedaAEstrella(detallado=detallado,
                                                h=heuristica.heuristica_de_bordes_rango_y_casillas_vacias)
        elif seleccion_heuristica == 1:
            busqueda = busqee.BúsquedaAEstrella(detallado=detallado,
                                                h=heuristica.heuristica_de_penalizacion_I)
        elif seleccion_heuristica == 2:
            busqueda = busqee.BúsquedaAEstrella(detallado=detallado,
                                                h=heuristica.heuristica_de_rango_y_casillas_vacias)
        elif seleccion_heuristica == 3:
            busqueda = busqee.BúsquedaAEstrella(detallado=detallado,
                                                h=heuristica.heuristica_de_premiado_I)
        else:
            break
    elif opcion == 1:
        busqueda = busqee.BúsquedaEnAnchura(detallado=detallado)
    elif opcion == 2:
        busqueda = busqee.BúsquedaEnProfundidad(detallado=detallado)
    elif opcion == 3:
        cota = int(input('Introduce cota:'))
        busqueda = busqee.BúsquedaEnProfundidadAcotada(detallado=detallado,
                                                       cota=cota)
    elif opcion == 4:
        cota = int(input('Introduce cota:'))
        busqueda = busqee.BúsquedaEnProfundidadIterativa(detallado=detallado,
                                                         cota_final=cota)
    elif opcion == 5:
        seleccion_heuristica = int(
            input('\nSeleccione heuristica\n' +
                  '0: heurística de bordes y rango,\n'
                  '1: heurística de penalización I,\n'
                  '2: heurística de rango,\n'
                  '3: heurística de premiado I,\n'
                  'Cualquier otro parámetro para salir: '))
        if seleccion_heuristica == 0:
            busqueda = busqee.BúsquedaPrimeroElMejor(detallado=detallado,
                                                     h=heuristica.heuristica_de_bordes_rango_y_casillas_vacias)
        elif seleccion_heuristica == 1:
            busqueda = busqee.BúsquedaPrimeroElMejor(detallado=detallado,
                                                     h=heuristica.heuristica_de_penalizacion_I)
        elif seleccion_heuristica == 2:
            busqueda = busqee.BúsquedaPrimeroElMejor(detallado=detallado,
                                                h=heuristica.heuristica_de_rango_y_casillas_vacias)
        elif seleccion_heuristica == 3:
            busqueda = busqee.BúsquedaPrimeroElMejor(detallado=detallado,
                                                h=heuristica.heuristica_de_premiado_I)
        else:
            break
    elif opcion == 6:
        busqueda = busqee.BúsquedaÓptima()
    else:
        break

    # Buscamos la solución al problema y medimos el tiempo necesitado
    tiempoActual = time.time()
    solucion = busqueda.buscar(problema_pentominos)
    duracion = time.time() - tiempoActual
    if (int(duracion) > 0):
        print(int(duracion), 'segundos')
    else:
        print(duracion, 'segundos')

    # Pintamos el tablero, cada pieza es representada por numeros
    table = np.zeros(
        (Pentomino.tablero_filas,
         Pentomino.tablero_columnas),
        dtype=int)
    i = 0
    for s in solucion:
        i += 1
        table += i * s
    print('\nSolución:\n')
    print(table)
    print()
