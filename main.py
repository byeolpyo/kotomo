import pygame
from pet_collection import Pet_Collection
from events import handle_events, is_event_quit

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

pets = Pet_Collection([])
pets.load_file('saves/data.json')

# music

bgm = pygame.mixer.Sound('assets/sound/bgm.wav')
bgm.play(-1)


# main game loop

while running:
    pets.current.draw_pet(screen)
    for event in pygame.event.get():
        handle_events(event, pets)
        if is_event_quit(event):
            if pets.size != 0:
                print('zapisuje...')
                pets.save_file('saves/data.json')
            print('wychodze...')
            running = False
 
    clock.tick(60)
    pygame.display.update()