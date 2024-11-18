from coordenada import Coordenada
from pieza_base import PiezaBase
from typing import List

class General(PiezaBase): # implementación del general del xiangqi
    
    def movimientos_posibles(self) -> List[Coordenada]: # implementa los movimientos del General
        movimientos = [] # lista de movimientos válidos
        # Movimientos ortogonales (cruz)
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for dir_fila, dir_columna in direcciones:
            nueva_fila = self.posicion.fila + dir_fila
            nueva_columna = self.posicion.columna + dir_columna
            
            if self._esta_dentro_palacio(nueva_fila, nueva_columna):
                movimientos.append(Coordenada(nueva_fila, nueva_columna))
        
        return movimientos
    
    def puede_mover_a(self, nueva_posicion: Coordenada) -> bool: # verifica si el general se puede mover a la nueva posición
        return (self._esta_dentro_palacio(nueva_posicion.fila, nueva_posicion.columna) and
                nueva_posicion in self.movimientos_posibles())
    
    def _esta_dentro_palacio(self, fila: int, columna: int) -> bool: # verifica si la posición está dentro del palacio
        if self.color == "negro":
            return 0 <= fila <= 2 and 3 <= columna <= 5
        else:
            return 7 <= fila <= 9 and 3 <= columna <= 5
