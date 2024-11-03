class Vehicle:
    fuel_consumption = 1.25
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel  # quantity of fuel
        self.horse_power = horse_power

    def drive(self, kilometers: int):
        fuel_needed = kilometers * self.fuel_consumption
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed

