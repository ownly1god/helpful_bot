import random


def receiving_monsters(encounter, character):
    x = len(encounter) - 1
    experience_gained = 0
    character_alive = True

    # THERE IS SOMETHING WRONG WITH THIS LOOP

    while 0 <= x:
        experience, character_alive = character_combat(encounter[x], character)

        if character_alive is True:
            experience_gained = experience + experience_gained
        else:
            return experience_gained, character_alive
        x = x - 1

    return experience_gained, character_alive


def character_combat(monster, character):
    character_alive = True
    character_dex = int(character[4])
    monster_dex = int(monster[4])

    character_attack_speed = (1/character_dex) + ((1/character_dex)*0)
    monster_attack_speed = (1/monster_dex) + ((1/monster_dex)*0)

    monster_hp = monster['hp']
    character_hp = character['hp']

    while monster_hp > 0 and character_hp > 0:
        character_auto_attack = random.randrange(int(character['strength']) - int(monster['physical_defence']))
        if character_auto_attack < 0:
            character_auto_attack = 0

        monster_auto_attack = random.randrange(int(monster['strength']) - int(character['physical_defence']))
        if monster_auto_attack < 0:
            monster_auto_attack = 0

        monster_hp = monster_hp - (character_auto_attack * character_attack_speed)
        character_hp = character_hp - (monster_auto_attack * monster_attack_speed)

        if monster_hp < 0:
            monster_hp = 0

        if character_hp < 0:
            character_hp = 0

    if character_hp is 0:
        experience = monster['experience']
        character_alive = True

    if monster_hp is 0:
        experience = 0
        character_alive = False

    return experience, character_alive
