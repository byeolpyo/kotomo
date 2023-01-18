import pygame
from datetime import datetime

class Pet():
    def __init__(self, name, image, background):
        # pet attributes

        # constructor variables
        self.name = name
        self.image = image
        self.background = background

        # 
        self.health = 100
        self.hunger = 100
        self.thirst = 100
        self.happiness = 100

        self.last_feed_date = datetime.now() 
        self.last_water_date = datetime.now()
        self.last_cuddle_date = datetime.now()

 
    def modify_health(self, value):
        self.health = self.health + value
        if (self.health > 100):
            self.health = 100
        if (self.health < 0):
            self.health = 0

    def modify_hunger(self, value):
        self.hunger = self.hunger + value
        if (self.hunger > 100):
            self.hunger = 100
        if (self.hunger < 0):
            self.hunger = 0
        self.recalculate_health()
    
    def modify_thirst(self, value):
        self.thirst = self.thirst + value
        if (self.thirst > 100):
            self.thirst = 100
        if (self.thirst < 0):
            self.thirst = 0
        self.recalculate_health()
    
    def modify_happiness(self, value):
        self.happiness = self.happiness + value
        if (self.happiness > 100):
            self.happiness = 100
        if (self.happiness < 0):
            self.happiness = 0
        self.recalculate_health()
        
    def recalculate_health(self):
        self.health = (self.hunger*self.thirst*self.happiness) ** (1/2)
        self.health = int(self.health/10)

    def draw_pet(self, screen):
        font = pygame.font.Font('assets/fonts/ui_font.ttf', 24) #actual font name - CuteAurora
        name_string = "current pet: {}".format(self.name)
        status_string = "health: {}".format(self.health)
        petname = font.render(name_string, True, '#ffffff')
        status  = font.render(status_string, True, '#ffffff')
        image = pygame.image.load(self.image)
        background = pygame.image.load(self.background)
        screen.blit(background, (0,0)) 
        screen.blit(image, (192, 192))
        screen.blit(petname, (256, 32))
        screen.blit(status, (256, 64))