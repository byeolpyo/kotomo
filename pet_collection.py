import json
from datetime import datetime

from collection import Collection
from pet import Pet

def init_pets():
    pets = [
        Pet('small puppy', 'assets/pets/p1.png', 'assets/backgrounds/b1.png'),
        Pet('cute cat', 'assets/pets/p2.png', 'assets/backgrounds/b2.png'),
        Pet('frog chan', 'assets/pets/p3.png', 'assets/backgrounds/b3.png'),
        Pet('bunny', 'assets/pets/p4.png', 'assets/backgrounds/b4.png'),
    ]
    return Pet_Collection(pets)

class Pet_Collection(Collection):
    def __init__(self, pets):
        # pet attributes
        super().__init__(pets)
        if self.size != 0:
            self.current = pets[self.current_index]
        else:
            self.current = Pet('NO PETS :c', 'assets/pets/DEFAULT.png', 'assets/backgrounds/DEFAULT.png')
         
    def load_file(self, file):
        self.vals = []
        with open(file, "r") as f:
            data = json.loads(f.read())
        for pet in data: 
            newpet = Pet(
                pet['name'], 
                pet['image'], 
                pet['background'], 
                pet['health'], 
                pet['hunger'], 
                pet['thirst'], 
                pet['happiness'],
                datetime.strptime(pet['last_feed_date'], '%Y-%m-%d %H:%M:%S.%f'),
                datetime.strptime(pet['last_water_date'], '%Y-%m-%d %H:%M:%S.%f'),
                datetime.strptime(pet['last_cuddle_date'], '%Y-%m-%d %H:%M:%S.%f')
            )
            newpet.update_status()
            self.insert_val(newpet)
        self.current = self.vals[0]

    def save_file(self, file):
        output = '['
        for pet in self.vals:
            json_pet = json.dumps(pet.__dict__, default=str)
            output = output + json_pet
            output = output + ',\n'
        output = output[:-2] + ']'
        with open(file, "w") as f:
            f.write(output)