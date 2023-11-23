# main.py

import pygame
import random
from plantas import Arbol, Arbusto, Flor, Hierba, Hongo

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ancho_pantalla = 1200
alto_pantalla = 800
tamaño_modulo = 40  # Ajustado a 40 píxeles

# Crear la pantalla
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Bosque con Plantas")

# Crear una matriz de plantas en el bosque
bosque = [[random.choice([Arbol(), Arbusto(), Flor(), Hierba(), Hongo()]) for _ in range(ancho_pantalla // tamaño_modulo)] 
        for _ in range(alto_pantalla // tamaño_modulo)]



# Definir el fondo (puedes cambiarlo según tus necesidades)
fondo = pygame.Surface((ancho_pantalla, alto_pantalla))
fondo.fill((255, 255, 255))  # Rellena el fondo con blanco (puedes cambiarlo según tus necesidades)

# Bucle principal
ejecutando = True
reloj = pygame.time.Clock()  # Crear un objeto Clock

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Dibujar el fondo en la pantalla
    pantalla.blit(fondo, (0, 0))


    # Dibujar el bosque en la pantalla
    for fila in range(alto_pantalla // tamaño_modulo):
        for columna in range(ancho_pantalla // tamaño_modulo):
            bosque[fila][columna].dibujar(pantalla, columna, fila, tamaño_modulo)

    # Interactuar y reducir la vida de cada planta en el bosque
    for fila in range(alto_pantalla // tamaño_modulo):
        for columna in range(ancho_pantalla // tamaño_modulo):
            bosque[fila][columna].interactuar()


    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la tasa de frames a 60 por segundo
    reloj.tick(60)

# Salir de Pygame
pygame.quit()