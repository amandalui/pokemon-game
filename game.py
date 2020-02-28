import random
import time
import sys

from characters import *

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

num_error = "\nPlease enter a number within range."

# Main menu

def main_menu():
    global num_error
    main_menu = ['Catch pokemon', 'Quit']
    quit = "\nThanks for playing, " + player.name + "\n"
    select = None
    
    print("\nWhat would you like to do:")
    for x, value in enumerate(main_menu, 1):
        print('[' + str(x) + '] ' + value)
    
    while (type(select) is not int) or (select not in range(1,3)):
        try:
            select = input("\n> ")
            select = int(select)
            if int(select) == (main_menu.index("Catch pokemon") + 1):
                battle()
            elif int(select) == (main_menu.index("Quit") + 1):
                print(quit)
            else:
                print(num_error)
        except ValueError:
            print(num_error)

# Choose a starter pokemon

def starter_poke():
    global num_error
    starter_choice = None
    
    print("\n" + player.name +
        ", choose a starter pokemon (type a number):")
    
    for x, value in enumerate(wild_pokemon, 1):
        print('[' + str(x) + '] ' + value.name)
    
    while (type(starter_choice) is not int) or (starter_choice not in range(1,len(wild_pokemon)+1)):
        try:
            starter_choice = input("\n > ")
            starter_choice = int(starter_choice)
            if (starter_choice not in range(1,len(wild_pokemon)+1)):
                print(num_error)
        except ValueError:
            print(num_error)
    
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
        global num_error
        nonlocal player_pokemon
        select = None
        
        # Select a pokemon
        print("Which pokemon do you want to use?")

        # List the pokemon available in the Trainer's pokedex
        for x, value in enumerate(Trainer.pokedex, 1):
            if value.health > 0:
                print("[" + str(x) + "]" + " " + value.name + ": " + str(value.health))
        
        while (type(select) is not int) or (select not in range(1,len(Trainer.pokedex)+1)):
            try:
                select = input("> ")
                select = int(select)
                if select in range(1,len(Trainer.pokedex)+1):
                    player_pokemon = Trainer.pokedex[int(select) - 1]
                else:
                    print(num_error)
            except ValueError:
                print(num_error)
        print("\nGo get 'em " + player_pokemon.name + "! ◓")
        wait()
        player_attack()

        
    def opponent_attack():
        nonlocal player_pokemon
        nonlocal opponent
        nonlocal winner
        
        damage = random.randint(1, 5)

        attack = random.choice(opponent.attacks)

        print("\nOppposing " + opponent.name + " used " + str.title(attack.get("move")) + "!")
        
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
        global num_error
        nonlocal player_pokemon
        nonlocal opponent
        nonlocal winner
        select = None
        
        damage = random.randint(1, 5)

        print("\nChoose an attack:")

        for x, value in enumerate(player_pokemon.attacks, 1):
            print('[' + str(x) + '] ' + str.title(value.get("move")))
            
        while type(select) is not int or (select not in range(1,len(player_pokemon.attacks)+1)):
            try:
                select = input("> ")
                select = int(select)
                if select in range(1,len(player_pokemon.attacks)+1):
                    attack = player_pokemon.attacks[int(select) - 1]
                else:
                    print(num_error)
            except ValueError:
                print(num_error)
        
        wait()

        print("\n" + player_pokemon.name + " used " + str.title(attack.get("move")) + "!")
        
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
                print("◓ ◓ ◓ You caught 'em all! ◓ ◓ ◓ \nThanks for playing, " + player.name + "\n")
            else:
                main_menu()


    def menu_battle():
        global num_error
        choice = None
        menu_battle = ['Fight', 'Switch pokemon', 'Run']
        
        print("\nWhat's your move? \n")
        for x, value in enumerate(menu_battle, 1):
            print('[' + str(x) + '] ' + value)
        
        while (type(choice) is not int) or (choice not in range(1,len(menu_battle)+1)):
            try:
                choice = input("\n> ")
                choice = int(choice)
                if choice not in range(1,len(menu_battle)+1):
                    print(num_error)
            except ValueError:
                print(num_error)
                
        if choice == menu_battle.index("Fight") + 1:
            player_attack()
        elif choice == menu_battle.index("Switch pokemon") + 1:
            menu_pokedex()
        elif choice == menu_battle.index("Run") + 1:
            winner = opponent
            opponent.health = 10
            print("\nYou got away safely.")
            wait()
            main_menu()

    
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" + 
          "\nYou encountered a wild " + opponent.name + "!\n" + "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")

    menu_pokedex()
    



# The game

print("\n-----------------------------------------------------------" + 
                    "\nϞϞ(๑⚈ ․̫ ⚈๑)∩  Welcome to the world of Pokemon! n(๑⚈ ․̫ ⚈๑)ϞϞ \n" + 
                    "-----------------------------------------------------------")

player_name = input("\n\nWhat's your name? \n> ")

player = Trainer(player_name)

starter_poke()
main_menu()
