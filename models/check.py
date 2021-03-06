from dataclasses import dataclass
from typing import List, Union

from content.coded import Coded
from enums.attr import Attr
from utils import plus_minus


@dataclass
class Check(Coded):
    attr: Union[Attr, List[Attr]]
    modifier: int = 0
    difficulty: int = 1

    @property
    def attrs(self):
        return [self.attr] if isinstance(self.attr, Attr) else self.attr

    def __str__(self):
        attrs_list = "+".join([attr.value for attr in self.attrs])
        return f'{attrs_list}({plus_minus(self.modifier)})' + (f'[{self.difficulty}]' if self.difficulty != 1 else '')