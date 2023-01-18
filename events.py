import pygame

def handle_events(event, pets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_l:
            pets.load_file('saves/data.json')
        if event.key == pygame.K_s:
            pets.save_file('saves/data.json')
        if event.key == pygame.K_n:
            pets.next_pet()
        if event.key == pygame.K_1:
            pets.current.feed()
        if event.key == pygame.K_2:
            pets.current.water()
        if event.key == pygame.K_3:
            pets.current.cuddle()
#    if event.type == pygame.MOUSEBUTTONDOWN: