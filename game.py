import pygame
import random
import sys

# Constantes
ANCHO_VENTANA = 640
ALTO_VENTANA = 480
FPS = 10

# Inicializando Pygame
pygame.init()

# Pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Juego de la Serpiente")

# La serpiente
serpiente = [(ANCHO_VENTANA // 2, ALTO_VENTANA // 2)]
direccion = (0, 0)

# La comida de la serpiente
comida = (random.randint(0, ANCHO_VENTANA // 10 - 1) * 10, random.randint(0, ALTO_VENTANA // 10 - 1) * 10)

# Bucle del juego
running = True
while running:

    # Actualizando el tiempo
    pygame.time.Clock().tick(FPS)

    # Manejo de los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Captura de las teclas
    teclas = pygame.key.get_pressed()

    # Actualizando la dirección de la serpiente
    if teclas[pygame.K_LEFT] and direccion != (10, 0):
        direccion = (-10, 0)
    elif teclas[pygame.K_RIGHT] and direccion != (-10, 0):
        direccion = (10, 0)
    elif teclas[pygame.K_UP] and direccion != (0, 10):
        direccion = (0, -10)
    elif teclas[pygame.K_DOWN] and direccion != (0, -10):
        direccion = (0, 10)

    # Movimiento de  la serpiente
    nueva_cabeza = (serpiente[0][0] + direccion[0], serpiente[0][1] + direccion[1])
    serpiente.insert(0, nueva_cabeza)

    # Verificando si la serpiente ha comido la comida
    if serpiente[0] == comida:
        comida = (random.randint(0, ANCHO_VENTANA // 10 - 1) * 10, random.randint(0, ALTO_VENTANA // 10 - 1) * 10)
    else:
        serpiente.pop()

    # Verificando si la serpiente se ha chocado con los bordes
    if (
        serpiente[0][0] < 0
        or serpiente[0][0] >= ANCHO_VENTANA
        or serpiente[0][1] < 0
        or serpiente[0][1] >= ALTO_VENTANA
    ):
        running = False

    # Verificando si la serpiente se ha chocado consigo misma
    if serpiente[0] in serpiente[1:]:
        running = False

    #  Pantalla
    pantalla.fill((0, 0, 0))
    for segmento in serpiente:
        pygame.draw.rect(pantalla, (255, 255, 255), pygame.Rect(segmento[0], segmento[1], 10, 10))
    pygame.draw.rect(pantalla, (255, 0, 0), pygame.Rect(comida[0], comida[1], 10, 10))
    pygame.display.flip()

# Cierra Pygame
pygame.quit()
sys.exit()