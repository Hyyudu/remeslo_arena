from typing import List

from models.check import Check
from content import foe_skill
from enums.areal import Areal
from enums.attr import Attr
from content.coded import Coded
from enums.foe_trait import FoeTrait


class Foe(Coded):
    areal: Areal
    name: str
    traits: List[FoeTrait]
    skills: List[foe_skill.FoeSkill]
    _hits: int

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


class Drowner(Foe):
    areal = Areal.forest
    name = 'Утопец'
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
    attack = 2
    to_hit = 5
    damage = 1
    evade = Check(Attr.dex)
    block = Check(Attr.str, +1)
