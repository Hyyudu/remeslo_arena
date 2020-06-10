from enum import Enum


class CombatPhase(Enum):
    attack_collect_dice = 'Удар/набор кубиков'
    attack_rerolls = 'Удар/перебросы'
    attack_modify_roll = 'Удар/применение модификаторов'
    attack_count_successes = 'Удар/подсчет успехов'
    attack_apply_result = 'Удар/нанесение урона'
    block_collect_dice = 'Блок/набор кубиков'
    block_rerolls = 'Блок/перебросы'
    block_modify_roll = 'Блок/применение модификаторов'
    block_count_successes = 'Блок/подсчет успехов'
    block_apply_result = 'Блок/применение результатов'
    retaliate_collect_dice = 'Возмездие/набор кубиков'
    retaliate_rerolls = 'Возмездие/перебросы'
    retaliate_modify_roll = 'Возмездие/применение модификаторов'
    retaliate_count_successes = 'Возмездие/подсчет успехов'
    retaliate_apply_result = 'Возмездие/нанесение урона'