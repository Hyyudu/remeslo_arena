from typing import Dict, List

from content.foe import Foe
from content.witcher import Witcher
from enums.combat_phase import CombatPhase
from models.diceroll import Diceroll
from models.listener import Listener
from utils import plural_dice


class Combat:
    witcher: Witcher
    foe: Foe
    listeners: Dict[CombatPhase, List[Listener]]
    round_number: int = 1

    def __init__(self, witcher: Witcher, foe: Foe):
        self.witcher = witcher
        self.foe = foe
        listener_sources = [
            witcher.skills,
            witcher.items,
            foe.skills,
        ]

    @property
    def finished(self):
        return self.witcher.hits <= 0 or self.foe.hits <= 0

    def battle_round(self):
        self.attack()
        self.defend()
        self.retaliate()

        self.round_number += 1
        if self.round_number >= 10:
            self.foe.hits = 0

    def attack(self):
        attack_dice_count = self.collect_attack_dice()
        print(f"{plural_dice(attack_dice_count)} на бросок")
        attack_roll = Diceroll(attack_dice_count)
        print(f"Результат броска: {attack_roll}")
        successes = attack_roll.count([5, 6])
        print(f"Успехов: {successes}")
        self.foe.hits -= successes
        print(f"Хиты противника: {self.foe.hits}")

    def defend(self):
        pass

    def retaliate(self):
        pass

    def collect_attack_dice(self):
        return self.witcher.str