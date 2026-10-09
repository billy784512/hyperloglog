import dataclasses
from typing import List


@dataclasses
class Sketch:

    # numbers of bucket 
    m: int
    ranks: List[int]

    def __post_init__(self):
        if len(self.ranks) != self.m:
            raise ValueError("Invalid sketch format")