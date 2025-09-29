"""In-memory calculation history."""
from typing import List
from .calculation import Calculation
class History:
    def __init__(self) -> None:
        self._items: List[Calculation] = []
    def add(self, calc: Calculation) -> None:
        self._items.append(calc)
    def all(self) -> list[Calculation]:
        return list(self._items)
    def clear(self) -> None:
        self._items.clear()
