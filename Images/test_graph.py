import pygame 
from pygame.locals import *
import os

r=200

os.chdir( "Documents\IMI\Projet MoPSi\Images" )
pygame.init()

screen = pygame.display.set_mode((3*r, 3*r))
white = 250, 250, 250
screen.fill(white)




#Rafraîchissement de l'écran
pygame.display.flip()


p1 = pygame.image.load("piece_bleu.png").convert()
screen.blit(p1, (r,r))
screen.blit(p1, (2*r,r))
screen.blit(p1, (2*r,2*r))


pygame.display.flip()