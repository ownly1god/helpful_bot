import random

character_names = [
    'Erik',
    'Alishba',
    'Zaki',
    'Ezmae',
    'Evie-May',
    'Ephraim',
    'Peggy',
    'Conan',
    'Claudia'
]


def character_generation():
    name = random.choice(character_names)

    hp = 10
    mp = 100

    strength = random.randrange(11)
    while strength < 6:
        strength = random.randrange(11)

    dexterity = random.randrange(11)
    while dexterity < 6:
        dexterity = random.randrange(11)

    intelligence = random.randrange(11)
    while intelligence < 6:
        intelligence = random.randrange(11)

    experience = 0

    return name, hp, mp, strength, dexterity, intelligence, experience
