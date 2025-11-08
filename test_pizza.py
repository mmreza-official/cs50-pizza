import subprocess
import sys
import os
from pathlib import Path

# Use the same Python interpreter running the tests
PYTHON = sys.executable


def run_cli(*args):
    """Run the pizza.py script with the given arguments and capture output."""
    result = subprocess.run(
        [PYTHON, "pizza.py", *args],
        capture_output=True,
        text=True
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def test_no_args():
    """Ensure the program exits when no argument is given."""
    code, out, err = run_cli()
    assert code != 0
    assert "Too few command-line arguments" in (out or err)


def test_many_args():
    """Ensure the program exits when too many arguments are given."""
    code, out, err = run_cli("a.csv", "b.csv")
    assert code != 0
    assert "Too many command-line arguments" in (out or err)


def test_not_csv_file(tmp_path):
    """Ensure non-CSV files are rejected."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("hello", encoding="utf-8")

    code, out, err = run_cli(str(test_file))
    assert code != 0
    assert "Not a CSV file" in (out or err)


def test_file_not_found():
    """Ensure missing file triggers proper error."""
    code, out, err = run_cli("not_exists.csv")
    assert code != 0
    assert "File does not exist" in (out or err)


def test_table_output(tmp_path):
    """Ensure CSV data is displayed as a formatted table."""
    sample = tmp_path / "sample.csv"
    sample.write_text(
        "Name,Age\n"
        "Ali,20\n"
        "Sara,22\n",
        encoding="utf-8"
    )

    code, out, err = run_cli(str(sample))
    assert code == 0
    assert "Ali" in out
    assert "Sara" in out
    assert "Age" in out
