import pytest
from app.calculation.calculation import Calculation
from app.calculation.factory import build_from_tokens
from app.calculation.history import History
from app.operation import add

def test_calculation_execute():
    c = Calculation(operation=add, operands=(1,2,3))
    assert c.execute() == 6

@pytest.mark.parametrize("tokens, expected", [
    (["add","1","2","3"], 6),
    (["subtract","5","2"], 3),
    (["multiply","2","3","4"], 24),
    (["divide","8","2"], 4),
])
def test_factory_and_execution(tokens, expected):
    calc = build_from_tokens(tokens)
    assert calc.execute() == expected

@pytest.mark.parametrize("bad", [
    [],
    ["foo","1"],
    ["add"],
    ["add","x"],
])
def test_factory_errors(bad):
    with pytest.raises(ValueError):
        build_from_tokens(bad)

def test_history_add_and_all():
    h = History()
    c = Calculation(operation=add, operands=(1,))
    h.add(c)
    items = h.all()
    assert len(items) == 1 and items[0].operands == (1,)
    h.clear()
    assert h.all() == []
def test_factory_handles_floats():
    from app.calculation.factory import build_from_tokens
    calc = build_from_tokens(["add","1.5","2.5"])
    assert calc.execute() == 4.0
