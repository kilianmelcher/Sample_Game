import pygame

pygame.init()

bullet_sound = pygame.mixer.Sound("bullet.wav")
hit_sound = pygame.mixer.Sound("hit.wav")
jump_sound = pygame.mixer.Sound('jump.wav')
background_music = pygame.mixer.music.load("music.mp3")