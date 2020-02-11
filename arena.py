from content.foe import Drowner
from content.item import LightSilverSword3, SteelWitcherSword1
from content.witcher import Ferret
from enums.attr import Attr
from models.combat import Combat

if __name__ == '__main__':
    witcher = Ferret()
    foe = Drowner()
    witcher.items.append(SteelWitcherSword1())
    combat = Combat(witcher, foe)
    while not combat.finished:
        combat.battle_round()