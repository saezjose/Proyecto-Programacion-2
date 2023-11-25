from tkinter import Canvas, Tk
import pygame
import random
import math
from plantas import Arbol, Arbusto, Flor, Hierba, Hongo

ANCHO, ALTO = 1200, 800
TAMANO_CELDA = 40
DISTANCIA_CAZA = 1
CICLOS_REPRODUCCION = 50

CICLOS_ENVEJECIMIENTO = 2000
VIDA_MAXIMA_DEPREDADOR = 100
ENERGIA_MAXIMA_DEPREDADOR = 70
VELOCIDAD_MIN_DEPREDADOR = 0.001
VELOCIDAD_MAX_DEPREDADOR = 0.005


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

        # Ajustar las posiciones para que los organismos aparezcan en el lado opuesto al salir de los límites
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


class Presa(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, imagen_path):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta
        self.imagen_path = imagen_path
        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (TAMANO_CELDA, TAMANO_CELDA))

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
        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (TAMANO_CELDA, TAMANO_CELDA))
        self.ciclos_vida = 0
        self.max_ciclos_vida = random.randint(100, 500)  # Ajusta este rango según lo que consideres apropiado
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

        # Mostrar el mensaje por consola
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
    


class Leon(Depredador):
    def __init__(self, posicion):
        super().__init__(posicion, vida=100, energia=70, velocidad=random.uniform(0.001, 0.005),
                         especie="León", dieta="Carnívoro", imagen_path="depredadoresimg/leon.png")
        


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
                         especie="Águila", dieta="Carnívoro", imagen_path="depredadoresimg/aguila.png")
        


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
                         especie="Antílope", dieta="Herbívoro", imagen_path="presasimg/gacela.png")




class SimuladorAnimales:
    def __init__(self, pantalla, bosque):
        self.pantalla = pantalla
        self.bosque = bosque

        pygame.display.set_caption("Simulador de Animales")
        self.reloj = pygame.time.Clock()

        self.ventana = pygame.display.set_mode((ANCHO, ALTO))

        # Crear matriz para el entorno del juego
        self.entorno = [[None for _ in range(ANCHO // TAMANO_CELDA)] for _ in range(ALTO // TAMANO_CELDA)]

        self.comidas = []

        # Crear animales depredadores
        self.depredadores = self.generar_animales_aleatorios(Leon, 2, 2) + \
                            self.generar_animales_aleatorios(Hiena, 2, 3) + \
                            self.generar_animales_aleatorios(Zorro, 2, 5) + \
                            self.generar_animales_aleatorios(Oso, 2, 2) + \
                            self.generar_animales_aleatorios(Aguila, 2, 4)

        # Crear animales presa
        self.presas = self.generar_animales_aleatorios(Gacela, 2, 3) + \
                      self.generar_animales_aleatorios(Conejo, 2, 8) + \
                      self.generar_animales_aleatorios(Ciervo, 2, 4) + \
                      self.generar_animales_aleatorios(Cebra, 2, 3) + \
                      self.generar_animales_aleatorios(Antilope, 2, 3)

        self.tkinter_canvas = Canvas(Tk(), width=ANCHO, height=ALTO)
        self.tkinter_canvas.pack()


    def generar_animales_aleatorios(self, tipo_animal, min_cantidad, max_cantidad):
        cantidad = random.randint(min_cantidad, max_cantidad)
        animales = [tipo_animal(posicion=(random.randint(0, ANCHO // TAMANO_CELDA - 1),
                                          random.randint(0, ALTO // TAMANO_CELDA - 1))) for _ in range(cantidad)]
        return animales
    def dibujar_animal(self, animal):
        self.ventana.blit(animal.imagen, (animal.posicion[0] * TAMANO_CELDA, animal.posicion[1] * TAMANO_CELDA))

        
    def mostrar_mensaje(self, mensaje, x, y):
        fuente = pygame.font.Font(None, 24)
        texto = fuente.render(mensaje, True, (0, 0, 0))
        self.ventana.blit(texto, (x, y))

    def actualizar_entorno(self):

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

    def ejecutar_simulacion(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.ventana.fill((0, 0, 0, 0))

            # Actualizar la matriz del entorno
            self.actualizar_entorno()

            # Lista para almacenar las presas cazadas
            presas_cazadas = []
            # Lista para almacenar los depredadores muertos
            depredadores_muertos = []

            # Lógica de la simulación para depredadores
# Lógica de la simulación para depredadores
            depredador_verificado = False  # Variable para rastrear si ya hemos verificado un depredador en esta iteración

            for depredador in self.depredadores:
                if not depredador_verificado:
                    depredador.moverse_aleatoriamente(self.entorno)
                    if depredador.envejecer_y_morir():
                        depredadores_muertos.append(depredador)
                        depredador_verificado = True  # Marcar que ya hemos verificado un depredador

            # Seleccionar un depredador de manera aleatoria para morir
            if depredadores_muertos:
                depredador_muerto = random.choice(depredadores_muertos)
                self.depredadores.remove(depredador_muerto)

            # Lógica de la simulación para presas
# Lógica de la simulación para presas
            for presa in self.presas:
                presa.moverse_aleatoriamente(self.entorno)
                presa.envejecer()
                if presa.reproducirse():
                    nueva_posicion = (random.randint(0, ANCHO // TAMANO_CELDA - 1),
                                    random.randint(0, ALTO // TAMANO_CELDA - 1))
                    nueva_presa = type(presa)(posicion=nueva_posicion)
                    self.presas.append(nueva_presa)

                # Lógica para consumir comida
                

            # Lógica de caza
            for depredador in self.depredadores:
                for presa in self.presas:
                    if presa is not None:
                        distancia = math.sqrt((depredador.posicion[0] - presa.posicion[0]) ** 2 +
                                             (depredador.posicion[1] - presa.posicion[1]) ** 2)
                        if distancia < DISTANCIA_CAZA:
                            mensaje_caza = depredador.cazar(presa)
                            self.mostrar_mensaje(mensaje_caza, 10, 10)
                            # Agregar la presa cazada a la lista
                            presas_cazadas.append(presa)

            # Eliminar las presas cazadas de la lista principal de presas
            self.presas = [presa for presa in self.presas if presa not in presas_cazadas]

            # Dibujar animales en la ventana
            for fila in self.entorno:
                for organismo in fila:
                    if organismo is not None:
                        self.dibujar_animal(organismo)

            for comida in self.comidas:
                self.dibujar_comida(comida)

          

            # Actualizar la pantalla
            pygame.display.update()
            self.reloj.tick(2)
