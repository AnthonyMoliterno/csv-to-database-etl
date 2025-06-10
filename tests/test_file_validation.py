import pytest
from app.file_validation import check_file
import os

def test_check_file_valid(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("dummy")
    assert check_file(str(file)) == str(file)

def test_check_file_missing():
    with pytest.raises(FileNotFoundError):
        check_file("nonexistent.csv")

def test_check_file_invalid_extension(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("dummy")
    with pytest.raises(ValueError):
        check_file(str(file))
