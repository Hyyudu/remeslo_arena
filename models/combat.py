from itertools import chain
from typing import Dict, List

from content.foe import Foe
from content.witcher import Witcher
from enums.combat_phase import CombatPhase
from models.diceroll import Diceroll
from models.listener import Listener, apply_listeners
from utils import plural_dice


class Combat:
    witcher: Witcher
    foe: Foe
    listeners: Dict[CombatPhase, List[Listener]] = {}
    round_number: int = 1
    attack_roll: Diceroll = None
    defend_diceroll: Diceroll = None

    def __init__(self, witcher: Witcher, foe: Foe):
        self.witcher = witcher
        self.foe = foe
        listener_sources = [
            witcher.skills,
            witcher.items,
            foe.skills,
        ]
        for listener_source in listener_sources:
            if not listener_source:
                continue
            if hasattr(listener_source[0], 'listeners'):
                listeners = list(chain(*[item.listeners for item in listener_source]))
            else:
                listeners = listener_source
            for listener in listeners:
                self.listeners.setdefault(listener.phase, [])
                self.listeners[listener.phase].append(listener)
        for phase, phase_listeners in self.listeners.items():
            phase_listeners.sort(key=lambda listener: listener.priority)


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
        attack_dice_count = self.attack_collect_dice()
        print(f"{plural_dice(attack_dice_count)} на бросок")
        self.attack_roll = Diceroll(attack_dice_count)
        print(f"Результат броска: {self.attack_roll}")
        self.attack_modify_roll()
        successes = self.attack_count_successes()
        print(f"Успехов: {successes}")
        self.foe.hits -= successes
        print(f"Хиты противника: {self.foe.hits}")

    def defend(self):
        pass

    def retaliate(self):
        pass

    @apply_listeners
    def attack_collect_dice(self):
        return self.witcher.str

    @apply_listeners
    def attack_modify_roll(self):
        return self.attack_roll

    @apply_listeners
    def attack_count_successes(self):
        return self.attack_roll.count([5,6])
