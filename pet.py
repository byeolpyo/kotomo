import pygame

def load_pets(save_file):
    return #list of pets that are saved

def draw_pet(pet, screen):
    font = pygame.font.Font('assets/fonts/ui_font.ttf', 24) #actual font name - CuteAurora
    name_string = "Current pet: {}".format(pet.name)
    petname = font.render(name_string, True, '#ffffff')
    screen.blit(pet.background, (0,0))
    screen.blit(pet.image, (192, 192))
    screen.blit(petname, (256, 32))

class Pet():
    def __init__(self, name, image, background, index):
        # pet attributes

        # constructor variables
        self.name = name
        self.image = pygame.image.load(image)
        self.background = pygame.image.load(background)
        self.index = index

        # 
        self.health = 100
        self.hunger = 100
        self.thirst = 100
        self.happiness = 100
