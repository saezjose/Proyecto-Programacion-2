#------------------------------------------------------------------------------------------------------------
from tkinter import Canvas, Tk
import pygame as pg
import random
import math
import os

ANCHO, ALTO = 1200, 800
TAMANO_CELDA = 40
DISTANCIA_CAZA = 1
CICLOS_REPRODUCCION = 50


#------------------------------------------------------------------------------------------------------------

class Organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad
        self.ciclos_reproduccion = 0

    def moverse(self, direccion):
        dx, dy = direccion
        x, y = self.posicion
        nueva_x = x + dx
        nueva_y = y + dy

        nueva_x %= ANCHO // TAMANO_CELDA
        nueva_y %= ALTO // TAMANO_CELDA

        self.posicion = (nueva_x, nueva_y)

    def reproducirse(self):
        self.ciclos_reproduccion += 1
        if self.ciclos_reproduccion >= CICLOS_REPRODUCCION:
            self.ciclos_reproduccion = 0
            return True
        return False

    def envejecer(self):
        self.vida -= 1
        if self.vida <= 0:
            return True
        return False

#------------------------------------------------------------------------------------------------------------


class Presa(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, imagen_path):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta
        self.imagen_path = imagen_path
        self.imagen = pg.image.load(imagen_path).convert_alpha()
        self.imagen = pg.transform.scale(self.imagen, (TAMANO_CELDA, TAMANO_CELDA))

    def moverse_aleatoriamente(self, entorno):
        direcciones_posibles = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        direccion = random.choice(direcciones_posibles)
        self.moverse(direccion)


class Depredador(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, imagen_path):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta
        self.imagen_path = imagen_path
        self.imagen = pg.image.load(imagen_path).convert_alpha()
        self.imagen = pg.transform.scale(self.imagen, (TAMANO_CELDA, TAMANO_CELDA))
        self.ciclos_vida = 0
        self.max_ciclos_vida = random.randint(100, 500) 
        self.ciclos_desde_ultima_muerte = 0
        self.muerte_anunciada = False

    def cazar(self, presa):
        probabilidad_exito = random.uniform(0, 1)

        if probabilidad_exito > 0.5:
            self.energia += presa.energia
            presa.vida = 0
            mensaje = f"{self.especie} ha cazado con éxito a {presa.especie} y ha ganado energía."
        else:
            mensaje = f"{self.especie} ha fallado en la caza."

        print(mensaje)

    def explorar(self, entorno):
        direcciones_posibles = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        direccion = random.choice(direcciones_posibles)
        self.moverse(direccion)

    def moverse_aleatoriamente(self, entorno):
        direcciones_posibles = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        direccion = random.choice(direcciones_posibles)
        self.moverse(direccion)

    def envejecer_y_morir(self):
        self.ciclos_vida += 1
        self.ciclos_desde_ultima_muerte += 1

        if self.ciclos_vida >= self.max_ciclos_vida:
            if not self.muerte_anunciada:
                mensaje_muerte = f"{self.especie} ha envejecido y muerto. Ciclos restantes: {self.max_ciclos_vida - self.ciclos_vida}"
                print(mensaje_muerte)
                self.muerte_anunciada = True  
            return True

        return False
    

#------------------------------------------------------------------------------------------------------------



class Leon(Depredador):
    def __init__(self, posicion):
        super().__init__(posicion, vida=100, energia=70, velocidad=random.uniform(0.001, 0.005),
                         especie="Leon", dieta="Carnívoro", imagen_path="depredadoresimg/leon.png")
        


class Hiena(Depredador):
    def __init__(self, posicion):
        super().__init__(posicion, vida=100, energia=70, velocidad=random.uniform(0.01, 0.01),
                         especie="Hiena", dieta="Carnívoro", imagen_path="depredadoresimg/hiena.png")


class Zorro(Depredador):
    def __init__(self, posicion):
        super().__init__(posicion, vida=100, energia=70, velocidad=random.uniform(0.01, 0.01),
                         especie="Zorro", dieta="Carnívoro", imagen_path="depredadoresimg/zorro.png")


class Oso(Depredador):
    def __init__(self, posicion):
        super().__init__(posicion, vida=100, energia=70, velocidad=random.uniform(0.01, 0.01),
                         especie="Oso", dieta="Carnívoro", imagen_path="depredadoresimg/oso.png")


class Aguila(Depredador):
    def __init__(self, posicion):
        super().__init__(posicion, vida=100, energia=70, velocidad=random.uniform(0.01, 0.01),
                         especie="Aguila", dieta="Carnívoro", imagen_path="depredadoresimg/aguila.png")
        


class Gacela(Presa):
    def __init__(self, posicion):
        super().__init__(posicion, vida=80, energia=50, velocidad=random.uniform(0.01, 0.2),
                         especie="Gacela", dieta="Herbívoro", imagen_path="presasimg/antilope.png")


class Conejo(Presa):
    def __init__(self, posicion):
        super().__init__(posicion, vida=80, energia=50, velocidad=random.uniform(0.1, 1.0),
                         especie="Conejo", dieta="Herbívoro", imagen_path="presasimg/conejo.png")


class Ciervo(Presa):
    def __init__(self, posicion):
        super().__init__(posicion, vida=80, energia=50, velocidad=random.uniform(0.1, 0.5),
                         especie="Ciervo", dieta="Herbívoro", imagen_path="presasimg/ciervo.png")


class Cebra(Presa):
    def __init__(self, posicion):
        super().__init__(posicion, vida=80, energia=50, velocidad=random.uniform(0.1, 0.5),
                         especie="Cebra", dieta="Herbívoro", imagen_path="presasimg/cebra.png")


class Antilope(Presa):
    def __init__(self, posicion):
        super().__init__(posicion, vida=80, energia=50, velocidad=random.uniform(0.1, 0.5),
                         especie="Antilope", dieta="Herbívoro", imagen_path="presasimg/gacela.png")




#------------------------------------------------------------------------------------------------------------





#------------------------------------------------------------------------------------------------------------



class SimuladorAnimales:
    def __init__(self, pantalla, bosque, ventana):
        self.pantalla = pantalla
        self.bosque = bosque
        self.reloj = pg.time.Clock()

        self.dia = True 
        self.tiempo_cambio = 24  
        self.ciclos_transcurridos = 0 

        self.ventana = pg.display.set_mode((ANCHO, ALTO))
        

        self.entorno = [[None for _ in range(ANCHO // TAMANO_CELDA)] for _ in range(ALTO // TAMANO_CELDA)]

        self.comidas = []

       
        self.depredadores = self.generar_animales_aleatorios(Leon, 2, 2) + \
                            self.generar_animales_aleatorios(Hiena, 2, 3) + \
                            self.generar_animales_aleatorios(Zorro, 2, 5) + \
                            self.generar_animales_aleatorios(Oso, 2, 2) + \
                            self.generar_animales_aleatorios(Aguila, 2, 4)

       
        self.presas = self.generar_animales_aleatorios(Gacela, 2, 3) + \
                      self.generar_animales_aleatorios(Conejo, 2, 8) + \
                      self.generar_animales_aleatorios(Ciervo, 2, 4) + \
                      self.generar_animales_aleatorios(Cebra, 2, 3) + \
                      self.generar_animales_aleatorios(Antilope, 2, 3)
        

    def guardar_datos(self, archivo):
        with open(archivo, 'w') as file:
            file.write(f"Estado: {'Dia' if self.dia else 'Noche'}\n\n")

            file.write("Depredadores:\n")
            for depredador in self.depredadores:
                file.write(f"{depredador.especie} - Posicion: {depredador.posicion}, Vida: {depredador.vida}, Energia: {depredador.energia}\n")

            file.write("\nPresas:\n")
            for presa in self.presas:
                file.write(f"{presa.especie} - Posicion: {presa.posicion}, Vida: {presa.vida}, Energia: {presa.energia}\n")

                    

        

    def generar_animales_aleatorios(self, tipo_animal, min_cantidad, max_cantidad):
        cantidad = random.randint(min_cantidad, max_cantidad)
        animales = [tipo_animal(posicion=(random.randint(0, ANCHO // TAMANO_CELDA - 1),
                                          random.randint(0, ALTO // TAMANO_CELDA - 1))) for _ in range(cantidad)]
        return animales
    
    def dibujar_animal(self, animal, ventana):
        ventana.blit(animal.imagen, (animal.posicion[0] * TAMANO_CELDA, animal.posicion[1] * TAMANO_CELDA))

        
    def mostrar_mensaje(self, mensaje, x, y):
        fuente = pg.font.Font(None, 24)
        texto = fuente.render(mensaje, True, (0, 0, 0))
        self.ventana.blit(texto, (x, y))

    def actualizar_entorno(self, ventana):
        self.entorno = [[None for _ in range(ANCHO // TAMANO_CELDA)] for _ in range(ALTO // TAMANO_CELDA)]

       
        for depredador in self.depredadores:
            x, y = depredador.posicion
            self.entorno[y][x] = depredador

        
        for presa in self.presas:
            x, y = presa.posicion
            self.entorno[y][x] = presa

        for comida in self.comidas:
            x, y = comida.posicion
            self.entorno[y][x] = comida    



    def ejecutar_simulacion(self, ventana):
        while True:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    pg.quit()
                    return
            
            fondo_imagen_path = "imgplantas/dia.png" if self.dia else "imgplantas/noche.png"
            fondo_imagen = pg.image.load(fondo_imagen_path).convert()

            #ventana.fill((0, 0, 0, 0))

            ventana.blit(fondo_imagen, (0, 0))
            self.actualizar_entorno(ventana)


            

            presas_cazadas = []
        
            depredadores_muertos = []

          
            depredador_verificado = False  

            for depredador in self.depredadores:
                if not depredador_verificado:
                    depredador.moverse_aleatoriamente(self.entorno)
                    if depredador.envejecer_y_morir():
                        depredadores_muertos.append(depredador)
                        depredador_verificado = True  

    
            if depredadores_muertos:
                depredador_muerto = random.choice(depredadores_muertos)
                self.depredadores.remove(depredador_muerto)

            
            for presa in self.presas:
                presa.moverse_aleatoriamente(self.entorno)
                presa.envejecer()
                if presa.reproducirse():
                    nueva_posicion = (random.randint(0, ANCHO // TAMANO_CELDA - 1),
                                    random.randint(0, ALTO // TAMANO_CELDA - 1))
                    nueva_presa = type(presa)(posicion=nueva_posicion)
                    self.presas.append(nueva_presa)

             

            for depredador in self.depredadores:
                for presa in self.presas:
                    if presa is not None:
                        distancia = math.sqrt((depredador.posicion[0] - presa.posicion[0]) ** 2 +
                                             (depredador.posicion[1] - presa.posicion[1]) ** 2)
                        if distancia < DISTANCIA_CAZA:
                            mensaje_caza = depredador.cazar(presa)
                            self.mostrar_mensaje(mensaje_caza, 10, 10)
                            presas_cazadas.append(presa)

            self.presas = [presa for presa in self.presas if presa not in presas_cazadas]

            for fila in self.entorno:
                for organismo in fila:
                    if organismo is not None:
                        self.dibujar_animal(organismo, ventana)

            self.ciclos_transcurridos += 1

            
            if self.ciclos_transcurridos >= self.tiempo_cambio:
                self.ciclos_transcurridos = 0  
                self.dia = not self.dia 
                print(f"Estado:  {'Es de Dia' if self.dia else 'Es de Noche'}")

                        
            
          
            pg.display.update()
            self.reloj.tick(2)

#------------------------------------------------------------------------------------------------------------
