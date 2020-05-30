from typing import List

from content.coded import Coded
from content import item_functions as item_funcs
from enums.combat_phase import CombatPhase
from models.listener import Listener, assign_listeners


class Item(Coded):
    name: str
    listeners: List[Listener]

    def __init__(self):
        assign_listeners(self, self.listeners)


def LsrAttackBonus(modifier):
    return Listener(
        description=f"Удар +{modifier}",
        phase=CombatPhase.attack_collect_dice,
        func=item_funcs.flat_bonus(modifier),
    )


def LsrBlockBonus(modifier):
    return Listener(
        description=f"Блок +{modifier}",
        phase=CombatPhase.block_collect_dice,
        func=item_funcs.flat_bonus(modifier),
    )


class SteelWitcherSword1(Item):
    name = 'Стальной меч ведьмака'
    listeners = [
        LsrAttackBonus(4),
        LsrBlockBonus(1),
    ]

class LightSilverSword3(Item):
    name = 'Легкий серебряный меч'
    listeners = [
        LsrAttackBonus(2),
        LsrBlockBonus(1),
        Listener(
            description='После броска Удара добавляет +1 к кубику с наименьшим значением',
            phase=CombatPhase.attack_modify_roll,
            func=item_funcs.diceroll_modify_least({0: 1}),
        )
    ]

