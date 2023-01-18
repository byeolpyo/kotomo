import pygame
from datetime import datetime

def timedif_hours(then_date):
    time_dif = datetime.now() - then_date
    print(time_dif.total_seconds()/3600)
    return time_dif.total_seconds()/3600

class Pet():
    def __init__(
        self, 
        name, 
        image, 
        background, 
        health=100, 
        hunger = 100, 
        thirst = 100, 
        happiness = 100, 
        last_feed_date = datetime.now(),
        last_water_date = datetime.now(),
        last_cuddle_date = datetime.now(),
        ):
        # pet attributes

        # constructor variables
        self.name = name
        self.image = image
        self.background = background

        self.health = health
        self.hunger = hunger
        self.thirst = thirst
        self.happiness = happiness

        self.last_feed_date = last_feed_date
        self.last_water_date = last_water_date
        self.last_cuddle_date = last_cuddle_date
 
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
        self.hunger = int(self.hunger)
    
    def modify_thirst(self, value):
        self.thirst = self.thirst + value
        if (self.thirst > 100):
            self.thirst = 100
        if (self.thirst < 0):
            self.thirst = 0
        self.thirst = int(self.thirst)
    
    def modify_happiness(self, value):
        self.happiness = self.happiness + value
        if (self.happiness > 100):
            self.happiness = 100
        if (self.happiness < 0):
            self.happiness = 0
        self.happiness = int(self.happiness)
        
    def update_health(self):
        self.health = (self.hunger*self.thirst*self.happiness) ** (1/2)
        self.health = int(self.health/10)

    def update_status(self):
        self.modify_hunger(timedif_hours(self.last_feed_date)*(-4))
        self.modify_thirst(timedif_hours(self.last_water_date)*(-2))
        self.modify_happiness(timedif_hours(self.last_cuddle_date)*(-8))
        self.update_health()

    def feed(self):
        self.modify_hunger(10)
        self.last_feed_date = datetime.now()
        self.update_health() 

    def water(self):
        self.modify_thirst(10)
        self.last_water_date = datetime.now()
        self.update_health() 
    
    def cuddle(self):
        self.modify_happiness(10)
        self.last_cuddle_date = datetime.now()
        self.update_health() 

    def draw_pet(self, screen):
        font = pygame.font.Font('assets/fonts/ui_font.ttf', 24) #actual font name - CuteAurora
        name_string = "current pet: {}".format(self.name)
        health = "health: {}".format(self.health)
        hunger = "hunger: {}".format(self.hunger)
        thirst = "thirst: {}".format(self.thirst)
        happiness = "happiness: {}".format(self.happiness)
        petname = font.render(name_string, True, '#ffffff')
        health_s = font.render(health, True, '#ffffff')
        hunger_s = font.render(hunger, True, '#ffffff')
        thirst_s = font.render(thirst, True, '#ffffff')
        happiness_s = font.render(happiness, True, '#ffffff')
        image = pygame.image.load(self.image)
        background = pygame.image.load(self.background)
        screen.blit(background, (0,0)) 
        screen.blit(image, (192, 192))
        screen.blit(petname, (256, 32))
        screen.blit(health_s, (256, 64))
        screen.blit(hunger_s, (256, 96))
        screen.blit(thirst_s, (256, 128))
        screen.blit(happiness_s, (256, 162))