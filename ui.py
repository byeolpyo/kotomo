import pygame

def draw_ui(screen):
    arrow_left = pygame.image.load('assets/arrow_left.png')
    arrow_right = pygame.image.load('assets/arrow_right.png')
    change_pet = pygame.image.load('assets/change_pet.png')

    screen.blit(arrow_left, (160, 408))
    screen.blit(arrow_right, (304, 408))
    screen.blit(change_pet, (384, 32))