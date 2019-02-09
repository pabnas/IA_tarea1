import pygame
import sys
import numpy as np

grid = sys.argv[1]
LEFT = 1
RIGHT = 3
from pygame.locals import *

#funciones
def pintar_cuadro(x,y,num):
	pygame.draw.rect(ventana, color[num],(cuadro_size*x,cuadro_size*y,cuadro_size,cuadro_size))
	if grid == "-g":
		for x in range(20):
			pygame.draw.line(ventana,color[19],(cuadro_size*(x+1),0),(cuadro_size*(x+1),cuadro_size*20))
			pygame.draw.line(ventana,color[19],(0,cuadro_size*(x+1)),(cuadro_size*20,cuadro_size*(x+1)))
	pygame.display.update()

#programa
pygame.init()
cuadro_size = 30
color = np.zeros((20,3))
color[0]  = (255,255,255)	#blanco
color[1]  = (255,255,0)		#amarillo
color[2]  = (34,113,179)	#azul
color[3]  = (87,166,57)		#verde
color[4]  = (213,48,50)		#rojo
color[5]  = (99,58,52)		#cafe
color[6]  = (215,45,109)	#magenta
color[7]  = (255,117,20)	#naranja
color[8]  = (127,181,181)	#turquesa
color[9]  = (234,137,154)	#rosa
color[10] = (40,114,51)		#esmeralda
color[11] = (1,93,82)		#opalo
color[12] = (0,247,0)		#verde brillante
color[13] = (244,169,0)		#melon
color[14] = (71,64,46)		#oliva
color[15] = (37,109,123)	#agua
color[16] = (194,176,120)	#beige
color[17] = (110,28,52)		#brudeos
color[18] = (125,132,113)	#gris cemento
color[19] = (10,10,10)		#negro

color_actual = 0
ventana = pygame.display.set_mode((cuadro_size*20,cuadro_size*20))
pygame.display.set_caption("programa")
ventana.fill(color[0])
for x in range(20):
	pintar_cuadro(x,0,x)	#pinta la barra inicial


while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		pygame.quit()
		sys.exit()
	if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
		pos = pygame.mouse.get_pos()
		posx,posy = pos
		posx = int(posx/cuadro_size)
		posy = int(posy/cuadro_size)
		if posy != 0:
			pintar_cuadro(posx,posy,color_actual)
	if event.type == MOUSEBUTTONDOWN and event.button == RIGHT:
		pos = pygame.mouse.get_pos()
		posx,posy = pos
		posx = int(posx/cuadro_size)
		posy = int(posy/cuadro_size)
		if posy == 0:
			color_actual = posx
			print("Color actual",color_actual+1)
