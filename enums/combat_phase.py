from enum import Enum


class CombatPhase(Enum):
    attack_collect_dice = 'Удар/набор кубиков'
    attack_rerolls = 'Удар/перебросы'
    attack_modify_roll = 'Удар/применение модификаторов'
    attack_count_successes = 'Удар/подсчет успехов'
    block_collect_dice = 'Блок/набор кубиков'