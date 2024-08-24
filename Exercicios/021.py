import pygame

pygame.init()
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()
input() #após as ultimas atualizações, se faz necessário o uso do input() antes do wait.
pygame.event.wait()