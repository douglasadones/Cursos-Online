# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('abc.mp3')
pygame.mixer.music.play()
input('preciso por esse input pra musica rolar D: ')
