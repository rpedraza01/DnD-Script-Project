import random


# This function rolls four 6-sided dice to create a stat value for the hero's attributes
# It then sorts the rolls greatest to lowest
# Then it returns the sum of the greatest 3 dice while dropping the lowest die value
def dice_roll_func():
    dice_rolls = [random.randint(1, 6) for _ in range(4)]
    dice_rolls.sort(reverse=True)
    return sum(dice_rolls[:3])


# This function randomly chooses a hero's class
def char_class_func():
    char_class_list = [
        "Barbarian",
        "Bard",
        "Cleric",
        "Druid",
        "Fighter",
        "Monk",
        "Paladin",
        "Ranger",
        "Rogue",
        "Sorcerer",
        "Warlock",
        "Wizard"
    ]
    rand_char_class_pick = random.choice(char_class_list)
    return rand_char_class_pick


# This function randomly chooses a hero's race
def char_race_func():
    char_race_list = [
        "Dwarf",
        "Elf",
        "Halfling",
        "Human",
        "Dragonborn",
        "Gnome",
        "Half-Elf",
        "Half-Orc",
        "Tiefling"
    ]
    rand_char_race_pick = random.choice(char_race_list)
    return rand_char_race_pick


# This function randomly chooses a hero's background
def char_bkgd_func():
    char_bkgd_list = [
        "Acolyte",
        "Charlatan",
        "Criminal",
        "Entertainer",
        "Folk Hero",
        "Gladiator",
        "Guild Artisan",
        "Guild Merchant",
        "Hermit",
        "Knight",
        "Noble",
        "Outlander",
        "Pirate",
        "Sage",
        "Sailor",
        "Soldier",
        "Urchin"
    ]
    rand_char_bkgd_pick = random.choice(char_bkgd_list)
    return rand_char_bkgd_pick
