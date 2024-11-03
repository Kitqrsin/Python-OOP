class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity_to_decrease: int):
        if self.quantity >= quantity_to_decrease:
            self.quantity -= quantity_to_decrease

    def increase(self, quantity_to_increase: int):
        self.quantity += quantity_to_increase

    def __repr__(self):
        return self.name
