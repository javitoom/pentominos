import numpy as np

from pentomino import Pentomino


def heuristica_de_bordes_rango_y_casillas_vacias(nodo):
    """Damos preferencia a los tableros cuyo borde está ocupado por piezas.
    Tambien premiamos las matrices con menor rango y mayor numero de casillas
    ocupadas"""
    estado = nodo.estado
    # Calculamos "perimetro" ocupado de la matriz
    h = Pentomino.tablero_filas * 2 + (Pentomino.tablero_columnas - 2) * 2
    h -= np.sum(estado[:, 0])
    h -= np.sum(estado[:, Pentomino.tablero_columnas - 1])
    h -= np.sum(estado[0, 1:Pentomino.tablero_columnas - 1])
    h -= np.sum(
        estado[Pentomino.tablero_filas - 1, Pentomino.tablero_columnas - 1])
    # Calculamos el rango de la matriz
    rango = np.linalg.matrix_rank(estado)
    h += 3 * rango
    # Calculamos el numero de casillas vacias
    h += 2 * (
        Pentomino.tablero_filas * Pentomino.tablero_columnas - np.sum(estado))
    return h


def heuristica_de_rango_y_casillas_vacias(nodo):
    """Premiamos las matrices con menor rango y mayor numero de casillas
    ocupadas"""
    estado = nodo.estado
    # Calculamos el rango de la matriz
    h = 2 * np.linalg.matrix_rank(estado)
    # Calculamos el numero de casillas vacias
    h += Pentomino.tablero_filas * Pentomino.tablero_columnas - np.sum(estado)
    return h


def heuristica_de_penalizacion_I(nodo):
    """Castigamos el uso de la pieza que representa la letra I"""
    if (nodo.acción != None):
        posicion = nodo.acción.posicion
        rango = np.linalg.matrix_rank(posicion)
        if (rango == 1):
            return 5
    return 0


def heuristica_de_premiado_I(nodo):
    """Premiamos el uso de la pieza que representa la letra I"""
    if (nodo.acción != None):
        posicion = nodo.acción.posicion
        rango = np.linalg.matrix_rank(posicion)
        if (rango == 1):
            return 0
    return 5
