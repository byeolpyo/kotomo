import pygame, sys
from pet import Pet
from pet_set import Pet_Set

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
pets.insert_pet(Pet('yae miko', 'assets/pets/p1.png', 'assets/backgrounds/b1.png'))
pets.insert_pet(Pet('cute cat', 'assets/pets/p2.png', 'assets/backgrounds/b2.png'))
pets.insert_pet(Pet('frog chan', 'assets/pets/p3.png', 'assets/backgrounds/b3.png'))

# music :3

bgm = pygame.mixer.Sound('assets/sound/bgm.wav')
bgm.play(-1)


# main game loop

while running:
    pets.current.draw_pet(screen)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                pets.change_pet(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pets.next_pet()
            #pets.insert_pet(Pet('yae miko', 'assets/pets/p1.png', 'assets/backgrounds/b1.png'))
        if event.type == pygame.QUIT:
            running = False
 
    clock.tick(60)
    pygame.display.update()