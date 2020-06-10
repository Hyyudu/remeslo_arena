from typing import List

from content import foe_skill_functions as fs_func
from content.coded import Coded
from enums.combat_phase import CombatPhase
from models.listener import Listener


class FoeSkill(Coded):
    name: str
    listeners: List[Listener]


class Agile(FoeSkill):
    name = 'Верткий'
    listeners = [
        Listener(
            description='При Ударе 6 не дает успехов',
            phase=CombatPhase.attack_count_successes,
            func=fs_func.agile,
            is_applicable=lambda success_count, attack: 6 in attack.roll
        )
    ]


class Press(FoeSkill):
    name = 'Натиск'
    listeners = [
        Listener(
            description='Если противник не получил ран в фазу Атаки, 1 хит противника заменяется на буст',
            phase=CombatPhase.attack_count_successes,
            func=fs_func.press,
            is_applicable=lambda success_count, attack: success_count == 0 and attack.combat.foe.hits > 0
        )
    ]

class Slippery(FoeSkill):
    name = 'Скользкий'
    listeners = [
        Listener(
            description="В фазу Удара, если в результатах броска есть 1, отмените 1 Успех",
            phase=CombatPhase.attack_count_successes,
            func=fs_func.slippery,
            is_applicable=lambda success_count, attack: 1 in attack.roll and success_count > 0
        )
    ]


