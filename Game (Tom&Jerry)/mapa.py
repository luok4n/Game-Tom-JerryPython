import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
fondo1= pygame.image.load("fondo.jpg").convert()

#Create the walls of the game
class Pared(pygame.sprite.Sprite):
    def __init__(self, imagen, pos):
        pygame.sprite.Sprite.__init__( self )
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    def update(self):
        pass



#Create the chesse in the game
class Queso(pygame.sprite.Sprite):

    def __init__(self, imagen, pos):
        pygame.sprite.Sprite.__init__( self )
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect_colision = self.rect.inflate(-30, -10)
        self.delay = 0
        self.se_puede_comer = True
        self.rect.topleft = pos
    
    def update(self):
        pass

    def update_desaparecer(self):
        self.delay -= 1
        if self.delay < 1:
            self.kill()


    def comer(self):
        self.delay = 30
        self.update = self.update_desaparecer
        self.se_puede_comer = False




#This class load the pic of the wall for render the walls and the chesses
class Mapa:
    def __init__(self, archivo): 

       
        self.grupo = pygame.sprite.RenderUpdates()
        self.quesos = pygame.sprite.RenderUpdates()

        self.h=pygame.image.load('h.png').convert_alpha()
        self.v=pygame.image.load('v.png').convert_alpha()
        self.sd=pygame.image.load('sd.png').convert_alpha()
        self.id=pygame.image.load('id.png').convert_alpha()
        self.ii=pygame.image.load('ii.png').convert_alpha()
        self.si=pygame.image.load('si.png').convert_alpha()
        self.q=pygame.image.load('q.png').convert_alpha() 
        
        
        
        
        archivo = open(archivo)
        self.textoMapa = archivo.readlines()
        archivo.close()
        
        
        fila = -1
        for linea in self.textoMapa:
            fila += 1
            columna = -1
            for c in linea:
                columna += 1
                
 
                
                x,y = self.aPixel(fila,columna)
                
            
                
                if c == '-':
                    self.grupo.add(Pared(self.h, (x,y)))
                elif c == '|':
                    self.grupo.add(Pared(self.v, (x,y)))
                elif c == '7':
                    self.grupo.add(Pared(self.sd, (x,y)))
                elif c == 'J':
                    self.grupo.add(Pared(self.id, (x,y)))
                elif c == 'L':
                    self.grupo.add(Pared(self.ii, (x,y)))
                elif c == 'T':
                    self.grupo.add(Pared(self.si, (x,y)))
                elif c == 'k':
					self.quesos.add(Queso(self.q, (x,y)))
              
 
    
    
    
    def actualizar(self, visor):
        screen.blit(fondo1,(0,0))
        self.grupo.update()
        self.grupo.draw(visor)
        self.quesos.update()
        self.quesos.draw(visor)

    
    def aPixel(self, fila, columna):
        return (columna*40, fila*40)
    

    
    def aCuadricula(self, x, y):
        return (y/40, x/40)
        




