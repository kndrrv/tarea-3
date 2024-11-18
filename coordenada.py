from dataclasses import dataclass# para crear clases de datos más simples
from typing import Tuple # para tipos de datos

@dataclass # usamos dataclass para la coordenada ya que es una clase simple de datos
class Coordenada: # clase para representar una posición en el tablero
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def __str__(self) -> str: # represenatción en texto de la coordenada
        return f"({self.fila}, {self.columna})"
    
    def obtener_posicion(self) -> Tuple[int, int]: # retorna la posición como una tupla
        return (self.fila, self.columna)