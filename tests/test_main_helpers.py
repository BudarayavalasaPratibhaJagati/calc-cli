import io
import contextlib
from app.main import _is_command, _print_history
from app.calculator import Calculator

def test_is_command_true_false():
    assert _is_command("help")
    assert _is_command("history")
    assert _is_command("exit")
    assert not _is_command("add 1 2")  # not a pure command

def test_print_history_outputs_first_line():
    calc = Calculator()
    # add one calc to history
    calc.evaluate(["add","1","2"])
    # capture stdout
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        _print_history(calc)
    out = buf.getvalue().strip()
    assert out.startswith("1. add 1 2")
