from typing import Dict, List

from content.coded import Coded
from enums.combat_phase import CombatPhase
from models.listener import Listener


class Item(Coded):
    name: str
    listeners: List[Listener]

    def __init__(self):
        for listener in self.listeners:
            listener.source = self


class SteelWitcherSword1(Item):
    name = 'Стальной меч ведьмака'
    listeners = [
        Listener(
            description="+4 к Удару",
            phase=CombatPhase.attack_collect_dice,
            func=lambda x: x+4,
        )
    ]