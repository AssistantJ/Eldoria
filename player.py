def create_player():
    name = input("Enter your name: ")
    classes = ["Warrior","Rogue","Mage","Ranger","Cleric","Summoner"]
    print("Choose class:")
    for i,c in enumerate(classes,1):
        print(f"{i}. {c}")
    choice = int(input("> "))

    personality = input("Describe personality: ").lower()

    traits = {"anti_magic":0,"aggression":0,"honor":0}

    if "magic" in personality and "hate" in personality:
        traits["anti_magic"] = 10
    if "ruthless" in personality:
        traits["aggression"] = 8
    if "honor" in personality:
        traits["honor"] = 8

    return {
        "name": name,
        "class": classes[choice-1],
        "hp": 100,
        "damage": 15,
        "traits": traits
    }
