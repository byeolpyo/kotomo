import pygame
import json

from pet import Pet

class Pet_Set():
    def __init__(self, pets):
        # pet attributes
        self.pets = pets
        self.current_index = 0
        self.size = len(pets)
        if self.size != 0:
            self.current = pets[self.current_index]
        else:
            self.current = Pet('NO PETS :c', 'assets/pets/DEFAULT.png', 'assets/backgrounds/DEFAULT.png')
        

    def insert_pet(self, pet):
        if self.size == 0:
            self.size = 1
            self.pets = [pet]
            self.current = pet
            return
        self.pets.append(pet)
        self.size = self.size + 1

    def next_pet(self):
        if self.size == 0:
            return
        self.current_index = self.current_index + 1 
        self.current_index = self.current_index % self.size
        self.current = self.pets[self.current_index]
    
    def change_pet(self, index):
        if self.size == 0:
            return
        if index >= self.size:
            return
        self.current_index = index 
        self.current = self.pets[self.current_index]
    
    def load_file(self, file):
        self.pets = []
        with open(file, "r") as f:
            data = json.loads(f.read())
        for pet in data:
            newpet = Pet(pet['name'], pet['image'], pet['background'])
            self.insert_pet(newpet)
        self.current = self.pets[0]
    def save_file(self, file):
        json_str = json.dumps(self.pets[0])