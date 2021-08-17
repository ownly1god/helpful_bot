import monster_dictionary
import combat
import random


def explore_selected_dungeon(selected_character, selected_dungeon):
    encounter_size = random.randrange(2)
    encounter_initial_loop = 0
    encounter_array = []

    if encounter_size is 0:
        encounter_size = 1

    while encounter_initial_loop < encounter_size:
        randomized_picked_encounter = monster_dictionary.monster_picker(selected_dungeon)
        encounter_array.append(randomized_picked_encounter)
        encounter_size = encounter_size - 1

    # pass monster object and character object to combat
    experience_gained, character_alive = combat.receiving_monsters(encounter_array, selected_character)

    return experience_gained, character_alive
