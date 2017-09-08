import copy

import numpy as np

import problema_espacio_estados as probee


class poner_pieza(probee.Acción):
    """Clase hija de Acción"""

    def __init__(self, nombre, posicion):
        self.posicion = posicion
        super().__init__(nombre=nombre)

    def es_aplicable(self, estado):
        """Un estado es aplicable si al realizar al suma no se obtiene ningun
        elemento de la matriz mayor a 1"""
        nuevo_estado = estado + self.posicion
        return not np.any(nuevo_estado[:, :] > 1)

    def aplicar(self, estado):
        """Se suman las matrices del estado actual y de la acción, obteniendo
        así el nuevo estado"""
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado += self.posicion
        return nuevo_estado


class ProblemaEspacioEstadosPentominos(probee.ProblemaEspacioEstados):
    """Clase hija de ProblemaEspacioEstados"""
    def __init__(self, acciones, estado_inicial=None, estados_finales=None):
        super().__init__(acciones, estado_inicial,
                         estados_finales)

    def es_estado_final(self, estado):
        """Un estado es final su el numero de casillas vacias es menor a 5"""
        filas, columnas = estado.shape
        return filas * columnas - np.sum(estado) < 5
