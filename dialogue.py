def intro_dialogue(player):
    print("\nA mysterious mage approaches...")

    if player["traits"]["anti_magic"] > 5:
        print(f"{player['name']}: 'Magic is pathetic. Leave.'")
    else:
        print(f"{player['name']}: 'What do you want?'')
