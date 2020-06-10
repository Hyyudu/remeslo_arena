from typing import List

from content import foe_skill
from content.coded import Coded
from enums.areal import Areal
from enums.attr import Attr
from enums.foe_trait import FoeTrait
from models.check import Check
from models.listener import assign_listeners


class Foe(Coded):
    areal: Areal
    name: str
    level: int
    traits: List[FoeTrait]
    skills: List[foe_skill.FoeSkill]
    _hits: int
    boosts: int = 0

    @property
    def hits(self):
        return self.hits

    @hits.setter
    def hits(self, value):
        self._hits = max(0, value)

    attack: int
    to_hit: int
    damage: int
    evade: Check
    block: Check

    def __init__(self):
        for skill in self.skills:
            assign_listeners(self, skill.listeners)


class Drowner(Foe):
    areal = Areal.forest
    name = 'Утопец'
    level = 1
    traits = [
        FoeTrait.night,
        FoeTrait.weak,
        FoeTrait.water,
        FoeTrait.pack,
    ]
    skills = [
        foe_skill.Slippery
    ]
    hits = 5
    attack = 3
    to_hit = 5
    damage = 1
    evade = Check(Attr.dex)
    block = Check(Attr.str, +1)


class Ekimma(Foe):
    areal = Areal.mountain
    name = 'Экимма'
    level = 1
    traits = [
        FoeTrait.night,
        FoeTrait.weak,
        FoeTrait.scoffer,
    ]
    skills = [
        foe_skill.Agile,
        foe_skill.Press,
    ]
    hits = 3
    attack = 2
    to_hit = 4
    damage = 1
    evade = Check(Attr.dex, -1)
    block = Check([Attr.str, Attr.dex], difficulty=2)
    # Сопротивление к стали