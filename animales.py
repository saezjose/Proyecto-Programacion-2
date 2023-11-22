import pygame
import random
import math

ANCHO, ALTO = 1200, 800
TAMANO_CELDA = 40
DISTANCIA_CAZA = 2
CICLOS_REPRODUCCION = 500

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

    def moverse_aleatoriamente(self, entorno):
        direcciones_posibles = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        direccion = random.choice(direcciones_posibles)
        self.moverse(direccion)


class Leon(Depredador):
    def __init__(self, posicion):
        super().__init__(posicion, vida=100, energia=70, velocidad=random.uniform(0.01, 0.01),
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


# Clase para el simulador
class SimuladorAnimales:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Simulador de Animales")
        self.reloj = pygame.time.Clock()

        # Crear matriz para el entorno del juego
        self.entorno = [[None for _ in range(ANCHO // TAMANO_CELDA)] for _ in range(ALTO // TAMANO_CELDA)]

        # Crear animales depredadores
        self.depredadores = [
            Leon(posicion=(random.randint(0, ANCHO // TAMANO_CELDA - 1),
                            random.randint(0, ALTO // TAMANO_CELDA - 1))),
            Hiena(posicion=(random.randint(0, ANCHO // TAMANO_CELDA - 1),
                             random.randint(0, ALTO // TAMANO_CELDA - 1))),
            Zorro(posicion=(random.randint(0, ANCHO // TAMANO_CELDA - 1),
                             random.randint(0, ALTO // TAMANO_CELDA - 1))),
            Oso(posicion=(random.randint(0, ANCHO // TAMANO_CELDA - 1),
                            random.randint(0, ALTO // TAMANO_CELDA - 1))),
            Aguila(posicion=(random.randint(0, ANCHO // TAMANO_CELDA - 1),
                              random.randint(0, ALTO // TAMANO_CELDA - 1)))
        ]

        # Crear animales presa
        self.presas = [
            Gacela(posicion=(random.randint(0, ANCHO // TAMANO_CELDA - 1),
                              random.randint(0, ALTO // TAMANO_CELDA - 1))),
            Conejo(posicion=(random.randint(0, ANCHO // TAMANO_CELDA - 1),
                              random.randint(0, ALTO // TAMANO_CELDA - 1))),
            Ciervo(posicion=(random.randint(0, ANCHO // TAMANO_CELDA - 1),
                              random.randint(0, ALTO // TAMANO_CELDA - 1))),
            Cebra(posicion=(random.randint(0, ANCHO // TAMANO_CELDA - 1),
                             random.randint(0, ALTO // TAMANO_CELDA - 1))),
            Antilope(posicion=(random.randint(0, ANCHO // TAMANO_CELDA - 1),
                               random.randint(0, ALTO // TAMANO_CELDA - 1)))
        ]

    def dibujar_animal(self, animal):
        self.ventana.blit(animal.imagen, (animal.posicion[0] * TAMANO_CELDA, animal.posicion[1] * TAMANO_CELDA))

    def mostrar_mensaje(self, mensaje, x, y):
        fuente = pygame.font.Font(None, 24)
        texto = fuente.render(mensaje, True, (0, 0, 0))
        self.ventana.blit(texto, (x, y))

    def actualizar_entorno(self):
        # Limpiar la matriz del entorno
        self.entorno = [[None for _ in range(ANCHO // TAMANO_CELDA)] for _ in range(ALTO // TAMANO_CELDA)]

        # Colocar depredadores en la matriz
        for depredador in self.depredadores:
            x, y = depredador.posicion
            self.entorno[y][x] = depredador

        # Colocar presas en la matriz
        for presa in self.presas:
            x, y = presa.posicion
            self.entorno[y][x] = presa

    def ejecutar_simulacion(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.ventana.fill((0, 0, 0, 0))  # Rellenar el fondo con un color transparente

            # Actualizar la matriz del entorno
            self.actualizar_entorno()

            # Lógica de la simulación para depredadores
            for depredador in self.depredadores:
                depredador.moverse_aleatoriamente(self.entorno)
                depredador.envejecer()
                if depredador.reproducirse():
                    nueva_posicion = (random.randint(0, ANCHO // TAMANO_CELDA - 1),
                                      random.randint(0, ALTO // TAMANO_CELDA - 1))
                    nuevo_depredador = type(depredador)(posicion=nueva_posicion)
                    self.depredadores.append(nuevo_depredador)

            # Lógica de la simulación para presas
            for presa in self.presas:
                presa.moverse_aleatoriamente(self.entorno)
                presa.envejecer()
                if presa.reproducirse():
                    nueva_posicion = (random.randint(0, ANCHO // TAMANO_CELDA - 1),
                                      random.randint(0, ALTO // TAMANO_CELDA - 1))
                    nueva_presa = type(presa)(posicion=nueva_posicion)
                    self.presas.append(nueva_presa)

            # Lógica de caza
            for depredador in self.depredadores:
                for presa in self.presas:
                    if presa is not None:
                        distancia = math.sqrt((depredador.posicion[0] - presa.posicion[0]) ** 2 +
                                             (depredador.posicion[1] - presa.posicion[1]) ** 2)
                        if distancia < DISTANCIA_CAZA:
                            mensaje_caza = depredador.cazar(presa)
                            self.mostrar_mensaje(mensaje_caza, 10, 10)

            # Dibujar animales en la ventana
            for fila in self.entorno:
                for organismo in fila:
                    if organismo is not None:
                        self.dibujar_animal(organismo)

            pygame.display.update()
            self.reloj.tick(5)

# Inicializar y ejecutar el simulador
simulador = SimuladorAnimales()
simulador.ejecutar_simulacion()
