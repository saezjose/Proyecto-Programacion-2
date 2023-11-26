import pygame
import sys

class CicloDiaNoche:
    def __init__(self):
        pygame.init()

        # Reloj para controlar la velocidad del ciclo
        self.clock = pygame.time.Clock()

        # Inicializar variables para el ciclo de día y noche
        self.is_day = True
        self.time_of_day = 0  # Variable para controlar la intensidad de la luz (0 para noche, 255 para día)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Lógica para el ciclo de día y noche
            if self.is_day:
                self.time_of_day += 1
                if self.time_of_day > 255:
                    self.time_of_day = 255
            else:
                self.time_of_day -= 1
                if self.time_of_day < 0:
                    self.time_of_day = 0

            # Establecer la velocidad del bucle
            self.clock.tick(30)  # Puedes ajustar esto según sea necesario

if __name__ == "__main__":
    juego = CicloDiaNoche()
    juego.run()
