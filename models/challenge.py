from typing import List, Union

from enums.attr import Attr


class Challenge:
    attrs: List[Attr]
    modifier: int = 0
    complexity: int = 1

    def __init__(
            self,
            attrs: Union[Attr, List[Attr]],
            modifier: int = 0,
            complexity: int = 1,
    ):
        self.attrs = [attrs] if isinstance(attrs, Attr) else attrs
        self.modifier = modifier
        self.complexity = complexity