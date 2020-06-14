from random import randint
from typing import (
    Iterable,
    List,
    Union,
)

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
        if isinstance(item, int):
            return item in self.dices
        if isinstance(item, (list, tuple)):
            dicecopy = self.dices[:]
            self.remove(item)
            contains = len(self.dices) + len(item) == len(dicecopy)
            self.dices = dicecopy
            return contains

    def remove(self, value):
        if isinstance(value, int):
            if value in self.dices:
                self.dices.remove(value)
        else:
            for item in value:
                if item in self.dices:
                    self.dices.remove(item)
        self.dices.sort()

    def __len__(self):
        return len(self.dices)

    def __iadd__(self, other):
        if isinstance(other, int):
            self.dices.append(other)
        else:
            self.dices += other
        self.dices.sort()
        return self

