import importlib

def test_main_imports_and_has_symbols():
    m = importlib.import_module("app.main")
    assert hasattr(m, "repl")
    assert hasattr(m, "main")
