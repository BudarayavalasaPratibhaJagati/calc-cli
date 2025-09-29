"""Calculation entity: holds operands + operation function, executes on demand."""
from dataclasses import dataclass
from typing import Callable, Sequence
Number = float | int

@dataclass(frozen=True, slots=True)
class Calculation:
    operation: Callable[[Sequence[Number]], Number]
    operands: tuple[Number, ...]
    def execute(self) -> Number:
        return self.operation(self.operands)
