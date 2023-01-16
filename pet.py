import pygame

class Pet():
    def __init__(self, name="empty", image=" ", background=" "):
        # pet attributes

        # constructor variables
        self.name = name
        self.image = pygame.image.load(image)
        self.background = pygame.image.load(background)

        # 
        self.health = 100
        self.hunger = 100
        self.thirst = 100
        self.happiness = 100


    def draw_pet(self, screen):
        font = pygame.font.Font('assets/fonts/ui_font.ttf', 24) #actual font name - CuteAurora
        name_string = "current pet: {}".format(self.name)
        petname = font.render(name_string, True, '#ffffff')
        screen.blit(self.background, (0,0))
        screen.blit(self.image, (192, 192))
        screen.blit(petname, (256, 32))