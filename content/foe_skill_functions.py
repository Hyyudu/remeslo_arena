def slippery(
    success_count: int,
    combat: 'Combat',
):
    return max(0, success_count - 1 if 1 in combat.attack_roll else success_count)


