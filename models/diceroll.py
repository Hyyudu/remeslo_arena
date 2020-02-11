from random import randint
from typing import List, Union

from utils import bound


class Diceroll():
    dices: List[int]

    def __init__(self, dice_count):
        self.dices = sorted([randint(1, 6) for i in range(dice_count)])

    def count(self, values: Union[int, List[int]]):
        if isinstance(values, int):
            values = [values]
        return sum(self.dices.count(value) for value in values)

    def __str__(self):
        return ', '.join(map(str, sorted(self.dices)))

    def __contains__(self, item):
        return item in self.dices

    def __len__(self):
        return len(self.dices)

    def __getitem__(self, item):
        return self.dices[item]

    def __setitem__(self, key, value):
        self.dices[key] = bound(value, 1, 6)