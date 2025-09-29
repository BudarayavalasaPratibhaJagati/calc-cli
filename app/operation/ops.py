from typing import Sequence
Number = float | int

def add(values: Sequence[Number]) -> Number:
    total: Number = 0
    for v in values:
        total += v
    return total

def subtract(values: Sequence[Number]) -> Number:
    if not values:
        return 0
    result: Number = values[0]
    for v in values[1:]:
        result -= v
    return result

def multiply(values: Sequence[Number]) -> Number:
    if not values:
        return 0
    result: Number = 1
    for v in values:
        result *= v
    return result

def divide(values: Sequence[Number]) -> Number:
    if not values:
        return 0
    result: Number = values[0]
    for v in values[1:]:
        result /= v  # ZeroDivisionError bubbles up
    return result

REGISTRY = {
    "add": add,
    "sub": subtract,
    "subtract": subtract,
    "mul": multiply,
    "multiply": multiply,
    "div": divide,
    "divide": divide,
}
