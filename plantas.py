# plantas.py
import pygame
import random as Ra

tamaño_modulo = 40

class Planta:
    def __init__(self, imagen, vida_max=100, estados=1):
        self.estados = estados
        self.imagen = pygame.image.load(imagen)
        self.vida_max = vida_max
        self.vida = vida_max

    def dibujar(self, superficie, x, y, tamaño_modulo):
        superficie.blit(self.imagen, (x * tamaño_modulo, y * tamaño_modulo))

    def interactuar(self):
        if self.estados == 1:
            self.vida -= Ra.uniform(0.1, 2)
            if self.vida <= 0:
                self.morir()
                self.estados = 0
        elif self.estados == 0:
            self.vida += Ra.uniform(0.1, 2)
            if self.vida >= self.vida_max:
                self.revivir()
                self.estados = 1

    def morir(self):
        pass  # La implementación específica se realizará en las subclases

    def revivir(self):
        pass  # La implementación específica se realizará en las subclases

class Arbol(Planta):
    def __init__(self):
        super().__init__('imgplantas/arbol.png', vida_max=150, estados=1)

    def morir(self):
        self.imagen = pygame.image.load('imgplantas/arbolmuerto.png')
    
    def revivir(self):
        self.imagen = pygame.image.load('imgplantas/arbol.png')

class Arbusto(Planta):
    def __init__(self):
        super().__init__('imgplantas/arbusto.png', vida_max=100, estados=1)

    def morir(self):
        self.imagen = pygame.image.load('imgplantas/arbustomuerto.png')

    def revivir(self):
        self.imagen = pygame.image.load('imgplantas/arbusto.png')

class Flor(Planta):
    def __init__(self):
        super().__init__('imgplantas/flor.png', vida_max=50, estados=1)

    def morir(self):
        self.imagen = pygame.image.load('imgplantas/flormuerta.png')

    def revivir(self):
        self.imagen = pygame.image.load('imgplantas/flor.png')

class Hierba(Planta):
    def __init__(self):
        super().__init__('imgplantas/hierba.png', vida_max=10, estados=1)

    def morir(self):
        self.imagen = pygame.image.load('imgplantas/hierba.png')
    
    def revivir(self):
        self.imagen = pygame.image.load('imgplantas/hierba.png')

class Hongo(Planta):
    def __init__(self):
        super().__init__('imgplantas/hongo.png', vida_max=80, estados=1)

    def morir(self):
        self.imagen = pygame.image.load('imgplantas/hongomuerto.png')

    def revivir(self):
        self.imagen = pygame.image.load('imgplantas/hongo.png')
