from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        else:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for curr_player in self.__players:
            if curr_player.name == player_name:
                self.__players.remove(curr_player)
                return curr_player
        return f'Player {player_name} not found'


p = Player("Pall", 1, 3, 5, 7)
print("\ncalling the __str__ method")
print(p)

print("\nAbout the team")
t = Team("Best", 10)
print("Team name:", t._Team__name)
print("Teams points:", t._Team__rating)
print("Teams players:", len(t._Team__players))
print(t.add_player(p))
print(t.add_player(p))
print("Teams players:", len(t._Team__players))
print(t.remove_player("Pall"))
print(t.remove_player("Pall"))
