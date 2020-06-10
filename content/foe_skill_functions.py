def agile(success_count: int, attack: 'Attack'):  # Верткий
    return success_count - attack.roll.count(6)


def press(success_count: int, attack: 'Attack'):  # Натиск
    foe = attack.combat.foe
    foe.hits -= 1
    foe.boosts += 1
    return success_count


def slippery(success_count: int, attack: 'Attack'):  # Скользкий
    return max(0, success_count - 1 if 1 in attack.roll else success_count)

