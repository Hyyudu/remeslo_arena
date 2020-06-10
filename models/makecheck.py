from dataclasses import dataclass

from content.coded import Coded
from content.witcher import Witcher
from models.diceroll import Diceroll
from utils import plural_dice


@dataclass
class MakeCheck(Coded):
    combat: 'Combat'
    witcher: 'Witcher'
    roll: Diceroll = None
    success_count: int = None

    def process(self):
        dice_count = self.collect_dice()
        # print(f"{plural_dice(dice_count)} на бросок")
        self.roll = Diceroll(dice_count)
        print(f"Результат броска: {self.roll}")
        if self.append_roll():
            print(f"Бросок с дополнением: {self.roll}")
        if self.modify_roll() != self.roll:
            print(f'Модифицированный бросок: {self.roll}')
        self.success_count = self.count_successes()
        print(f"Успехов: {self.success_count}")
        self.apply_result()

    def collect_dice(self) -> int:
        pass

    def append_roll(self) -> bool:
        return False

    def modify_roll(self) -> bool:
        return False

    def count_successes(self):
        return self.roll.count([5, 6])

    def apply_result(self):
        pass


