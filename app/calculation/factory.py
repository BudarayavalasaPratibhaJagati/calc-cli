"""Factory to build Calculation from user tokens."""
from typing import Iterable
from app.operation import REGISTRY
from .calculation import Calculation

def _to_number(tok: str):
    try:
        if "." in tok:
            return float(tok)
        return int(tok)
    except ValueError as e:
        raise ValueError(f"Invalid number: '{tok}'") from e

def build_from_tokens(tokens: Iterable[str]) -> Calculation:
    tokens = list(tokens)
    if not tokens:
        raise ValueError("No input provided")
    op = tokens[0].lower()
    if op not in REGISTRY:
        raise ValueError(f"Unknown operation: {op}")
    if len(tokens) < 2:
        raise ValueError("Provide at least one number")
    nums = tuple(_to_number(t) for t in tokens[1:])
    return Calculation(operation=REGISTRY[op], operands=nums)
