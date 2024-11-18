from abc import ABC, abstractmethod # importamos lo necesario para clases abstractas
from coordenada import Coordenada # importamos la clase cooordenada
from typing import List  # para tipos de datos
    
class PiezaBase(ABC): # clase abstracta que define el comportamiento básico de una pieza

    def __init__(self, color: str, posicion: Coordenada): # contructor de la pieza base
        self.color = color # color de la pieza
        self.posicion = posicion # posición de lapieza
    
    @abstractmethod # método abstracto que se implementa en todas las piezas
    def movimientos_posibles(self) -> List[Coordenada]: # lista de posibles movimientos
        pass
    
    @abstractmethod # método abstracto para verificar si la pieza puede moverse a una posición
    def puede_mover_a(self, nueva_posicion: Coordenada) -> bool: # verifica si la pieza se puede mover a esa posición
        pass
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.color} en {self.posicion}"