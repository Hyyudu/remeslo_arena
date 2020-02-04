from content.foes import Drowner
from content.witchers import Ferret
from models.combat import Combat

if __name__ == '__main__':
    witcher = Ferret()
    foe = Drowner()
    combat = Combat(witcher, foe)
    while not combat.finished:
        combat.battle_round()