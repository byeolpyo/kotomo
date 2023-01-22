import pygame
from events import handle_events, is_event_quit
from ui import draw_ui

from pet_collection import Pet_Collection, init_pets
from food_collection import init_foods

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

# initial pets setup - load pets from a local save

pets = Pet_Collection([])
try:
    pets.load_file('saves/data.json')
except:
    print("nie znaleziono pliku w saves, tworze nowy...")
    pets = init_pets()

# initial food setup (food is hardcoded in)

foods = init_foods()

# music

bgm = pygame.mixer.Sound('assets/sound/bgm.wav')
bgm.play(-1)


# main game loop

while running:
    pets.current.draw_pet(screen)
    foods.current.draw_food(screen)
    draw_ui(screen)
    for event in pygame.event.get():
        handle_events(event, pets, foods)
        if is_event_quit(event):
            if pets.size != 0:
                print('zapisuje...')
                pets.save_file('saves/data.json')
            print('wychodze...')
            running = False
 
    clock.tick(60)
    pygame.display.update()