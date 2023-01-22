from collection import Collection
from food import Food

def init_foods():
    foods = [
        Food('ice cream', 'assets/foods/f1.png', 2, 0, 5),
        Food('water', 'assets/foods/f2.png', 0, 10, 2),
        Food('pancake', 'assets/foods/f3.png', 10, 0, 0)
    ]
    return Food_Collection(foods)

class Food_Collection(Collection):
    def __init__(self, foods):
        # pet attributes
        super().__init__(foods)
        self.current = self.vals[0]

    def previous_val(self):
        if self.size == 0:
            return
        self.current_index = self.current_index - 1 
        self.current_index = self.current_index % self.size
        self.current = self.vals[self.current_index]