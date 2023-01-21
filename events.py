import pygame

def cursor_in_area(p1, p2):
    pos = pygame.mouse.get_pos()
    xmin = min(p1[0], p2[0])
    xmax = max(p1[0], p2[0])
    ymin = min(p1[1], p2[1])
    ymax = max(p1[1], p2[1])
    if xmin < pos[0] and pos[0] < xmax and ymin < pos[1] and pos[1] < ymax:
        return True

def handle_events(event, pets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_l:
            pets.load_file('saves/data.json')
        if event.key == pygame.K_s:
            pets.save_file('saves/data.json')
        if event.key == pygame.K_n:
            pets.next_val()
        if event.key == pygame.K_1:
            pets.current.feed()
        if event.key == pygame.K_2:
            pets.current.water()
        
        if event.key == pygame.K_r and pygame.key.get_mods() & pygame.KMOD_CTRL:
            pets.current.reset()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if cursor_in_area((192, 192), (320, 320)) and pygame.mouse.get_pressed()[0] == True:
            pets.current.cuddle()

def is_event_quit(event):
    if event.type == pygame.QUIT:
        return True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            return True
    return False