from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = None
        dvd = None
        for curr_customer in self.customers:
            if curr_customer.id == customer_id:
                customer = curr_customer
        for curr_dvd in self.dvds:
            if curr_dvd.id == dvd_id:
                dvd = curr_dvd
        # first and second check if the dvd and customer exist in movie world
        if not dvd:
            return "Given dvd ID doesn't exist"

        if not customer:
            return "Given customer ID doesn't exist"
        # third check if the current customer has the DVD already at his possession
        for curr_dvd in customer.rented_dvds:
            if curr_dvd.id == dvd_id:
                return f"{customer.name} has already rented {curr_dvd.name}"
        # fourth check if the dvd is rented by someone else
        if dvd.is_rented:
            return "DVD is already rented"
        # fifth and final check if the customer is of age to acquire the DVD
        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = None
        dvd = None
        for curr_customer in self.customers:
            if curr_customer.id == customer_id:
                customer = curr_customer
        for curr_dvd in self.dvds:
            if curr_dvd.id == dvd_id:
                dvd = curr_dvd
        # first and second check if the dvd and customer exist in movie world
        if not dvd:
            return "Given dvd ID doesn't exist"

        if not customer:
            return "Given customer ID doesn't exist"
        # third check to see if the customer has the DVD in his possession
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for curr_customer in self.customers:
            result += f'{curr_customer}\n'

        for count, curr_dvd in enumerate(self.dvds, start=1):
            result += f'{curr_dvd}\n'

        return result

