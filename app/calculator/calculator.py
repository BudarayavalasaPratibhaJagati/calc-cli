"""Calculator facade that uses factory + history."""
from app.calculation.factory import build_from_tokens
from app.calculation.history import History

class Calculator:
    def __init__(self) -> None:
        self.history = History()

    def evaluate(self, tokens: list[str]) -> float | int:
        calc = build_from_tokens(tokens)
        result = calc.execute()
        self.history.add(calc)
        return result
