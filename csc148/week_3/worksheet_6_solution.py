import random
from datetime import datetime
from worksheet_6_starter_code import Vehicle, SuperDuperManager

"""
Question 7
"""

class Car(Vehicle):

    def __init__(self, initial_fuel: int,
                    initial_position: Tuple[int, int] = (0,0)) -> None:
        super().__init__()

    def fuel_needed(self, new_x: int, new_y: int) -> int:

        old_x = self.position[0]
        old_y = self.position[1]

        delta_x = abs(old_x - new_x)
        delta_y = abs(old_y - new_y)

        return delta_x + delta_y


"""
Question 8.1
"""

class Helicopter(Vehicle):

    def __init__(self, initial_fuel: int,
                    initial_position: Tuple[int, int] = (0,0)) -> None:
        super().__init__()

    def fuel_needed(self, new_x: int, new_y: int) -> int:

        old_x = self.position[0]
        old_y = self.position[1]

        delta_x = abs(old_x - new_x)
        delta_y = abs(old_y - new_y)

        return math.ceil(math.sqrt(delta_x**2 + delta_y**2))


"""
Question 8.2
"""

 class UnreliableMagicCarpet:

    def __init__(self, initial_fuel: int,
                    initial_position: Tuple[int, int] = (0,0)) -> None:
        super().__init__()

        random.seed(datetime.now())
        self.position = (random.randint(-100,100), random.randint(-100,100))

    def move(self, new_x: int, new_y: int) -> None:
        self.position = (random.randint(-100,100), random.randint(-100,100))
