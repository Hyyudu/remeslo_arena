from typing import List,  Dict

from content.coded import Coded
from enums.attr import Attr


class Witcher(Coded):
    attrs: Dict[Attr,  List[int]]
    hits: int
    toxic: int
    signs: int
    alchemy: int

    @property
    def offhand_free(self):
        return True


class Ferret(Witcher):
    attrs = {
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