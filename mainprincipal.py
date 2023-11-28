# main.py

import pygame
import random
from plantas import Arbol, Arbusto, Flor, Hierba, Hongo
from animales import SimuladorAnimales

pygame.init()

ancho_pantalla = 1200
alto_pantalla = 800
tamaño_modulo = 40  

pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Bosque con Plantas")




bosque = [[random.choice([Arbol(x,y), Arbusto(x,y), Flor(x,y), Hierba(x,y), Hongo(x,y)]) for x in range(ancho_pantalla // tamaño_modulo)]
          for y in range(alto_pantalla // tamaño_modulo)]


fondo = pygame.Surface((ancho_pantalla, alto_pantalla))
fondo.fill((255, 255, 255)) 

ejecutando = True
reloj = pygame.time.Clock() 

simulador = SimuladorAnimales(pantalla, bosque, fondo)  

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False


    pantalla.blit(fondo, (0, 0))



    
    for fila in range(alto_pantalla // tamaño_modulo):
        for columna in range(ancho_pantalla // tamaño_modulo):
            bosque[fila][columna].dibujar(pantalla, columna, fila, tamaño_modulo)

    for fila in range(alto_pantalla // tamaño_modulo):
        for columna in range(ancho_pantalla // tamaño_modulo):
            bosque[fila][columna].interactuar()

    pygame.display.flip()

    reloj.tick(60)

    

    simulador.ejecutar_simulacion(pantalla)

pygame.quit()
