from content.foe import Drowner
from content.witcher import Ferret
from enums.attr import Attr
from models.combat import Combat

if __name__ == '__main__':
    witcher = Ferret()
    witcher.runners[Attr.str] = 0
    foe = Drowner()
    combat = Combat(witcher, foe)
    while not combat.finished:
        combat.battle_round()