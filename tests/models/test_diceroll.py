from parameterized import parameterized

from models.diceroll import Diceroll


def diceroll():
    d = Diceroll(1)
    d.dices = [3,4,5,6,6,1]
    return d


@parameterized.expand([
    (5, 1),
    (6, 2),
    ([3, 4, 5], 3)
])
def test_count(value, result):
    assert diceroll().count(value) == result


def test_str():
    assert str(diceroll()) == '1, 3, 4, 5, 6, 6'

@parameterized.expand([
    (2, False),
    (3, True),
    ([1, 5, 6], True),
    ((6, 6, 6), False),
])
def test_contains(value, result):
    assert (value in diceroll()) is result


def test_len():
    assert len(diceroll()) == 6

@parameterized.expand([
    (2, [1,2,3,4,5,6,6]),
    ([1,5], [1,1,3,4,5,5,6,6]),
])
def test_iadd(value, result):
    d = diceroll()
    d += value
    assert d.dices == result

@parameterized.expand([
    (3, [1,4,5,6,6]),
    (2, [1,3,4,5,6,6]),
    ([], [1,3,4,5,6,6]),
    ([5.2,5,6,6,6], [1,3,4]),
])
def test_remove(value, result):
    d = diceroll()
    d.remove(value)
    assert d.dices == result

@parameterized.expand([
    (2, [1,2,3,4,5,6,6]),
    ([2,6], [1,2,3,4,5,6,6,6]),
    ((2,6), [1,2,3,4,5,6,6,6]),
])
def test_iadd(value, result):
    d = diceroll()
    d += value
    assert d.dices == result
