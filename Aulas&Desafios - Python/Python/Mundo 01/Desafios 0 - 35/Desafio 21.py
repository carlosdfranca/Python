#Faça um pregrama em Python qye abra e reproduza o áudio de um mp3.
import pygame
pygame.cdrom.init()
pygame.music.load('Desafio 21.mp3')
pygame.cdrom.play()
pygame.event.wait()