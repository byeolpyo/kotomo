import pygame

def handle_events(event, pets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_0:
            pets.load_file('saves/data.json')
        if event.key == pygame.K_1:
            pets.save_file('saves/data.json')
        if event.key == pygame.K_n:
            pets.next_pet()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pets.current.feed()
        print(pets.pets[0].image)