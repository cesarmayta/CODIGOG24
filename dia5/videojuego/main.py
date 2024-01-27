import pygame
import sys

ANCHO = 640
ALTO = 480

pygame.init()

class Bolita(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagenes/bolita.png')
        self.rect = self.image.get_rect()
        #posición inicial de la bolita
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        self.speed = [3,3]
    

pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('Mi primer videojuego con python')


bolita = Bolita()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
            
    pantalla.blit(bolita.image,bolita.rect)
    #actualizar los objetos en la pantalla
    pygame.display.flip()