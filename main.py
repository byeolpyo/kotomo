import pygame, sys
from pet import Pet
from pet_set import Pet_Set
from events import handle_events

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
pets = Pet_Set([])

# music :3

bgm = pygame.mixer.Sound('assets/sound/bgm.wav')
bgm.play(-1)


# main game loop

while running:
    pets.current.draw_pet(screen)
    for event in pygame.event.get():
        handle_events(event, pets)
        if event.type == pygame.QUIT:
            print('wychodzeeee')
            running = False
 
    clock.tick(60)
    pygame.display.update()