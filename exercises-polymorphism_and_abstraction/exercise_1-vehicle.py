from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def fuel_consumption_with_ac(self):
        pass

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass



class Car(Vehicle):
    AC_ON = 0.9
    TANK_STATUS = 1

    def fuel_consumption_with_ac(self):
        return self.fuel_consumption + Car.AC_ON

    def drive(self, distance: int):
        total_fuel_needed = distance * self.fuel_consumption_with_ac()
        if self.fuel_quantity >= total_fuel_needed:
            self.fuel_quantity -= total_fuel_needed

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * Car.TANK_STATUS


class Truck(Vehicle):
    AC_ON = 1.6
    TANK_STATUS = 0.95

    def fuel_consumption_with_ac(self):
        return self.fuel_consumption + Truck.AC_ON

    def drive(self, distance: int):
        total_fuel_needed = distance * self.fuel_consumption_with_ac()
        if self.fuel_quantity >= total_fuel_needed:
            self.fuel_quantity -= total_fuel_needed

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * Truck.TANK_STATUS


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)


