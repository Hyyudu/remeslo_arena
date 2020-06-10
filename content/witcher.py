from typing import List,  Dict

from content.coded import Coded
from content.item import Item, SteelWitcherSword1
from enums.attr import Attr
from enums.defence_action import DefenceAction
from models.listener import Listener


class Witcher(Coded):
    name: str
    attr_tables: Dict[Attr, List[int]]
    runners: Dict[Attr, int] = {
        Attr.str: 1,
        Attr.spd: 1,
        Attr.soc: 1
    }
    hits: int
    toxic: int
    signs: int
    alchemy: int
    items: List[Item] = []
    skills: List[Listener] = []

    @property
    def offhand_free(self):
        return True

    @property
    def str(self): return self.attr_tables[Attr.str][self.runners[Attr.str]]

    @property
    def dex(self): return self.attr_tables[Attr.dex][self.runners[Attr.str]]

    @property
    def spd(self): return self.attr_tables[Attr.spd][self.runners[Attr.spd]]

    @property
    def meta(self): return self.attr_tables[Attr.meta][self.runners[Attr.spd]]

    @property
    def soc(self): return self.attr_tables[Attr.soc][self.runners[Attr.soc]]

    @property
    def luck(self): return self.attr_tables[Attr.luck][self.runners[Attr.soc]]

    def get_attr(self, attr: Attr):
        return getattr(self, attr.name)

    def defence_desicion(self) -> DefenceAction:
        return DefenceAction.block


class Ferret(Witcher):
    name = 'Хорёк'
    attr_tables = {
        Attr.str: [4, 3, 2], 
        Attr.meta: [2, 3, 4], 
        Attr.spd: [4, 3, 2], 
        Attr.dex: [2, 3, 4], 
        Attr.soc: [4, 3, 2], 
        Attr.luck: [1, 2, 3], 
    }
    hits = 5
    toxic = 5
    signs = 2
    alchemy = 3
