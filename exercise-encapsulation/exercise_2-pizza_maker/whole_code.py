class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self._topping_type

    @topping_type.setter
    def topping_type(self, value):
        if not value:
            raise ValueError("The topping type cannot be an empty string")
        self._topping_type = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self._weight = value


class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
            self.flour_type = flour_type
            self.baking_technique = baking_technique
            self.weight = weight

    @property
    def flour_type(self):
        return self._flour_type

    @flour_type.setter
    def flour_type(self, value):
        if not value:
            raise ValueError("The flour type cannot be an empty string")
        self._flour_type = value

    @property
    def baking_technique(self):
        return self._baking_technique

    @baking_technique.setter
    def baking_technique(self, value):
        if not value:
            raise ValueError("The baking technique cannot be an empty string")
        self._baking_technique = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self._weight = value



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
            self_name = value

        @property
        def dough(self):
            return self._dough

        @dough.setter
        def dough(self, value):
            if not value:
                raise ValueError("You should add dough to the pizza")
            self.dough = value

        @property
        def max_number_of_toppings(self):
            return self._max_number_of_toppings

        @max_number_of_toppings.setter
        def max_number_of_toppings(self, value):
            if value <= 0:
                raise ValueError("The maximum number of toppings cannot be less or equal to zero")
            self._max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        elif topping in self.toppings:
            self.toppings[topping] += topping.weight
        else:
            self.toppings[topping] = topping.weight

    def calculate_total_weight(self):
        weight_accumulated = self.dough.weight
        for _, curr_weight in self.toppings.items():
            weight_accumulated += curr_weight
        return weight_accumulated
