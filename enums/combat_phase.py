from enum import Enum


class CombatPhase(Enum):
    attack_collect_dice = 'Удар/набор кубиков'
    block_collect_dice = 'Блок/набор кубиков'