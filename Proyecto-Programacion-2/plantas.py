# plantas.py
import pygame
import random as Ra

tamaño_modulo = 40

ARCHIVO = "capturadora_eventos.txt"

#------------------------------------------------------------------------------------------------------------

# Se crea una clase Padre que se llama planta que se encarga de la simulacion general de las plantas ya sea dibujar las plantas en el entorno asi como su ciclo de vida y muerte.

class Planta:
    def __init__(self, estados = 1, imagen = None, vida_max = 100):
        self.estados = estados
        self.imagen = pygame.image.load(imagen) if imagen else None
        self.vida_max = vida_max
        self.vida = vida_max


    def dibujar(self, superficie, x, y, tamaño_modulo):
        if self.imagen:
            superficie.blit(self.imagen, (x * tamaño_modulo, y * tamaño_modulo))

    def interactuar(self):
        if self.estados == 1:
            self.vida -= Ra.uniform(0.001, 0.1)
            if self.vida <= 0:
                self.morir()
        elif self.estados == 0:
            self.vida += Ra.uniform(0.001, 0.1)
            if self.vida >= self.vida_max:
                self.revivir()

    def guardar_datos_plantas(self,archivo, estado,x,y):
        if estado == 1:
            estado_planta = "viva"
        elif estado == 0:
            estado_planta = "muelta"
        with open(archivo, 'a') as file:
            file.write(f"Planta posicion ({x}, {y}) Estado: {estado_planta}\n")


    def morir(self, imagen_muerta=None):
        if imagen_muerta:
            self.imagen = pygame.image.load(imagen_muerta)
        self.estados = 0
        self.guardar_datos_plantas(ARCHIVO, self.estados, self.x, self.y)

    def revivir(self, imagen_viva=None):
        if imagen_viva:
            self.imagen = pygame.image.load(imagen_viva)
        self.estados = 1
        self.guardar_datos_plantas(ARCHIVO, self.estados, self.x, self.y)

#------------------------------------------------------------------------------------------------------------

# Son subclases o clase hijo que se encarga de importar las imagenes de cada planta para poder dibujarlas en pantalla

class Arbol(Planta):
    def __init__(self, x, y):
        super().__init__(estados = 1, imagen='imgplantas/arbol.png', vida_max = (Ra.randint(4, 10) * 100))
        self.x = x
        self.y = y

    def morir(self):
        super().morir(imagen_muerta='imgplantas/arbolmuerto.png')

    def revivir(self):
        super().revivir(imagen_viva='imgplantas/arbol.png')

#------------------------------------------------------------------------------------------------------------

class Arbusto(Planta):
    def __init__(self, x, y):
        super().__init__(estados = 1, imagen='imgplantas/arbusto.png', vida_max = (Ra.randint(4, 10) * 10))
        self.x = x
        self.y = y

    def morir(self):
        super().morir(imagen_muerta='imgplantas/arbustomuerto.png')

    def revivir(self):
        super().revivir(imagen_viva='imgplantas/arbusto.png')

#------------------------------------------------------------------------------------------------------------

class Flor(Planta):
    def __init__(self, x, y):
        super().__init__(estados = 1, imagen='imgplantas/flor.png', vida_max = (Ra.randint(5, 6) * 10))
        self.x = x
        self.y = y

    def morir(self):
        super().morir(imagen_muerta='imgplantas/flormuerta.png')

    def revivir(self):
        super().revivir(imagen_viva='imgplantas/flor.png')

#------------------------------------------------------------------------------------------------------------

class Hierba(Planta):
    def __init__(self, x, y):
        super().__init__(estados=1, imagen='imgplantas/hierba.png', vida_max = 10)
        self.x = x
        self.y = y

    def morir(self):
        super().morir()  # No hay imagen diferente para la hierba muerta

    def revivir(self):
        super().revivir()  # No hay imagen diferente para la hierba viva

#------------------------------------------------------------------------------------------------------------

class Hongo(Planta):
    def __init__(self, x, y):
        super().__init__(estados=1, imagen='imgplantas/hongo.png', vida_max = (Ra.randint(4, 8) * 10))
        self.x = x
        self.y = y

    def morir(self):
        super().morir(imagen_muerta='imgplantas/hongomuerto.png')

    def revivir(self):
        super().revivir(imagen_viva='imgplantas/hongo.png')

#------------------------------------------------------------------------------------------------------------