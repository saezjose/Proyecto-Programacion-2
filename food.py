import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 30
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
CELL_SIZE = 30

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x * CELL_SIZE
        self.rect.y = y * CELL_SIZE

class Herbivore(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Herbivore Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
foods = pygame.sprite.Group()

# Crear una matriz de 0 y 1 para representar la presencia de comida
matrix_width = WIDTH // CELL_SIZE
matrix_height = HEIGHT // CELL_SIZE
food_matrix = [[0] * matrix_width for _ in range(matrix_height)]

herbivore = Herbivore()
all_sprites.add(herbivore)

# Función para generar comida en ubicaciones aleatorias en la matriz
def generate_food():
    x = random.randrange(matrix_width)
    y = random.randrange(matrix_height)
    food_matrix[y][x] = 1
    food = Food(x, y)
    all_sprites.add(food)
    foods.add(food)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generar comida de manera continua
    if random.randrange(100) < 2:
        generate_food()

    # Comprobar colisiones entre el herbívoro y la comida
    hits = pygame.sprite.spritecollide(herbivore, foods, True)

    for hit in hits:
        print("¡Comiste la comida!")

    screen.fill((0, 0, 0))

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
