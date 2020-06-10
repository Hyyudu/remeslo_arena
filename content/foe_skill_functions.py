def slippery(
    success_count: int,
    attack: 'Attack',
):
    return max(0, success_count - 1 if 1 in attack.roll else success_count)

