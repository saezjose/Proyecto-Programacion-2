#-----------------------------#
# Integrantes del proyecto.   #
#                             #
# José Tomás Sáez Hermosilla. #
#                             #
# Lukas Escobar Quezada.      #
#                             #
#-----------------------------#



#  Importamos librerias necesarias para nuestra simulacion.

#------------------------------------------------------------------------------------------------------------


import pygame 
import random
from plantas import Arbol, Arbusto, Flor, Hierba, Hongo
from animales import SimuladorAnimales                                 #[Tenemos esto comentando por un experimento]


#------------------------------------------------------------------------------------------------------------



#Aca generamos variables establecemos el ancho y alto de nuestra ventana y nos crea el fondo  de nuestro bosque.

pygame.init()

ANCHO_PANTALLA = 1200
ALTO_PANTALLA = 800
TAMAÑO_MODULO = 40


pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Bosque con Plantas")


bosque = [
    [random.choice([Arbol(x,y), Arbusto(x,y), Flor(x,y), Hierba(x,y), Hongo(x,y)]) for x in range(ANCHO_PANTALLA // TAMAÑO_MODULO)]
    for y in range(ALTO_PANTALLA // TAMAÑO_MODULO)
]

fondo = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
fondo.fill((255, 255, 255))


simulador = SimuladorAnimales(pantalla, bosque, fondo)                    #[Tenemos esto comentando por un experimento]


ejecutando = True
reloj = pygame.time.Clock()



#------------------------------------------------------------------------------------------------------------

#Dentro de la matriz bosque agarra las filas y las columnas hace que llame el metodo deibujar de cada objeto."Plantas"
#Y la funcion interactuar Hace que interactue con el ambiente cambiando el estado de vivo a muelto.


def Dibujar_Bosque(): 
    for fila in range(ALTO_PANTALLA // TAMAÑO_MODULO):
            for columna in range(ANCHO_PANTALLA // TAMAÑO_MODULO):
                bosque[fila][columna].dibujar(pantalla, columna, fila, TAMAÑO_MODULO)


def Interactuar_Bosque():
     for fila in range(ALTO_PANTALLA // TAMAÑO_MODULO):
        for columna in range(ANCHO_PANTALLA // TAMAÑO_MODULO):
            bosque[fila][columna].interactuar()




#Con el ciclo while llamamos a las Funciones.

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.blit(fondo, (0, 0))

    Dibujar_Bosque()
   
    Interactuar_Bosque()

    simulador.ejecutar_simulacion(pantalla)                                    #[Tenemos esto comentando por un experimento]

    simulador.guardar_datos("datos_simulacion.txt")                             #[Tenemos esto comentando por un experimento]
    
    pygame.display.flip()

    reloj.tick(60)


pygame.quit()

#------------------------------------------------------------------------------------------------------------