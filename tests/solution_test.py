import builtins
import importlib
import sys
import re
from contextlib import redirect_stdout
from io import StringIO

# Helper to run the student's script with mocked stdin sequence
def run_script_with_inputs(inputs):
    it = iter(inputs)
    original_input = builtins.input
    buf = StringIO()
    try:
        # Mock input BEFORE import/reload so import-time input() uses our values
        builtins.input = lambda prompt=None: next(it)

        # Ensure a fresh import each run (so global code re-executes with new inputs)
        if "src.solution" in sys.modules:
            del sys.modules["src.solution"]

        # Capture all prints that happen during import
        with redirect_stdout(buf):
            importlib.import_module("src.solution")
    finally:
        builtins.input = original_input
    return buf.getvalue()

def number_in_text(text):
    """Prefer the number on the 'area' line; fall back to the first number."""
    for line in text.splitlines():
        if "area" in line.lower():
            m = re.search(r"(-?\d+(?:\.\d+)?)", line)
            if m:
                return float(m.group(1))
    m = re.search(r"(-?\d+(?:\.\d+)?)", text)
    return float(m.group(1)) if m else None


def test_q1_greeting_includes_name_and_age(monkeypatch):
    out = run_script_with_inputs(["Anele", "21", "5", "6", "25.0"])
    lower = out.lower()
    assert "anele" in lower, "Greeting should include the provided name."
    assert "21" in lower, "Greeting should include the provided age."

def test_q2_area_multiplication_result_numeric():
    # length=7, width=8 → area = 56
    out = run_script_with_inputs(["Bo", "30", "7", "8", "0"])
    val = number_in_text(out)
    assert val is not None, "Area should be printed as a number."
    assert abs(val - 56) < 1e-9, "Area should be length * width (7*8=56)."

def test_q3_celsius_to_fahrenheit_rounded():
    # C=25.3 → F = (25.3*9/5)+32 = 77.54
    out = run_script_with_inputs(["Chen", "18", "1", "1", "25.3"])
    # Find a number with 2 dp; accept either 77.54 or formatted equivalent
    matches = re.findall(r"(-?\d+\.\d{2})", out)
    assert matches, "Output should include a number rounded to 2 decimals."
    nums = list(map(float, matches))
    assert any(abs(n - 77.54) < 1e-2 for n in nums), "Expected ~77.54 in output."
