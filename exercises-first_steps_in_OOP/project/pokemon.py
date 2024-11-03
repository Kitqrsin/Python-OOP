class Pokemon:
    def __init__(self, name, health):
        self.pokemon_name = name
        self.pokemon_health = health

    def pokemon_details(self):
        return f'{self.pokemon_name} with health {self.pokemon_health}'
