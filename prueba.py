from coordenada import Coordenada
from ficha import Ficha
from juego import General

# ejemplo de uso
def ejemplo_uso():
    try:
        # crear una ficha de damas
        ficha = Ficha("blanco", Coordenada(0, 1))
        print(f"Ficha creada: {ficha}")
        
        # ver sus movimientos posibles
        movimientos = ficha.movimientos_posibles()
        print("Movimientos posibles de la ficha:")
        for mov in movimientos:
            print(f"  - {mov}")
        
        # crear un general
        general = General("negro", Coordenada(0, 4))
        print(f"\nGeneral creado: {general}")
        
        # probar un movimiento
        nueva_pos = Coordenada(1, 4)
        if general.puede_mover_a(nueva_pos):
            print(f"El general puede moverse a {nueva_pos}")
        else:
            print(f"El general no puede moverse a {nueva_pos}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ejemplo_uso()