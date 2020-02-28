class Trainer:
    pokedex = []
    def __init__(self, name):
        self.name = name
        
class Pokemon:
    def __init__(self, name, health, element, weakness, attacks):
        self.name = name
        self.health = health
        self.element = element
        self.weakness = weakness
        self.attacks = attacks
        
def create_trainer():
    player_name = input("\n\nWhat's your name? \n> ")
    player = Trainer(player_name)