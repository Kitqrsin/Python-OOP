from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self._name = value

    @property
    def dough(self):
        return self._dough

    @dough.setter
    def dough(self, value):
        if not value:
            raise ValueError("You should add dough to the pizza")
        self._dough = value

    @property
    def max_number_of_toppings(self):
        return self._max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self._max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings.keys()) == self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        elif topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        weight_accumulated = self.dough.weight
        for curr_weight in self.toppings.values():
            weight_accumulated += curr_weight
        return weight_accumulated

