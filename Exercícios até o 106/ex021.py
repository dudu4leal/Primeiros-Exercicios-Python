#Programa que abre e reproduz um arquivo mp3

import pygame

pygame.init()
pygame.mixer.music.load('LoucoPraVoltar-FilipeRet.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
