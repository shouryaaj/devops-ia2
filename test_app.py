import pytest

from app import add, divide, validate_name


def test_add():
    assert add(2, 3) == 6


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


def test_validate_name_strips_whitespace():
    assert validate_name("  Alice  ") == "Alice"


def test_validate_name_rejects_empty_string():
    with pytest.raises(ValueError, match="Name cannot be empty"):
        validate_name("   ")
