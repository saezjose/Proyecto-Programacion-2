import pygame
import random
import math

ANCHO, ALTO = 800, 600
BLANCO = (255, 255, 255)
TAMANO_CELDA = 60
DISTANCIA_CAZA = 2
CICLOS_REPRODUCCION = 50

class Organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad
        self.ciclos_reproduccion = 0

    def moverse(self, direccion):
        x, y = self.posicion
        dx, dy = direccion
        self.posicion = (x + dx*self.velocidad, y + dy*self.velocidad)

    def reproducirse(self):
        self.ciclos_reproduccion += 1
        if self.ciclos_reproduccion >= CICLOS_REPRODUCCION:
            self.ciclos_reproduccion = 0
            return True
        return False

class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, imagen_path):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta
        self.imagen_path = imagen_path
        self.imagen = pygame.image.load(imagen_path)
        self.imagen = pygame.transform.scale(self.imagen, (TAMANO_CELDA, TAMANO_CELDA))

    def cazar(self, presa):
        probabilidad_exito = random.uniform(0, 1)

        if probabilidad_exito > 0.5:
            self.energia += presa.energia
            presa.vida = 0
            return f"{self.especie} ha cazado con éxito a {presa.especie} y ha ganado energía."
        else:
            return f"{self.especie} ha fallado en la caza."

    def explorar(self, entorno):
        direcciones_posibles = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        direccion = random.choice(direcciones_posibles)
        self.moverse(direccion)

class Depredador(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, imagen_path):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta, imagen_path)

class Presa(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, imagen_path):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta, imagen_path)

# Clase para el simulador
class SimuladorAnimales:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Simulador de Animales")
        self.reloj = pygame.time.Clock()

        # Crear animales depredadores
        self.depredadores = [
            Depredador(posicion=(random.randint(0, ANCHO//TAMANO_CELDA - 1),
                                 random.randint(0, ALTO//TAMANO_CELDA - 1)),
                       vida=100, energia=70, velocidad=random.uniform(0.5, 1.5),
                       especie="Lobo", dieta="Carnívoro", imagen_path="depredadoresimg/leon.jpg"),
            Depredador(posicion=(random.randint(0, ANCHO//TAMANO_CELDA - 1),
                                 random.randint(0, ALTO//TAMANO_CELDA - 1)),
                       vida=100, energia=70, velocidad=random.uniform(0.5, 1.5),
                       especie="Hiena", dieta="Carnívoro", imagen_path="depredadoresimg/hiena.jpg"),
            Depredador(posicion=(random.randint(0, ANCHO//TAMANO_CELDA - 1),
                                 random.randint(0, ALTO//TAMANO_CELDA - 1)),
                       vida=100, energia=70, velocidad=random.uniform(0.5, 1.5),
                       especie="Zorro", dieta="Carnívoro", imagen_path="depredadoresimg/zorro.jpg"),
            Depredador(posicion=(random.randint(0, ANCHO//TAMANO_CELDA - 1),
                                 random.randint(0, ALTO//TAMANO_CELDA - 1)),
                       vida=100, energia=70, velocidad=random.uniform(0.5, 1.5),
                       especie="Oso", dieta="Carnívoro", imagen_path="depredadoresimg/oso.png"),
            Depredador(posicion=(random.randint(0, ANCHO//TAMANO_CELDA - 1),
                                 random.randint(0, ALTO//TAMANO_CELDA - 1)),
                       vida=100, energia=70, velocidad=random.uniform(0.5, 1.5),
                       especie="Águila", dieta="Carnívoro", imagen_path="depredadoresimg/aguila.jpg")
        ]

        # Crear animales presa
        self.presas = [
            Presa(posicion=(random.randint(0, ANCHO//TAMANO_CELDA - 1),
                             random.randint(0, ALTO//TAMANO_CELDA - 1)),
                   vida=80, energia=50, velocidad=random.uniform(0.1, 1.0),
                   especie="Gacela", dieta="Herbívoro", imagen_path="presasimg/antilope.png"),
            Presa(posicion=(random.randint(0, ANCHO//TAMANO_CELDA - 1),
                             random.randint(0, ALTO//TAMANO_CELDA - 1)),
                   vida=80, energia=50, velocidad=random.uniform(0.1, 1.0),
                   especie="Conejo", dieta="Herbívoro", imagen_path="presasimg/conejo.jpg"),
            Presa(posicion=(random.randint(0, ANCHO//TAMANO_CELDA - 1),
                             random.randint(0, ALTO//TAMANO_CELDA - 1)),
                   vida=80, energia=50, velocidad=random.uniform(0.1, 1.0),
                   especie="Ciervo", dieta="Herbívoro", imagen_path="presasimg/ciervo.png"),
            Presa(posicion=(random.randint(0, ANCHO//TAMANO_CELDA - 1),
                             random.randint(0, ALTO//TAMANO_CELDA - 1)),
                   vida=80, energia=50, velocidad=random.uniform(0.1, 1.0),
                   especie="Cebra", dieta="Herbívoro", imagen_path="presasimg/cebra.jpg"),
            Presa(posicion=(random.randint(0, ANCHO//TAMANO_CELDA - 1),
                             random.randint(0, ALTO//TAMANO_CELDA - 1)),
                   vida=80, energia=50, velocidad=random.uniform(0.1, 1.0),
                   especie="Antílope", dieta="Herbívoro", imagen_path="presasimg/gacela.jpg")
        ]

    def dibujar_animal(self, animal):
        self.ventana.blit(animal.imagen, (animal.posicion[0]*TAMANO_CELDA, animal.posicion[1]*TAMANO_CELDA))

    def mostrar_mensaje(self, mensaje, x, y):
        fuente = pygame.font.Font(None, 24)
        texto = fuente.render(mensaje, True, (0, 0, 0))
        self.ventana.blit(texto, (x, y))

    def ejecutar_simulacion(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.ventana.fill(BLANCO)

            # Lógica de la simulación para depredadores
            for depredador in self.depredadores:
                depredador.explorar(None)
                if depredador.reproducirse():
                    nueva_posicion = (random.randint(0, ANCHO//TAMANO_CELDA - 1),
                                      random.randint(0, ALTO//TAMANO_CELDA - 1))
                    nuevo_depredador = Depredador(posicion=nueva_posicion,
                                                  vida=100, energia=70, velocidad=random.uniform(0.5, 1.5),
                                                  especie="Lobo", dieta="Carnívoro",
                                                  imagen_path="depredadoresimg/leon.jpg")
                    self.depredadores.append(nuevo_depredador)

            # Lógica de la simulación para presas
            for presa in self.presas:
                presa.explorar(None)
                if presa.reproducirse():
                    nueva_posicion = (random.randint(0, ANCHO//TAMANO_CELDA - 1),
                                      random.randint(0, ALTO//TAMANO_CELDA - 1))
                    nueva_presa = Presa(posicion=nueva_posicion,
                                        vida=80, energia=50, velocidad=random.uniform(0.1, 1.0),
                                        especie="Gacela", dieta="Herbívoro",
                                        imagen_path="presasimg/antilope.png")
                    self.presas.append(nueva_presa)

            # Lógica de caza
            for depredador in self.depredadores:
                for presa in self.presas:
                    distancia = math.sqrt((depredador.posicion[0] - presa.posicion[0])**2 +
                                         (depredador.posicion[1] - presa.posicion[1])**2)
                    if distancia < DISTANCIA_CAZA:
                        mensaje_caza = depredador.cazar(presa)
                        self.mostrar_mensaje(mensaje_caza, 10, 10)

            # Dibujar animales depredadores
            for depredador in self.depredadores:
                self.dibujar_animal(depredador)

            # Dibujar animales presa
            for presa in self.presas:
                self.dibujar_animal(presa)

            pygame.display.update()
            self.reloj.tick(5)

# Inicializar y ejecutar el simulador
simulador = SimuladorAnimales()
simulador.ejecutar_simulacion()
