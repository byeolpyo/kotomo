import pygame

class Food():
    def __init__(
        self, 
        name,
        image, 
        hunger=10,
        thirst=0,
        happiness=0):

        self.name = name
        self.image = image
        
        self.hunger = hunger
        self.thirst = thirst
        self.happiness = happiness

    def get_values(self):
        return (self.hunger, self.thirst, self.happiness)
    
    def draw_food(self, screen):
        font = pygame.font.Font('assets/fonts/ui_font.ttf', 24) #actual font name - CuteAurora
         
        image = pygame.image.load(self.image)

        screen.blit(image, (208, 384))