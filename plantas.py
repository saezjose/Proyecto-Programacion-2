# plantas.py
import pygame

tamaño_modulo = 40

class Planta:
    def __init__(self, imagen):
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, superficie, x, y, tamaño_modulo):
        superficie.blit(self.imagen, (x * tamaño_modulo, y * tamaño_modulo))

    def interactuar(self, bosque, fila, columna):
        # Lógica de interacción genérica, puedes cambiarla según tus necesidades
        print(f"Interacción genérica en {fila}, {columna}")

class Arbol(Planta):
    def __init__(self):
        super().__init__('imgplantas/arbol.png')

    def interactuar(self, bosque, fila, columna):
        # Lógica de interacción específica para el árbol
        print(f"El árbol en {fila}, {columna} interactúa cambiando a Hierba")
        bosque[fila][columna] = Hierba()

class Arbusto(Planta):
    def __init__(self):
        super().__init__('imgplantas/arbusto.png')

    def interactuar(self, bosque, fila, columna):
        # Lógica de interacción específica para el arbusto
        print(f"El arbusto en {fila}, {columna} interactúa cambiando a Hierba")
        bosque[fila][columna] = Hierba()

class Flor(Planta):
    def __init__(self):
        super().__init__('imgplantas/flor.png')

    def interactuar(self, bosque, fila, columna):
        # Lógica de interacción específica para la flor
        print(f"La flor en {fila}, {columna} interactúa cambiando a Hierba")
        bosque[fila][columna] = Hierba()

class Hierba(Planta):
    def __init__(self):
        super().__init__('imgplantas/hierba.png')

class Hongo(Planta):
    def __init__(self):
        super().__init__('imgplantas/hongo.png')

    def interactuar(self, bosque, fila, columna):
        # Lógica de interacción específica para el hongo
        print(f"El hongo en {fila}, {columna} interactúa cambiando a Hierba")
        bosque[fila][columna] = Hierba()
