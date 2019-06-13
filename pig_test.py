import pytest

from oopig import Dice, Player

def test_dice_roll():
    dice = Dice()
    assert (dice.roll() in range(1, 7))

def test_name():
    player1 = Player('Michael')
    assert player1.name == "Michael"

def test_add_score():
    player1 = Player('Michael')
    player_score = 2
    assert player1.add_score(player_score) != 3
