from typing import Dict


def flat_bonus(modifier):
    def func(result: int, combat: 'Combat' = None):
        return result + modifier
    return func


def diceroll_modify_least(modfiers: Dict[int, int]):
    def func(roll: 'Diceroll', combat: 'Combat' = None):
        for index, modif in modfiers.items():
            if index < len(roll):
                roll[index] += modif
        roll.dices.sort()
        return roll
    return func