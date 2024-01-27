import pygame
import sys
import time

ANCHO = 640
ALTO = 480
FONDO = (0,0,64)

pygame.init()
#creamos reloj para mover la bolita mas lento
reloj = pygame.time.Clock()
#ajustar repetición de eventos para presion de tecla
pygame.key.set_repeat(30)


class Bolita(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagenes/bolita.png')
        self.rect = self.image.get_rect()
        #posición inicial de la bolita
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        self.speed = [3,3]
        
    def update(self):
        if self.rect.top <= 0 or self.rect.bottom >= ALTO:
            self.speed[1] = -self.speed[1]
        elif self.rect.right > ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        self.rect.move_ip(self.speed)
        
class Paleta(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagenes/paleta.png')
        self.rect = self.image.get_rect()
        
        #posición inicial de la paleta
        self.rect.midbottom = (ANCHO /2,ALTO - 20)
        #velocidad inicial
        self.speed = [0,0]
        
    def update(self,evento):
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5,0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5,0]
        else:
            self.speed = [0,0]
            
        self.rect.move_ip(self.speed)
        
    

pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('Mi primer videojuego con python')


bolita = Bolita()
jugador = Paleta()

while True:
    #establecer el tiempo del reloj
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            jugador.update(evento)
            
    #movemos la bolita
    bolita.update()
            
    pantalla.fill(FONDO)
    pantalla.blit(bolita.image,bolita.rect)
    pantalla.blit(jugador.image,jugador.rect)
    #actualizar los objetos en la pantalla
    pygame.display.flip()