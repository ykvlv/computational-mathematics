from dataclasses import dataclass
from typing import List


@dataclass
class Equation:
    dif: List
    ex: List
    a: float
    b: float
    y0: float


def format_float(x):
    return f'{x:.5f}'
