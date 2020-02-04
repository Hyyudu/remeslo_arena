from dataclasses import dataclass

from content.foes import Foe
from content.witchers import Witcher


@dataclass
class Combat:
    witcher: Witcher
    foe: Foe
    round_number: int = 1

    @property
    def finished(self):
        return self.witcher.hits <= 0 or self.foe.hits <= 0

    def battle_round(self):
        self.attack()
        self.defend()
        self.retaliate()

        self.round_number += 1
        if self.round_number >= 10:
            self.foe.hits = 0

    def attack(self):
        pass

    def defend(self):
        pass

    def retaliate(self):
        pass