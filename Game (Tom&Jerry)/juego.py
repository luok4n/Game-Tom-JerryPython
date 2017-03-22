import pygame
from pygame.locals import *
import sys
import time
import mapa
import q
import random


pygame.init()


#Define global variables

BLANCO = (255,255,255)
AMARILLO = (255,0,0)
tipoLetra = pygame.font.Font('Grandezza.ttf', 40)
tipoLetra2 = pygame.font.Font('Grandezza.ttf', 30)
musica=pygame.mixer.Sound("benny.ogg")
soundqueso=pygame.mixer.Sound("bonus.ogg")
gameoversound=pygame.mixer.Sound("gameover.ogg")
winnersouned=pygame.mixer.Sound("winner.ogg")
lasersound=pygame.mixer.Sound("laser.ogg")
imagenDeFondo = 'Noticia_TomJerry.jpg'
explosion=pygame.mixer.Sound("explosion.ogg")
star=pygame.mixer.Sound("star.ogg")
presound=pygame.mixer.Sound("preludio.ogg")
imagenGatoContento = 'gato.png'
imagenGatoEnfadado = 'gato2.png'
imagenRatonContento = 'raton1.png'
imagenRatonEnfadado = 'raton2.png'
imagenQueso = 'q.png'
ancho=800
alto=600
space='space.png'
inst1='inst1.png'
inst2='inst2.png'
pr1='a1.png'
pr2='a2.png'
pr3='a3.png'
pr4='a4.png'
pr5='a5.png'
pr6='a6.png'
pr7='a7.png'
pr8='a8.png'
pr9='a9.png'

vida1='vida1.png'
vida2='vida2.png'
vida3='vida3.png'
vida4='vida4.png'
ex3='fire3.png'
visor = pygame.display.set_mode((800, 600))
global quesos
global sound
global vida
vida=3
quesos=0
sound= True

#Class of the cheese

class bloque(pygame.sprite.Sprite):

		def __init__(self,archivo):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load(archivo).convert_alpha()
			self.rect=self.image.get_rect()

		def reini_pos(self):
			self.rect.y=random.randrange(-500,-20)
			self.rect.x=random.randrange(0,ancho)

		def update(self):
			self.rect.y +=1
			if self.rect.y >810:
			   self.reini_pos()


class asteroide(pygame.sprite.Sprite):

		def __init__(self,archivo):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load(archivo).convert_alpha()
			self.rect=self.image.get_rect()

		def reini_pos(self):
			self.rect.y=random.randrange(-2000,-20)
			self.rect.x=random.randrange(0,ancho)

		def update(self):
			self.rect.y +=1
			if self.rect.y >810:
			   self.reini_pos()

class jugador(pygame.sprite.Sprite):

                def __init__(self,archivo):
                        pygame.sprite.Sprite.__init__(self)
                        self.image = pygame.image.load(archivo).convert_alpha()
                        self.rect=self.image.get_rect()

                def reini_pos(self):
                        self.rect.y=550
                        self.rect.x=500

                def pos(self):
                    self.rect.y=500
                    self.rect.x=550

class item(pygame.sprite.Sprite):

                def __init__(self,archivo):
                        pygame.sprite.Sprite.__init__(self)
                        self.image = pygame.image.load(archivo).convert_alpha()
                        self.rect=self.image.get_rect()

                def reini_pos(self):
                        self.rect.y=random.randrange(-1000,-800)
                        self.rect.x=random.randrange(0,ancho)

                def update(self):
                        self.rect.y +=1
                        if self.rect.y >5000:
                            self.reini_pos()

class bala(pygame.sprite.Sprite):

                var_y=9

                def __init__(self,x,y,archivo):
                        pygame.sprite.Sprite.__init__(self)
                        self.image = pygame.image.load(archivo).convert_alpha()
                        self.rect=self.image.get_rect()
                        self.rect.y += y
                        self.rect.x += x

                def update(self):
                        if (self.rect.top>-50):
                                self.rect.y -= self.var_y
                        else:
                                self.rect.top= -50



bl=pygame.sprite.Group()
tl=pygame.sprite.Group()
al=pygame.sprite.Group()
nave=jugador("nave.png")
modi=pygame.sprite.Group()
tl.add(nave)
ll=pygame.sprite.Group()

for i in range (10):
	b=bloque("q.png")
	b.rect.x= random.randint(10,ancho)
	b.rect.y= random.randint(-500,0)
	bl.add(b)
	tl.add(b)

for i in range (3):
        bonus=item("item.png")
        bonus.rect.x= random.randint(10,ancho)
        bonus.rect.y= random.randint(-500,0)
        modi.add(bonus)
        tl.add(bonus)

    
for i in range (30):
        a=asteroide("asteroid.png")
        a.rect.x=random.randint(10,ancho)
        a.rect.y=random.randint(-1000,-400)
        al.add(a)
        tl.add(a)	
	
estrellas= 'Estrellas.jpg'


def pausa():
   esperar = True
   while esperar:
      for evento in pygame.event.get():
          if evento.type == KEYDOWN:
              esperar = False
  

def ins1():
    fondo =pygame.image.load(inst1).convert()
    visor.blit(fondo,(0,0))
    pygame.display.update()
    pausa()

def ins2():
    fondo =pygame.image.load(inst2).convert()
    visor.blit(fondo,(0,0))
    pygame.display.update()
    pausa()


    

    
def fondonave():
   mega_x=500
   mega_y=550
   modificador=0
   global vida
   global quesos
   global sound
   vel=1
   laser= bala(-10,-10,"laser.png")
   laser2=bala(-10,-10,"laser.png")
   tl.add(laser)
   tl.add(laser2)
   f3=pygame.image.load(ex3).convert()
   v1=pygame.image.load(vida1).convert()
   v2=pygame.image.load(vida2).convert()
   v3=pygame.image.load(vida3).convert()
   v4=pygame.image.load(vida4).convert()
   puntosnave=0
   fondo = pygame.image.load(estrellas).convert()
#   nave=pygame.image.load(mega).convert()
   visor.blit(fondo,(0,0))
#   visor.blit(nave,(mega_x,mega_y))
   nave.rect.x=mega_x
   nave.rect.y=mega_y
   tl.update()
   pygame.display.update()
   l_existe=False
   fin =False
   while not fin:
      for event in pygame.event.get():
         if event.type == pygame.QUIT: sys.exit
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               if sound == True:
                   lasersound.play()
               laser= bala(-10,-10,"laser.png")
               laser2=bala(-10,-10,"laser.png")
               tl.add(laser)
               tl.add(laser2)               
               if modificador==1 or modificador==2 or modificador == 3:
                   laser2.rect.x=nave.rect.x-10
                   laser2.rect.y=nave.rect.y-20
                   laser.rect.x=nave.rect.x+25
                   laser.rect.y=nave.rect.y-20
               if modificador==0:                   
                   laser2.rect.x=-20
                   laser2.rect.y=-20
                   laser.rect.x=nave.rect.x+11
                   laser.rect.y=nave.rect.y-20
               l_existe=True

               if laser.rect.y == 0:
                   laser.rect.x = -20
               if laser2.rect.y == 0:
                   laser2.rect.x = -20
                   
      
      keys= pygame.key.get_pressed()
      if keys[K_LEFT]:
          nave.rect.x = nave.rect.x-vel
          if nave.rect.x <= (-60 ):
            nave.rect.x=ancho
      if keys[K_RIGHT]:
            nave.rect.x=nave.rect.x+vel
            if nave.rect.x >= (ancho ):
               nave.rect.x=-60
      if keys[K_p]:
          tempx=nave.rect.x
          tempy=nave.rect.y
          nave.rect.x=-10
          nave.rect.x=-10
          pausar()
          nave.rect.x=tempx
          nave.rect.x=tempy

      if keys[K_u]and sound==True:
         sound= False
         star.stop()
    

      if keys[K_i]and sound==False:
         sound= True
         star.play()

      lg= pygame.sprite.spritecollide(laser,al,True)
      for b in lg:
         if sound == True:
             explosion.play()
         visor.blit(f3,(b.rect.x,b.rect.y))
         pygame.display.update()
         time.sleep(0.08)
         b.reini_pos()
         laser.rect.x=-10
         laser.rect.y=-10
         laser2.rect.x=-10
         laser2.rect.y=-10

      lg2= pygame.sprite.spritecollide(laser2,al,True)
      for b in lg2:
         if sound == True:
             explosion.play()
         visor.blit(f3,(b.rect.x,b.rect.y))
         pygame.display.update()
         time.sleep(0.08)
         b.reini_pos()
         laser2.rect.x=-10
         laser2.rect.y=-10
         laser.rect.x=-10
         laser.rect.y=-10

      if vida==4:
          visor.blit(v4,(5,5))
          pygame.display.update()

      if vida==3:
          visor.blit(v3,(5,5))
          pygame.display.update()

      if vida==2:
          visor.blit(v2,(5,5))
          pygame.display.update()

      if vida==1:
          visor.blit(v1,(5,5))
          pygame.display.update()
        
      ag=pygame.sprite.spritecollide(nave,bl,True)
      for a in ag:
          puntosnave +=1
          a.reini_pos()

      mo=pygame.sprite.spritecollide(nave,modi,True)
      for bonus in mo:
          modificador +=1
          if modificador==2:
                vel=vel+1
          if modificador ==3:
                vida= vida+1
          bonus.reini_pos()

      ty= pygame.sprite.spritecollide(nave,al,True)
      for a in ty:
         vida=vida-1
         if sound == True:
             explosion.play()
         visor.blit(f3,(nave.rect.x,550))
         pygame.display.update()
         time.sleep(0.08)
         if vida == 0:
              puntuaciongato()
         a.reini_pos()

      visor.blit(fondo,(0,0))
#      visor.blit(nave,(mega_x,mega_y))
      tl.update()
      tl.draw(visor)
     # if l_existe:
      #   laser.rect.y=laser.rect.y-4
       #  laser2.rect.y=laser.rect.y-4
	
      pygame.display.flip()
      if puntosnave == 10:
          quesos= quesos+puntosnave
          pygame.display.update
          puntosnave=0
          puntuacionraton()
          epilogo()
          pygame.quit()
          sys.exit()          

	 	
def mostrarIntro():
   teclasPulsadas = pygame.key.get_pressed()
   fondo = pygame.image.load(imagenDeFondo).convert()
   visor.blit(fondo, (0,0))
   mensaje = 'Pulsa cualquier tecla para comenzar'
   texto = tipoLetra2.render(mensaje, True, AMARILLO)
   visor.blit(texto, (50,550,350,30))
   pygame.display.update()
   pausa()

def preludio():
    fondo1 =pygame.image.load(pr1).convert()
    fondo2 =pygame.image.load(pr2).convert()
    fondo3 =pygame.image.load(pr3).convert()
    fondo4 =pygame.image.load(pr4).convert()
    fondo5 =pygame.image.load(pr5).convert()
    fondo6 =pygame.image.load(pr6).convert()
    fondo7 =pygame.image.load(pr7).convert()
    fondo8 =pygame.image.load(pr8).convert()
    fondo9 =pygame.image.load(pr9).convert()
    presound.play()
    visor.blit(fondo1, (0,0))
    pygame.display.update()
    time.sleep(1.5)
    visor.blit(fondo2, (0,0))
    pygame.display.update()
    time.sleep(1.5)
    visor.blit(fondo3, (0,0))
    pygame.display.update()
    time.sleep(1.5)
    visor.blit(fondo4, (0,0))
    pygame.display.update()
    time.sleep(1.5)
    visor.blit(fondo5, (0,0))
    pygame.display.update()
    time.sleep(1.5)
    visor.blit(fondo6, (0,0))
    pygame.display.update()
    time.sleep(1.5)
    visor.blit(fondo7, (0,0))
    pygame.display.update()
    time.sleep(1.5)
    visor.blit(fondo8, (0,0))
    pygame.display.update()
    time.sleep(1.5)
    presound.stop()
    visor.blit(fondo9, (0,0))
    pygame.display.update()
    time.sleep(1.5)



pygame.mouse.set_visible(False)
mostrarIntro()
preludio()
time.sleep(0.75)
musica.play()



def mostrarlvl2():
    global lvl
    lvl=2
    fondo = pygame.image.load(space).convert()
    visor.blit(fondo,(0,0))
    mensaje= 'Nivel 2'
    mensaje2='Pulsa una tecla para comenzar'
    texto1=tipoLetra.render(mensaje, True, AMARILLO)
    texto2=tipoLetra.render(mensaje2, True, BLANCO)
    visor.blit(texto1, (280,50,350,30))
    visor.blit(texto2, (20,550,350,30))
    pygame.display.update()
    pausa()
    ins2()
    star.play()
    

def puntuaciongato():
   fondo = pygame.image.load(imagenDeFondo).convert()
   visor.blit(fondo, (0,0))
   mensaje = 'Game Over'
   texto = tipoLetra.render(mensaje, True, AMARILLO)
   visor.blit(texto, (260,550,350,30))
   pygame.display.update()
   musica.stop()
   star.stop()
   if sound == True:
       gameoversound.play()
   pausa()
   pygame.quit()
   sys.exit()

def epilogo():
    movie = pygame.movie.Movie('epilogo.mpg')
    mrect= pygame.Rect(0,0,800,600)
    movie.set_display(visor,mrect.move(0,0))
    movie.play()
    pausa()
    pygame.quit()
    sys.exit()

def pausar():
   global sound
   teclasPulsadas = pygame.key.get_pressed()
   fondo = pygame.image.load(imagenDeFondo).convert()
   visor.blit(fondo, (0,0))
   mensaje1='Activar sonido ( i )'
   mensaje2='Desactivar sonido ( u )'
   texto1=tipoLetra2.render(mensaje1,True,AMARILLO)
   texto2=tipoLetra2.render(mensaje2, True, AMARILLO)
   visor.blit(texto2, (150,500,350,30))
   visor.blit(texto1,(190,550,350,30))
   pygame.display.update()
   pausa()
   


   
def puntuacionraton():
   fondo = pygame.image.load(imagenDeFondo).convert()
   visor.blit(fondo, (0,0))
   mensaje = 'Puntaje'
   if quesos == 0:
      puntaje ='1'
   if quesos == 1:
      puntaje ='2'
   if quesos == 2:
      puntaje ='3'
   if quesos == 3:
      puntaje ='4'
   if quesos == 4:
      puntaje ='5'
   if quesos == 5:
      puntaje ='6'
   if quesos == 6:
      puntaje ='7'
   if quesos == 7:
      puntaje ='8'
   if quesos == 8:
      puntaje ='9'
   if quesos == 9:
      puntaje ='10'
   if quesos == 10:
      puntaje ='11'
   if quesos == 11:
      puntaje ='12'
   if quesos == 12:
      puntaje ='13'
   if quesos == 13:
      puntaje ='14'
   if quesos == 14:
      puntaje ='15'
   if quesos == 15:
      puntaje ='16'
   if quesos == 16:
      puntaje ='17'
   if quesos == 17:
      puntaje ='18'
   if quesos == 18:
      puntaje ='19'
   if quesos == 19:
      puntaje ='20'
   if quesos == 20:
      puntaje ='21'
   if quesos == 21:
      puntaje ='22'
   if quesos == 22:
      puntaje ='23'
   if quesos == 23:
      puntaje ='24'
   if quesos == 24:
      puntaje ='25'
   if quesos == 25:
      puntaje ='26'
   if quesos == 26:
      puntaje ='27'
   if quesos == 27:
      puntaje ='28'
   if quesos == 28:
      puntaje ='29'
   if quesos == 29:
      puntaje ='30'
   if quesos == 30:
      puntaje ='30'
   texto = tipoLetra.render(mensaje, True, AMARILLO)
   texto1 = tipoLetra.render(puntaje, True, AMARILLO)
   musica.stop()
   star.stop()
   if sound == True:
       winnersouned.play()
   visor.blit(texto, (60,550,350,30))
   visor.blit(texto1, (280,550,350,30))
   pygame.display.update()
   pausa()


class imagenRatonContento( pygame.sprite.Sprite ):

    def __init__( self, posX, posY ):
        pygame.sprite.Sprite.__init__( self )
        self.image = pygame.image.load('raton1.png').convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
              
      
        
        
        self.rect.topleft = (posX, posY)
               
        
        
        self.dy = 0
        self.dx = 0
                
    def update(self):       
        
        
        self.pos = self.rect.topleft
       
       
        
        
        self.rect.move_ip(self.dx,self.dy)
        
    def deshacer(self):
 
               
        self.rect.topleft = self.pos



class imagenGatoContento( pygame.sprite.Sprite ):

    def __init__( self, posX, posY ):
        pygame.sprite.Sprite.__init__( self )
        self.image = pygame.image.load('gato.png').convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
              
        self.rect.topleft = (posX, posY)
               
        self.dy = 0
        self.dx = 0
                
    def update(self):
                
        self.pos = self.rect.topleft
       
        self.rect.move_ip(self.dx,self.dy)
        
    def deshacer(self):
 
        self.rect.topleft = self.pos




visor = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tom&Jerry')






imagenRatonContento = imagenRatonContento(50,200)
imagenGatoContento = imagenGatoContento(50,500)

grupoimagenRatonContento = pygame.sprite.RenderUpdates( imagenRatonContento )
grupoimagenGatoContento = pygame.sprite.RenderUpdates( imagenGatoContento )

nivel = mapa.Mapa('mapa.txt')



reloj = pygame.time.Clock()



while True:
    
    reloj.tick(60)


    
    for evento in pygame.event.get():
        if evento.type == QUIT or (evento.type == KEYDOWN and evento.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    

    
    if imagenGatoContento.rect.right > 800:
        puntuaciongato()
        pygame.quit()
        sys.exit() 
    
    
    teclasPulsadas = pygame.key.get_pressed()



    if imagenGatoContento.rect.top > 40 and imagenGatoContento.rect.left < 50:
        imagenGatoContento.dy=-3
        imagenGatoContento.dx=0
    elif imagenGatoContento.rect.left <500 and imagenGatoContento.rect.top <50:
        imagenGatoContento.dx=3
        imagenGatoContento.dy=0
    elif imagenGatoContento.rect.top < 250:
        imagenGatoContento.dy=3
        imagenGatoContento.dx=0
    else:
        imagenGatoContento.dy=0
        imagenGatoContento.dx=-3

    if imagenGatoContento.rect.top >249 and imagenGatoContento.rect.left > 200 and imagenGatoContento.rect.left < 330 and imagenGatoContento.rect.top <390  :
        imagenGatoContento.dy=3
        imagenGatoContento.dx=0
    elif imagenGatoContento.rect.top < 400 and imagenGatoContento.rect.left > 150 and imagenGatoContento.rect.top > 340 and imagenGatoContento.rect.left < 700:
        imagenGatoContento.dy=0
        imagenGatoContento.dx=3
    elif imagenGatoContento.rect.top < 470 and imagenGatoContento.rect.top > 339 and imagenGatoContento.rect.left > 201  :
        imagenGatoContento.dy=3
        imagenGatoContento.dx=0        
        

    
    
    
    if imagenRatonContento.rect.right > 800:
        puntuacionraton()
        mostrarlvl2()
        fondonave()

 
    
    teclasPulsadas = pygame.key.get_pressed()
    

    
    if teclasPulsadas[K_LEFT]:
        imagenRatonContento.dx = -3
    elif teclasPulsadas[K_RIGHT]:
        imagenRatonContento.dx = 3
    else:
        imagenRatonContento.dx = 0
        
    if teclasPulsadas[K_UP]:
        imagenRatonContento.dy = -3
    elif teclasPulsadas[K_DOWN]:
        imagenRatonContento.dy = 3
    else:
        imagenRatonContento.dy = 0
    

    
    grupoimagenRatonContento.update()
    grupoimagenGatoContento.update()
  
 
    
    if pygame.sprite.spritecollide(imagenRatonContento, nivel.grupo, 0, pygame.sprite.collide_mask):        
        imagenRatonContento.deshacer()
        
    if pygame.sprite.spritecollide(imagenGatoContento, nivel.grupo, 0, pygame.sprite.collide_mask):
        imagenGatoContento.deshacer()    
    
    if teclasPulsadas[K_p]:
       pausar()

    if teclasPulsadas[K_o]:
       ins1()

    if teclasPulsadas[K_u]and sound==True:
         sound= False
         musica.stop()

    if teclasPulsadas[K_i]and sound==False:
         sound= True
         musica.play()
    
    for pum in pygame.sprite.groupcollide(grupoimagenRatonContento, nivel.quesos, 0, 1):
        quesos=quesos+1
        if sound == True:
            soundqueso.play()
        pass
      
  
    for pum in pygame.sprite.groupcollide(grupoimagenRatonContento, grupoimagenGatoContento, 1, 0):
        puntuaciongato()
        pygame.quit()
        sys.exit()    


    nivel.actualizar(visor)

    
 
    
    grupoimagenRatonContento.draw(visor)
    grupoimagenGatoContento.draw(visor)
       
    pygame.display.update()

  
