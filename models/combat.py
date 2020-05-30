from itertools import chain
from typing import Dict, List

from content.foe import Foe
from content.witcher import Witcher
from enums.combat_phase import CombatPhase
from models.check import Check
from models.combat_action import Attack
from models.diceroll import Diceroll
from models.listener import Listener, apply_listeners
from utils import plural_dice, simulate_select


class Combat:
    witcher: Witcher
    foe: Foe
    listeners: Dict[CombatPhase, List[Listener]] = {}
    round_number: int = 1
    attack_roll: Diceroll = None
    block_roll: Diceroll = None
    evade_roll: Diceroll = None
    cast_roll: Diceroll = None
    retal_roll: Diceroll = None

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
        Attack(combat=self, witcher=self.witcher).process()
        self.defend()
        self.retaliate()

        self.round_number += 1
        if self.round_number >= 10:
            self.foe.hits = 0

    def defend(self):
        defence_options = ['block', 'evade', 'sign']
        defence_action = simulate_select(defence_options)
        if defence_action == 'block':
            self.block()

    def block(self):
        block_dice_count = self.block_collect_dice()
        print(f"{plural_dice(block_dice_count)} на блок")
        self.block_roll = Diceroll(block_dice_count)
        print(f"Результат броска: {self.block_roll}")
        self.block_modify_roll()
        successes = self.block_count_successes()
        print(f"Успехов: {successes}")

    def retaliate(self):
        pass

    @apply_listeners
    def block_collect_dice(self) -> int:
        block_check: Check = self.foe.block
        return sum([
            getattr(self.witcher, attr.name)
            for attr in block_check.attrs
        ]) + block_check.modifier

    @apply_listeners
    def block_modify_roll(self) -> Diceroll:
        return self.block_roll

    @apply_listeners
    def block_count_successes(self) -> int:
        return self.block_roll.count([5, 6])
