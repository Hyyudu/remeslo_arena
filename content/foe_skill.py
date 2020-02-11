from typing import List

from content import foe_skill_functions as fs_func
from content.coded import Coded
from enums.combat_phase import CombatPhase
from models.listener import Listener


class FoeSkill(Coded):
    name: str
    listeners: List[Listener]


class Slippery(FoeSkill):
    name = 'Скользкий'
    listeners = [
        Listener(
            description="В фазу Удара, если в результатах броска есть 1, отмените 1 Успех",
            phase=CombatPhase.attack_count_successes,
            func=fs_func.slippery,
            is_applicable=lambda success_count, combat: 1 in combat.attack_roll and success_count > 0
        )
    ]

