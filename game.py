import random
import time
import sys

from characters import Trainer
from characters import Pokemon

HEALTH = 10

# Create attacks by type

fire_attacks = [
    {
        "move": "tackle",
        "element": "normal"
    },
    {
        "move": "ember",
        "element": "fire"
    }
]

water_attacks = [
    {
        "move": "tackle",
        "element": "normal"
    },
    {
        "move": "water gun",
        "element": "water"
    }
]

grass_attacks = [
    {
        "move": "tackle",
        "element": "normal"
    },
    {
        "move": "vine whip",
        "element": "grass"
    }
]


# Create wild pokemon

charmander = Pokemon(
    "Charmander",
    HEALTH,
    "fire",
    "water",
    fire_attacks)

squirtle = Pokemon(
    "Squirtle",
    HEALTH,
    "fire",
    "grass",
    water_attacks)

bulbasaur = Pokemon(
    "Bulbasaur",
    HEALTH,
    "grass",
    "fire",
    grass_attacks)

flareon = Pokemon(
    "Flareon",
    HEALTH,
    "fire",
    "water",
    fire_attacks)

vaporeon = Pokemon(
    "Vaporeon",
    HEALTH,
    "water",
    "grass",
    water_attacks)

leafeon = Pokemon(
    "Leafeon",
    HEALTH,
    "grass",
    "fire",
    grass_attacks)

growlithe = Pokemon(
    "Growlithe",
    HEALTH,
    "fire",
    "water",
    fire_attacks)

magikarp = Pokemon(
    "Magikarp",
    HEALTH,
    "water",
    "grass",
    water_attacks)

oddish = Pokemon(
    "Oddish",
    HEALTH,
    "grass",
    "fire",
    grass_attacks)

ponyta = Pokemon(
    "Ponyta",
    HEALTH,
    "fire",
    "water",
    fire_attacks)

psyduck = Pokemon(
    "Psyduck",
    HEALTH,
    "water",
    "grass",
    water_attacks)

tangela = Pokemon(
    "Tangela",
    HEALTH,
    "grass",
    "fire",
    grass_attacks)

wild_pokemon = [
    charmander,
    squirtle,
    bulbasaur,
    flareon,
    vaporeon,
    leafeon,
    growlithe,
    magikarp,
    oddish,
    ponyta,
    psyduck,
    tangela
]


# Choose a starter pokemon

def starter_poke():
    starter_choice = input("\n" + player.name +
        ", choose a starter pokemon (type a number):" +
        "\n[1] " + wild_pokemon[0].name + 
        "\n[2] " + wild_pokemon[1].name +
        "\n[3] " + wild_pokemon[2].name +
        "\n[4] " + wild_pokemon[3].name +
        "\n[5] " + wild_pokemon[4].name +
        "\n[6] " + wild_pokemon[5].name +
        "\n[7] " + wild_pokemon[6].name +
        "\n[8] " + wild_pokemon[7].name +
        "\n[9] " + wild_pokemon[8].name +
        "\n[10] " + wild_pokemon[9].name +
        "\n[11] " + wild_pokemon[10].name +
        "\n[12] " + wild_pokemon[11].name + 
        "\n > "
    )
    
    for x, value in enumerate(wild_pokemon):
        if int(starter_choice) == (x + 1):
            print("\nYou chose " + wild_pokemon[x].name + ", great choice.")
            player.pokedex.append(wild_pokemon.pop(x))
            
def wait():
    wait = "\n...\n"
    for x in wait:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.5)

# Battle
def battle():
    
    winner = None
    opponent = random.choice(wild_pokemon)
    player_pokemon = None
    damage = 0


    def status():
        wait()
        print("\nStatus: \n" + player_pokemon.name + " health: " + str(player_pokemon.health))
        print("Opposing " + opponent.name + " health: " + str(opponent.health))


    def menu_pokedex():
        nonlocal player_pokemon
        
        # Select a pokemon
        print("Which pokemon do you want to use?")

        # List the pokemon available in the Trainer's pokedex
        for x, value in enumerate(Trainer.pokedex):
            if value.health > 0:
                print("[" + str(x) + "]" + " " + value.name + ": " + str(value.health))

        player_pokemon = Trainer.pokedex[int(input("> "))]
        print("\nGo get 'em " + player_pokemon.name + "! ◓")
        wait()
        player_attack()

        
    def opponent_attack():
        nonlocal player_pokemon
        nonlocal opponent
        nonlocal winner
        
        damage = random.randint(1, 5)

        attack = random.choice(opponent.attacks)

        print("\nOppposing " + opponent.name + " used " + attack.get("move") + "!")
        
        # if the move equals the opponents weakness, double the damage
        if attack.get("element") == player_pokemon.weakness:
            damage *= 2
        print("Damage dealt: " + str(damage) + " ✷")

        player_pokemon.health -= damage
        status()
        
        wait()
        
        if player_pokemon.health > 0:
            menu_battle()
        elif player_pokemon.health <= 0 and len(Trainer.pokedex) > 1:
            print("\n" + player_pokemon.name + " fainted.\n")
            menu_pokedex()
        elif player_pokemon.health <= 0:
            winner = opponent
            print("\n" + player_pokemon.name + " fainted.")
            print("Game over...")
        
        
    def player_attack():
        nonlocal player_pokemon
        nonlocal opponent
        nonlocal winner
        
        damage = random.randint(1, 5)

        print("\nChoose an attack:")
        for x, value in enumerate(player_pokemon.attacks):
            print("[" + str(x) + "] " + player_pokemon.attacks[int(x)].get("move"))

        attack = player_pokemon.attacks[int(input("> "))]
        
        wait()

        print("\n" + player_pokemon.name + " used " + attack.get("move") + "!")
        
        # if the move equals the opponents weakness, double the damage
        if attack.get("element") == opponent.weakness:
            damage *= 2
        print("Damage dealt: " + str(damage) + " ✷")

        opponent.health -= damage
        
        wait()
        
        if opponent.health > 0:
            opponent_attack()
        elif opponent.health <= 0:
            winner = player_pokemon
            print("\nOpposing " + opponent.name + " fainted.")
            print("You caught " + opponent.name + "! \n")
            Trainer.pokedex.append(wild_pokemon.pop(wild_pokemon.index(opponent)))
            for x in Trainer.pokedex:
                x.health = HEALTH
            
            if len(wild_pokemon) == 0:
                print("◓ ◓ ◓ You caught 'em all! ◓ ◓ ◓ \nThanks for playing, " + player_name + "\n")
            else:
                main_menu()


    def menu_battle():
        
        choice = input("\nWhat's your move? \n" +
                        "[1] Fight \n" +
                        "[2] Switch pokemon \n" +
                        "[3] Run" +
                        "\n> ")
        if int(choice) == 1:
            player_attack()
        elif int(choice) == 2:
            menu_pokedex()
        elif int(choice) == 3:
            winner = opponent
            opponent.health = 10
            print("\nYou got away safely.")
            wait()
            main_menu()

    
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" + 
          "\nYou encountered a wild " + opponent.name + "!\n" + "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")

    menu_pokedex()
    

            
# Main menu

def main_menu():
    select = input("\nWhat would you like to do: \n[1] Catch pokemon \n[2] Quit \n> ")
    
    quit = "\nThanks for playing, " + player_name + "\n"
    
    if int(select) == 1:
        battle()
    else:
        print(quit)

# The game

player_name = input("\n-----------------------------------------------------------" + 
                    "\nϞϞ(๑⚈ ․̫ ⚈๑)∩  Welcome to the world of Pokemon! n(๑⚈ ․̫ ⚈๑)ϞϞ \n" + 
                    "-----------------------------------------------------------" + 
                    "\n\nWhat's your name? \n> ")

player = Trainer(player_name)

starter_poke()
main_menu()
