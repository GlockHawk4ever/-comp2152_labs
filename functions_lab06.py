import random
import os

def save_game(winner, hero_name=None, num_stars=0):
    """Saves the game outcome to save.txt."""
    with open("save.txt", "a") as file:
        if winner == "hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "monster":
            file.write("Monster has killed the hero previously.\n")

def hero_wins(hero_name, num_stars):
    """Handles hero winning the game by saving the result."""
    save_game("hero", hero_name, num_stars)
    print(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.")

def monster_wins():
    """Handles monster winning the game by saving the result."""
    save_game("monster")
    print("Monster has killed the hero previously.")

def battle(hero, monster):
    """Simulates a battle between hero and monster."""
    hero_strength = hero["combat_strength"]
    monster_strength = monster["combat_strength"]
    
    hero_roll = random.randint(1, 6) + hero_strength
    monster_roll = random.randint(1, 6) + monster_strength
    
    if hero_roll > monster_roll:
        stars = random.randint(1, 5)
        hero_wins(hero["name"], stars)
        return "hero", stars
    else:
        monster_wins()
        return "monster", 0
