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
        if self.rect.top <= 0: #or self.rect.bottom >= ALTO:
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
        
class Ladrillo(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagenes/ladrillo.png')
        self.rect= self.image.get_rect()
        self.rect.topleft = position
        
class Muro(pygame.sprite.Group):
    def __init__(self,cantidad):
        pygame.sprite.Group.__init__(self)
        pos_x = 0
        pos_y = 20
        for i in range(cantidad):
            ladrillo = Ladrillo((pos_x,pos_y))
            self.add(ladrillo)
            
            pos_x += ladrillo.rect.width
            if pos_x >= ANCHO:
                pos_x = 0
                pos_y += ladrillo.rect.height
                
            
        
    

pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('Mi primer videojuego con python')


bolita = Bolita()
jugador = Paleta()
muro = Muro(50)

#carga sonidos para videojuego
sonido_colision_paleta = pygame.mixer.Sound('sonidos/colision.ogg')
sonido_colision_muro = pygame.mixer.Sound('sonidos/colision_muro.ogg')
sonido_game_over = pygame.mixer.Sound('sonidos/game_over.ogg')

def juego_terminado():
    fuente = pygame.font.SysFont('Arial',72)
    texto = fuente.render('GAME OVER',True,(255,255,255))
    texto_rect = texto.get_rect()
    texto_rect.center = [ANCHO / 2, ALTO / 2]
    pantalla.blit(texto,texto_rect)
    pygame.display.flip()
    pygame.mixer.Sound.play(sonido_game_over)
    time.sleep(5)
    sys.exit()

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
    
    #### COLISIONES################
    #COLISION DE BOLITA Y JUGADOR
    if pygame.sprite.collide_rect(bolita,jugador):
        bolita.speed[1] = -bolita.speed[1]
        pygame.mixer.Sound.play(sonido_colision_paleta)
    
    #COLISION DE BOLITA CON EL MURO
    lista = pygame.sprite.spritecollide(bolita,muro,False)
    if lista:
        ladrillo = lista[0]
        cx = bolita.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita.speed[0] = -bolita.speed[0]
        else:
            bolita.speed[1] = -bolita.speed[1]
        muro.remove(ladrillo)
        pygame.mixer.Sound.play(sonido_colision_muro)
        
    if bolita.rect.top > ALTO:
        juego_terminado()
            
    pantalla.fill(FONDO)
    pantalla.blit(bolita.image,bolita.rect)
    pantalla.blit(jugador.image,jugador.rect)
    muro.draw(pantalla)
    #actualizar los objetos en la pantalla
    pygame.display.flip()