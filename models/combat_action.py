from content.coded import Coded
from models.makecheck import MakeCheck
from models.diceroll import Diceroll
from models.listener import apply_listeners
from utils import plural_dice, bound


class Attack(MakeCheck):
    @apply_listeners
    def collect_dice(self) -> int:
        return self.witcher.str

    @apply_listeners
    def modify_roll(self) -> Diceroll:
        return self.roll

    @apply_listeners
    def count_successes(self):
        return super().count_successes()

    @apply_listeners
    def apply_result(self):
        self.combat.foe.hits = bound(self.combat.foe.hits - self.count_successes(), 0, 999)
        print(f"Хиты противника: {self.combat.foe.hits}")