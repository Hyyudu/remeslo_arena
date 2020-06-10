import inspect

from dataclasses import dataclass
from typing import Callable, Union, List, Any

from enums.combat_phase import CombatPhase


@dataclass
class Listener:
    description: str
    phase: CombatPhase
    func: Callable
    is_applicable: Callable = lambda *args, **kwargs: True
    source: Union['Witcher', 'Item', 'Foe'] = None
    priority: int = 0

    @property
    def present(self):
        return f"{self.source.name}: {self.description}"


def assign_listeners(obj, listeners: List[Listener]):
    for listener in listeners:
        listener.source = obj


def apply_listeners(func):
    def wrapper(obj):
        result = func(obj)
        phase = obj.__class__.__name__.lower() + '_' + func.__name__
        listeners_source: List[Listener] = obj.combat.listeners.get(CombatPhase[phase]) or []
        for listener in listeners_source:
            if listener.is_applicable(result, obj):
                print(listener.present)
                result = listener.func(result, obj)
        return result
    return wrapper
