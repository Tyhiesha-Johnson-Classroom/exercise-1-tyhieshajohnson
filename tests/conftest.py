import sys, pathlib
# Add the exercise folder (parent of tests) to sys.path so 'src' is importable
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
