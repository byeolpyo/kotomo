import pygame, sys
from pet import Pet, draw_pet

# initial pygame config

pygame.init()
pygame.display.set_caption('kotomo')
icon = pygame.image.load('assets/window_icon.png')
pygame.display.set_icon(icon)
clock=pygame.time.Clock()

screen=pygame.display.set_mode((512,512))

# variables

screensize = pygame.display.get_window_size()
running = True


# load pets from a local save
pet1 = Pet('yae miko', 'assets/pets/p1.png', 'assets/backgrounds/b1.png', 1)
pet2 = Pet('cute cat', 'assets/pets/p2.png', 'assets/backgrounds/b2.png', 2)

# set current pet

current_pet = pet3


# music :3

bgm = pygame.mixer.Sound('assets/sound/bgm.wav')
bgm.play(-1)


# main game loop

while running:
    draw_pet(current_pet, screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    clock.tick(60)
    pygame.display.update()