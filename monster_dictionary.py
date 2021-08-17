import random


def monster_picker(dungeon_level):
    if dungeon_level is 1:
        return level_one()
    elif dungeon_level is 2:
        return level_two()
    elif dungeon_level is 3:
        return level_three()
    else:
        return print("Dungeon does not exist.")


def level_one():
    # Monster Dictionaries
    kobold = {
        "_id": 1,
        "element_type": 'earth',
        "hp": 5,
        "mp": 0,
        "strength": 5,
        "dexterity": 5,
        "intelligence": 5,
        "physical_defence": 5,
        "magical_defence": 5,
        "spells": {},
        "experience": 5,
        "drops": {'earth_core_1', 'kobold_fur'},
    }

    # Put all monsters in an array for random choice
    monster_array = [kobold, ]
    monster_randomizer = random.choice(monster_array)

    return monster_randomizer


def level_two():
    return


def level_three():
    return
