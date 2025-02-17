import os
from functions_lab06 import *

def load_game():
    """Loads the last saved game state from save.txt."""
    if not os.path.exists("save.txt"):
        return None
    
    with open("save.txt", "r") as file:
        lines = file.readlines()
        if lines:
            return lines[-1].strip()
    return None

def save_game(winner, hero_name=None, num_stars=0):
    """Saves the game outcome to save.txt."""
    with open("save.txt", "a") as file:
        if winner == "hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "monster":
            file.write("Monster has killed the hero previously.\n")

def adjust_combat_strength(hero, monster):
    """Adjusts combat strength based on the last game outcome."""
    last_game = load_game()
    if last_game:
        print("Previous Game Outcome:", last_game)
        if "Hero" in last_game and "stars" in last_game:
            stars = int(last_game.split("gained ")[-1].split(" stars")[0])
            if stars > 3:
                monster["combat_strength"] += 1
        elif "Monster" in last_game:
            hero["combat_strength"] += 1

def get_dream_levels():
    """Prompts the user to input a valid dream level between 0-3."""
    while True:
        try:
            levels = int(input("How many dream levels do you want to go down? (Enter a number 0-3): "))
            if 0 <= levels <= 3:
                return levels
            else:
                print("Invalid input. Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 3.")

# Example game flow (this would be part of the main game logic)
if __name__ == "__main__":
    hero = {"name": "Hero", "combat_strength": 5}
    monster = {"name": "Monster", "combat_strength": 4}
    
    adjust_combat_strength(hero, monster)
    print("Hero Strength:", hero["combat_strength"])
    print("Monster Strength:", monster["combat_strength"])
    
    dream_levels = get_dream_levels()
    print(f"You chose to go down {dream_levels} dream levels.")
    
    winner, stars = battle(hero, monster)
    save_game(winner, hero["name"], stars)
