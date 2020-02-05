from dataclasses import dataclass
from typing import Callable, Union

from enums.combat_phase import CombatPhase


@dataclass
class Listener:
    description: str
    phase: CombatPhase
    func: Callable
    source: Union['Witcher', 'Item', 'Foe'] = None
    priority: int = 0

