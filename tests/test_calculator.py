from app.calculator import Calculator
def test_calculator_evaluate_and_history():
    calc = Calculator()
    result = calc.evaluate(["add","1","2"])
    assert result == 3
    assert len(calc.history.all()) == 1
