import pytest

from oopig import Dice

def test_dice_roll():
    dice = Dice()
    assert (dice.roll() in range(1, 7))