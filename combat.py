import random

def start_battle(player):
    enemy = {"name":"Dark Mage","hp":80,"damage":12,"type":"magic"}

    print(f"\nA {enemy['name']} appears!")

    while player["hp"] > 0 and enemy["hp"] > 0:
        input("Press Enter to attack...")
        enemy["hp"] -= player["damage"]
        print(f"You hit the enemy! Enemy HP: {enemy['hp']}")

        if enemy["hp"] <= 0:
            break

        dmg = enemy["damage"]

        if player["traits"]["anti_magic"] > 5:
            dmg = int(dmg * 0.5)
            print("Your hatred of magic reduces damage!")

        player["hp"] -= dmg
        print(f"Enemy hits you! Your HP: {player['hp']}")

    if player["hp"] > 0:
        print("\nYou won the battle!")
    else:
        print("\nYou were defeated...")
