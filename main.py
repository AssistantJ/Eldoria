from player import create_player
from combat import start_battle
from dialogue import intro_dialogue

print("Welcome to Eldoria")

player = create_player()
intro_dialogue(player)
start_battle(player)
