from models.diceroll import Diceroll
from models.listener import apply_listeners
from models.makecheck import MakeCheck
from utils import bound


class Attack(MakeCheck):
    @apply_listeners
    def collect_dice(self) -> int:
        print(f'{self.witcher.name}: Сила {self.witcher.str}')
        return self.witcher.str

    @apply_listeners
    def modify_roll(self) -> Diceroll:
        return self.roll

    @apply_listeners
    def count_successes(self):
        return super().count_successes()

    @apply_listeners
    def apply_result(self):
        self.combat.foe.hits = self.combat.foe.hits - self.success_count
        print(f"Хиты противника: {self.combat.foe.hits}")


class Block(MakeCheck):
    @apply_listeners
    def collect_dice(self) -> int:
        block = self.combat.foe.block
        print(f'Блок: {block}')
        return sum([self.witcher.get_attr(attr) for attr in block.attrs]) + block.modifier

    @apply_listeners
    def modify_roll(self) -> Diceroll:
        return self.roll

    @apply_listeners
    def count_successes(self):
        return super().count_successes()

    @apply_listeners
    def apply_result(self):
        if self.count_successes() >= self.combat.foe.block.difficulty:
            self.combat.block_count += 1


class Retaliate(MakeCheck):
    @apply_listeners
    def collect_dice(self) -> int:
        foe = self.combat.foe
        print(f'{foe.name}: возмездие {foe.attack}/{foe.to_hit} ({foe.damage})')
        return foe.attack

    @apply_listeners
    def modify_roll(self) -> Diceroll:
        return self.roll

    @apply_listeners
    def count_successes(self):
        success_count = self.roll.count([x for x in range(7) if x >= self.combat.foe.to_hit])
        self.success_count = max(0, success_count - self.combat.block_count)
        return self.success_count

    @apply_listeners
    def apply_result(self):
        self.combat.witcher.hits -= self.success_count * self.combat.foe.damage
        print(f"Хиты ведьмака: {self.combat.witcher.hits}")
