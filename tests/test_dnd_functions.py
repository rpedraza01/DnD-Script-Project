import pytest
import source.dnd_functions as dnd_functions


def test_dice_roll_func():

    for x in range(7):
        result = dnd_functions.dice_roll_func()
        print(result)
        assert 3 <= result <= 18


@pytest.fixture()
def char_classes():
    char_classes = [
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
    return char_classes


def test_char_class_func(char_classes):
    for x in range(12):
        result = dnd_functions.char_class_func()
        print(result)
        assert result in char_classes


@pytest.fixture()
def char_race():
    char_race = [
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
    return char_race


def test_char_race_func(char_race):
    for x in range(9):
        result = dnd_functions.char_race_func()
        print(result)
        assert result in char_race


@pytest.fixture()
def char_background():
    char_background = [
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
    return char_background


def test_char_background_func(char_background):
    for x in range(17):
        result = dnd_functions.char_bkgd_func()
        print(result)
        assert result in char_background
