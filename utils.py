import re
from functools import partial


def camel_to_snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def plural(x: int, v1: str, v2: str, v5: str) -> str:
    x1 = x % 100
    if 5 <= x1 <= 20:
        return f"{x} {v5}"
    x1 = x1 % 10
    if x1 == 1:
        return f"{x} {v1}"
    if x1 in (2, 3, 4):
        return f"{x} {v2}"
    return f"{x} {v5}"


def bound(value, minval, maxval):
    value = max(minval, value)
    value = min(maxval, value)
    return value


plural_dice = partial(plural, v1='кубик', v2="кубика", v5="кубиков")