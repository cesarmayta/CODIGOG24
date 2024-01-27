import pygame
import sys

ANCHO = 640
ALTO = 480

pygame.init()

pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('Mi primer videojuego con python')

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()