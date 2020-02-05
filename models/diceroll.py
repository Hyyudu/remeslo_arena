from random import randint
from typing import List, Union


class Diceroll:
    dices: List[int]

    def __init__(self, dice_count):
        self.dices = sorted([randint(1, 6) for i in range(dice_count)])

    def count(self, values: Union[int, List[int]]):
        if isinstance(values, int):
            values = [values]
        return sum(self.dices.count(value) for value in values)

    def __str__(self):
        return ', '.join(map(str, self.dices))