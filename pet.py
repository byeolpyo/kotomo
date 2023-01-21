import pygame
from datetime import datetime

def timedif_hours(then_date):
    time_dif = datetime.now() - then_date
    return time_dif.total_seconds()/3600

class Pet():
    def __init__(
        self, 
        name, 
        image, 
        background, 
        health = 100, 
        hunger = 100, 
        thirst = 100, 
        happiness = 100, 
        last_feed_date = datetime.now(),
        last_water_date = datetime.now(),
        last_cuddle_date = datetime.now(),
        is_alive = True
        ):

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

        self.is_alive = is_alive

    def modify_health(self, value):
        self.health = self.health + value
        if (self.health > 100):
            self.health = 100
        if (self.health < 0):
            self.health = 0

    def modify_hunger(self, value):
        before = self.hunger
        self.hunger = before + value
        if (self.hunger > 100):
            self.hunger = 100
        if (self.hunger < 0):
            self.hunger = 0
        self.hunger = round(self.hunger)
        if self.hunger != before:
            self.last_feed_date = datetime.now()
    
    def modify_thirst(self, value):
        before = self.thirst
        self.thirst = before + value
        if (self.thirst > 100):
            self.thirst = 100
        if (self.thirst < 0):
            self.thirst = 0
        self.thirst = round(self.thirst)
        if self.thirst != before:
            self.last_water_date = datetime.now()
    
    def modify_happiness(self, value):
        before = self.happiness
        self.happiness = before + value
        if (self.happiness > 100):
            self.happiness = 100
        if (self.happiness < 0):
            self.happiness = 0
        self.happiness = round(self.happiness)
        if self.happiness != before:
            self.last_cuddle_date = datetime.now()
        
    def update_health(self):
        self.health = (self.hunger*self.thirst*self.happiness) ** (1/2)
        self.health = round(self.health/10)

    def update_status(self):
        self.modify_hunger(timedif_hours(self.last_feed_date)*(-4))
        self.modify_thirst(timedif_hours(self.last_water_date)*(-2))
        self.modify_happiness(timedif_hours(self.last_cuddle_date)*(-8))
        self.update_health()
        if self.health == 0:
            self.is_alive = False

    def feed(self, food):
        if self.is_alive == False:
            return 
        vals = food.get_values()
        if vals[0] > 0:
            self.modify_hunger(self.hunger+vals[0])
            self.last_feed_date = datetime.now()
        if vals[1] > 0:
            self.modify_thirst(self.thirst+vals[1])
            self.last_water_date = datetime.now()
        if vals[2] > 0:
            self.modify_happiness(self.happiness+vals[2])
        self.update_health() 
    
    def cuddle(self):
        if self.is_alive == False:
            return 
        self.modify_happiness(self.happiness+20)
        self.last_cuddle_date = datetime.now()
        self.update_health() 

    def reset(self):
        self.health = 100 
        self.hunger = 100
        self.thirst = 100 
        self.happiness = 100 
        self.last_feed_date = datetime.now()
        self.last_water_date = datetime.now()
        self.last_cuddle_date = datetime.now()
        self.is_alive = True
        self.update_status()
    
    def draw_pet(self, screen):
        self.update_status()
        font = pygame.font.Font('assets/fonts/ui_font.ttf', 24) #actual font name - CuteAurora
        
        name_s = "current pet: {}".format(self.name)
        health_s = "health: {}".format(self.health)
        hunger_s = "hunger: {}".format(self.hunger)
        thirst_s = "thirst: {}".format(self.thirst)
        happiness_s = "happiness: {}".format(self.happiness)
        death_s = "this pet is dead :C"

        name = font.render(name_s, True, '#ffffff')
        health = font.render(health_s, True, '#ffffff')
        hunger = font.render(hunger_s, True, '#ffffff')
        thirst = font.render(thirst_s, True, '#ffffff')
        happiness = font.render(happiness_s, True, '#ffffff')
        death = font.render(death_s, True, '#ffffff')
        
        image = pygame.image.load(self.image)
        background = pygame.image.load(self.background)
        
        screen.blit(background, (0,0)) 
        screen.blit(image, (192, 192))
        screen.blit(name, (32, 32))
        screen.blit(health, (32, 64))
        screen.blit(hunger, (32, 96))
        screen.blit(thirst, (32, 128))
        screen.blit(happiness, (32, 160))
        if self.is_alive == False:
            screen.blit(death, (160, 340))