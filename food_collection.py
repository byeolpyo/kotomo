from collection import Collection
from food import Food

def init_foods():
    foods = [
        Food('pepsi', 'assets/foods/f1.png', 0, 5, -2),
        Food('candy', 'assets/foods/f2.png', 2, 0, 2),
        Food('borgir', 'assets/foods/f3.png', 10, 0, 0)
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