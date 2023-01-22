import pygame

def cursor_in_area(p1, p2):
    pos = pygame.mouse.get_pos()
    xmin = min(p1[0], p2[0])
    xmax = max(p1[0], p2[0])
    ymin = min(p1[1], p2[1])
    ymax = max(p1[1], p2[1])
    if xmin < pos[0] and pos[0] < xmax and ymin < pos[1] and pos[1] < ymax:
        return True

def handle_events(event, pets, foods):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_n:
            pets.next_val()
        
        if event.key == pygame.K_r and pygame.key.get_mods() & pygame.KMOD_CTRL:
            pets.current.reset()

    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == True:
        if cursor_in_area((192, 192), (320, 320)):
            pets.current.cuddle()
        if cursor_in_area((208, 384), (304, 480)):
            pets.current.feed(foods.current)
        
        if cursor_in_area((160, 408), (208, 456)):
            foods.previous_val()
        if cursor_in_area((304, 408), (352, 456)):
            foods.next_val()
        
        if cursor_in_area((384, 32), (480, 80)):
            pets.next_val()

def is_event_quit(event):
    if event.type == pygame.QUIT:
        return True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            return True
    return False