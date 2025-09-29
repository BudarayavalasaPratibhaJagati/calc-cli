"""
Interactive REPL.
Author: Pratibha Jagati
Date: 2025-09-30
"""
from app.calculator import Calculator

PROMPT = "> "
HELP_TEXT = """Commands:
  add/subtract/multiply/divide <numbers...>
  history             Show past calculations
  help                Show this message
  exit                Quit the program
Examples:
  add 1 2 3
  divide 10 2
"""

def _is_command(line: str) -> bool:
    return line.strip().lower() in {"help", "history", "exit"}

def _print_history(calc: Calculator) -> None:
    for i, c in enumerate(calc.history.all(), start=1):
        op = c.operation.__name__
        nums = " ".join(map(str, c.operands))
        print(f"{i}. {op} {nums}")

def repl() -> None:  # pragma: no cover  # pragma: no cover
    calc = Calculator()
    print("Professional Calculator. Type 'help' to begin.")
    while True:
        try:
            line = input(PROMPT).strip()
        except EOFError:
            print()
            break
        if not line:
            continue  # pragma: no cover
        if _is_command(line):
            cmd = line.lower()
            if cmd == "help":
                print(HELP_TEXT)
            elif cmd == "history":
                _print_history(calc)
            elif cmd == "exit":
                print("Goodbye!")
                break
            continue
        tokens = line.split()
        try:
            result = calc.evaluate(tokens)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

def main() -> None:  # pragma: no cover
    repl()

if __name__ == "__main__":  # pragma: no cover
    main()
