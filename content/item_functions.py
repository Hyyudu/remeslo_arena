from typing import Dict

from enums.combat_phase import CombatPhase
from enums.item_trait import ItemTrait
from models.listener import Listener
from utils import plus_minus


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


class LsrAttackBonus(Listener):
    material: ItemTrait
    modifier: int

    def __init__(self, modifier: int = 0, material: ItemTrait = None):
        self.modifier = modifier
        self.material = material
        self.phase = CombatPhase.attack_collect_dice

    @property
    def present(self):
        return f'Удар {plus_minus(self.modifier)}' + (f' ({self.material.value})' if self.material else '')

    def func(self, result, attack: 'Attack'):
        modifier = self.modifier
        if self.material in attack.combat.foe.resistance:
            modifier = min(1, modifier)
        return result + modifier
