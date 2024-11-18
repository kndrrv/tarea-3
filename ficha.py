from coordenada import Coordenada
from pieza_base import PiezaBase
from typing import List 

class Ficha(PiezaBase): # implementación de una ficha de damas
    
    def __init__(self, color: str, posicion: Coordenada): # constructor de la ficha, agrega el atributo es_dama además de los heredados
        super().__init__(color, posicion)
        self.es_dama = False
    
    def movimientos_posibles(self) -> List[Coordenada]:  # implementación de movimientos posibles para la ficha
        movimientos = [] # lista de coordenadas válidas
        direccion = 1 if self.color == "blanco" else -1
        
        if not self.es_dama:
            # movimientos básicos diagonales hacia adelante
            self._agregar_movimiento_diagonal(movimientos, direccion, 1)
            self._agregar_movimiento_diagonal(movimientos, direccion, -1)
        else:
            # movimientos en todas direcciones para damas
            for dir_fila in [-1, 1]:
                for dir_columna in [-1, 1]:
                    self._agregar_movimiento_diagonal(movimientos, dir_fila, dir_columna)
        
        return movimientos
    
    def puede_mover_a(self, nueva_posicion: Coordenada) -> bool: # verifica si la ficha puede moverse a la nueva posición
        return nueva_posicion in self.movimientos_posibles()
    
    def _agregar_movimiento_diagonal(self, movimientos: List[Coordenada], # método auxiliar para agregar movimientos diagonales válidos
                                   dir_fila: int, dir_columna: int) -> None:
        nueva_fila = self.posicion.fila + dir_fila
        nueva_columna = self.posicion.columna + dir_columna
        
        if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
            movimientos.append(Coordenada(nueva_fila, nueva_columna))