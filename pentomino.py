import copy

import numpy as np



class Pentomino:
    """Clase para almacenar en forma de variables estaticas el numero de
    filas y de columnas del tablero y las letras"""
    tablero_filas = 0
    tablero_columnas = 0
    letras = [
        np.array(p) for p in [

            # F
            [[0, 1, 1],
             [1, 1, 0],
             [0, 1, 0]],

            # I
            [[1, 1, 1, 1, 1]],

            # L
            [[1, 1, 1, 1],
             [0, 0, 0, 1]],

            # N
            [[1, 1, 0, 0],
             [0, 1, 1, 1]],

            # P
            [[1, 1, 1],
             [0, 1, 1]],

            # T
            [[1, 1, 1],
             [0, 1, 0],
             [0, 1, 0]],

            # U
            [[1, 0, 1],
             [1, 1, 1]],

            # V
            [[1, 0, 0],
             [1, 0, 0],
             [1, 1, 1]],

            # W
            [[1, 0, 0],
             [1, 1, 0],
             [0, 1, 1]],

            # X
            [[0, 1, 0],
             [1, 1, 1],
             [0, 1, 0]],

            # Y
            [[0, 0, 1, 0],
             [1, 1, 1, 1]],

            # Z
            [[1, 1, 0],
             [0, 1, 0],
             [0, 1, 1]]
        ]
    ]

def todas_las_orientaciones():
    """Genera las direfentes orientaciones de los pentominós,
    incluyendo rotaciones y reflecciones"""

    rotacionesObtenidas = set()
    piezas = []
    for i, letra in enumerate(Pentomino.letras):

        # Giramos arriba, abajo, izquierda y derecha en todas las combinaciones
        # para generar todas las posibles orientaciones del pentomino.
        for letra in (letra, letra.T):
            for letra in (letra, np.fliplr(letra)):
                for letra in (letra, np.flipud(letra)):
                    s = str(letra)
                    if not s in rotacionesObtenidas:
                        piezas.append(letra)
                        rotacionesObtenidas.add(s)
    return piezas

def todas_las_posiciones(piezas_con_orientaciones, tablero):
    """ Busca todas las posiciones donde poner el pentominó"""
    posiciones = []
    filas = Pentomino.tablero_filas + 1
    columnas = Pentomino.tablero_columnas + 1
    for pieza in piezas_con_orientaciones:
        pieza_filas, pieza_columas = pieza.shape
        for i in range(filas - pieza_filas):
            for j in range(columnas - pieza_columas):
                M = copy.deepcopy(tablero)
                M[i:i + pieza_filas, j:j + pieza_columas] += pieza
                posiciones.append(M)
    return posiciones